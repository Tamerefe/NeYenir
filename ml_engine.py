"""
Yemek-Alkol Eşleştirmesi için Gelişmiş Makine Öğrenimi Modülü
Sinir ağları, işbirlikçi filtreleme ve öneri algoritmalarını içerir
"""

import numpy as np
import json
import pickle
from typing import Dict, List, Tuple, Optional, Union
from datetime import datetime, timedelta
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import logging

logger = logging.getLogger(__name__)

class NeuralNetworkRecommender:
    """Yemek-alkol eşleştirme tahminleri için basit bir sinir ağı sınıfı"""
    
    def __init__(self, input_size: int = 20, hidden_size: int = 64, output_size: int = 1):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        # Ağırlıkları ve bias'ları başlat
        self.W1 = np.random.randn(input_size, hidden_size) * 0.1
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, hidden_size) * 0.1
        self.b2 = np.zeros((1, hidden_size))
        self.W3 = np.random.randn(hidden_size, output_size) * 0.1
        self.b3 = np.zeros((1, output_size))
        
        self.learning_rate = 0.001
        self.trained = False
    
    def sigmoid(self, x):
        """Sigmoid activation function"""
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    
    def relu(self, x):
        """ReLU activation function"""
        return np.maximum(0, x)
    
    def forward(self, X):
        """Forward propagation"""
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.relu(self.z1)
        
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.relu(self.z2)
        
        self.z3 = np.dot(self.a2, self.W3) + self.b3
        self.a3 = self.sigmoid(self.z3)
        
        return self.a3
    
    def backward(self, X, y, output):
        """Backward propagation"""
        m = X.shape[0]
        
        # Output layer
        dZ3 = output - y.reshape(-1, 1)
        dW3 = (1/m) * np.dot(self.a2.T, dZ3)
        db3 = (1/m) * np.sum(dZ3, axis=0, keepdims=True)
        
        # Hidden layer 2
        dA2 = np.dot(dZ3, self.W3.T)
        dZ2 = dA2 * (self.z2 > 0)  # ReLU derivative
        dW2 = (1/m) * np.dot(self.a1.T, dZ2)
        db2 = (1/m) * np.sum(dZ2, axis=0, keepdims=True)
        
        # Hidden layer 1
        dA1 = np.dot(dZ2, self.W2.T)
        dZ1 = dA1 * (self.z1 > 0)  # ReLU derivative
        dW1 = (1/m) * np.dot(X.T, dZ1)
        db1 = (1/m) * np.sum(dZ1, axis=0, keepdims=True)
        
        # Update weights
        self.W3 -= self.learning_rate * dW3
        self.b3 -= self.learning_rate * db3
        self.W2 -= self.learning_rate * dW2
        self.b2 -= self.learning_rate * db2
        self.W1 -= self.learning_rate * dW1
        self.b1 -= self.learning_rate * db1
    
    def train(self, X_train, y_train, epochs=100):
        """Train the neural network"""
        losses = []
        
        for epoch in range(epochs):
            # Forward pass
            output = self.forward(X_train)
            
            # Calculate loss (MSE)
            loss = np.mean((output.flatten() - y_train) ** 2)
            losses.append(loss)
            
            # Backward pass
            self.backward(X_train, y_train, output)
            
            if epoch % 20 == 0:
                logger.info(f"Epoch {epoch}, Loss: {loss:.4f}")
        
        self.trained = True
        return losses
    
    def predict(self, X):
        """Make predictions"""
        if not self.trained:
            logger.warning("Model not trained yet. Using random predictions.")
            return np.random.rand(X.shape[0])
        
        predictions = self.forward(X)
        return predictions.flatten()

class CollaborativeFilter:
    """Kullanıcı tabanlı öneriler için işbirlikçi filtreleme sınıfı"""
    
    def __init__(self):
        self.user_item_matrix = None
        self.user_similarities = None
        self.item_similarities = None
        self.fitted = False
    
    def fit(self, ratings_data: List[Tuple[int, int, int, int]]):
        """
        Fit the collaborative filtering model
        Args:
            ratings_data: List of (user_id, food_id, alcohol_id, rating) tuples
        """
        # Create user-item matrix (users x food-alcohol pairs)
        user_ids = sorted(set(r[0] for r in ratings_data))
        pair_ids = sorted(set((r[1], r[2]) for r in ratings_data))
        
        self.user_id_map = {uid: i for i, uid in enumerate(user_ids)}
        self.pair_id_map = {pair: i for i, pair in enumerate(pair_ids)}
        self.reverse_pair_map = {i: pair for pair, i in self.pair_id_map.items()}
        
        # Initialize matrix
        n_users = len(user_ids)
        n_pairs = len(pair_ids)
        self.user_item_matrix = np.zeros((n_users, n_pairs))
        
        # Fill matrix with ratings
        for user_id, food_id, alcohol_id, rating in ratings_data:
            user_idx = self.user_id_map[user_id]
            pair_idx = self.pair_id_map.get((food_id, alcohol_id))
            if pair_idx is not None:
                self.user_item_matrix[user_idx, pair_idx] = rating
        
        # Calculate similarities
        self._calculate_similarities()
        self.fitted = True
    
    def _calculate_similarities(self):
        """Calculate user and item similarities using cosine similarity"""
        # User similarities (user-user)
        self.user_similarities = cosine_similarity(self.user_item_matrix)
        
        # Item similarities (item-item)
        self.item_similarities = cosine_similarity(self.user_item_matrix.T)
    
    def predict_user_rating(self, user_id: int, food_id: int, alcohol_id: int, k: int = 5) -> float:
        """
        Predict rating for a specific user-food-alcohol combination
        Args:
            user_id: User ID
            food_id: Food ID
            alcohol_id: Alcohol ID
            k: Number of similar users to consider
        Returns:
            Predicted rating (1-5 scale)
        """
        if not self.fitted:
            return 3.0  # Default rating
        
        user_idx = self.user_id_map.get(user_id)
        pair_idx = self.pair_id_map.get((food_id, alcohol_id))
        
        if user_idx is None or pair_idx is None:
            return 3.0  # Default rating for new users/items
        
        # Get k most similar users
        user_sims = self.user_similarities[user_idx]
        similar_users = np.argsort(user_sims)[-k-1:-1]  # Exclude self
        
        # Calculate weighted average rating
        numerator = 0
        denominator = 0
        
        for similar_user in similar_users:
            sim_score = user_sims[similar_user]
            user_rating = self.user_item_matrix[similar_user, pair_idx]
            
            if user_rating > 0 and sim_score > 0:  # Only consider actual ratings
                numerator += sim_score * user_rating
                denominator += sim_score
        
        if denominator == 0:
            return 3.0  # Default rating
        
        predicted_rating = numerator / denominator
        return max(1.0, min(5.0, predicted_rating))  # Clamp to 1-5 range

class AdvancedFoodAlcoholMatcher:
    """Birden çok ML tekniğini birleştiren gelişmiş AI eşleştirici"""
    
    def __init__(self):
        self.neural_network = None
        self.collaborative_filter = CollaborativeFilter()
        self.tfidf_vectorizer = None
        self.scaler = StandardScaler()
        self.pca = PCA(n_components=10)
        self.flavor_embeddings = {}
        self.trained = False
        
        # Feature extractors
        self.feature_weights = {
            'neural_network': 0.4,
            'collaborative_filtering': 0.3,
            'content_based': 0.2,
            'rule_based': 0.1
        }
    
    def extract_features(self, food_item, alcohol_item, user_profile=None) -> np.ndarray:
        """
        Extract comprehensive features for ML models
        Returns feature vector of fixed size
        """
        features = []
        
        # Food features
        food_vector = food_item.get_compatibility_vector() if hasattr(food_item, 'get_compatibility_vector') else {}
        features.extend([
            food_vector.get('intensity', 0.5),
            food_vector.get('spicy', 0),
            food_vector.get('sweet', 0),
            food_vector.get('salty', 0),
            food_vector.get('sour', 0),
            food_vector.get('bitter', 0),
            food_vector.get('umami', 0),
            food_vector.get('price_level', 2) / 3.0,
            food_vector.get('difficulty', 0.5)
        ])
        
        # Alcohol features
        alcohol_vector = alcohol_item.get_compatibility_vector() if hasattr(alcohol_item, 'get_compatibility_vector') else {}
        features.extend([
            alcohol_vector.get('alcohol_content', 0.3),
            alcohol_vector.get('sweetness', 0.5),
            alcohol_vector.get('acidity', 0.5),
            alcohol_vector.get('tannins', 0.5),
            alcohol_vector.get('body_light', 0),
            alcohol_vector.get('body_medium', 0),
            alcohol_vector.get('body_full', 0),
            alcohol_vector.get('price_level', 2) / 3.0,
            alcohol_vector.get('vintage_quality', 0.5)
        ])
        
        # User features (if available)
        if user_profile and hasattr(user_profile, 'get_preference_vector'):
            user_vector = user_profile.get_preference_vector()
            features.extend([
                user_vector.get('age_normalized', 0.5),
                user_vector.get('spice_tolerance', 0.5),
                user_vector.get('adventurous_level', 0.5),
                user_vector.get('budget_level', 0.6),
                user_vector.get('alcohol_tolerance', 0.6),
                user_vector.get('health_conscious', 0),
                user_vector.get('rating_count', 0)
            ])
        else:
            # Default user features
            features.extend([0.5] * 7)
        
        # Interaction features
        features.append(abs(food_vector.get('intensity', 0.5) - alcohol_vector.get('alcohol_content', 0.3)))  # Intensity match
        features.append(food_vector.get('price_level', 2) / 3.0 * alcohol_vector.get('price_level', 2) / 3.0)  # Price compatibility
        
        return np.array(features)
    
    def train_models(self, training_data: List[Dict]):
        """
        Train all ML models with comprehensive training data
        Args:
            training_data: List of training examples with features and ratings
        """
        logger.info("Starting model training...")
        
        # Prepare data for neural network
        X_features = []
        y_ratings = []
        cf_data = []
        
        for example in training_data:
            features = self.extract_features(
                example.get('food_item'),
                example.get('alcohol_item'),
                example.get('user_profile')
            )
            X_features.append(features)
            y_ratings.append(example.get('rating', 3) / 5.0)  # Normalize to 0-1
            
            # Data for collaborative filtering
            cf_data.append((
                example.get('user_id', 0),
                example.get('food_id', 0),
                example.get('alcohol_id', 0),
                example.get('rating', 3)
            ))
        
        if len(X_features) == 0:
            logger.warning("No training data available. Using default models.")
            return
        
        X_train = np.array(X_features)
        y_train = np.array(y_ratings)
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        
        # Train neural network
        input_size = X_train_scaled.shape[1]
        self.neural_network = NeuralNetworkRecommender(input_size=input_size)
        
        try:
            losses = self.neural_network.train(X_train_scaled, y_train, epochs=100)
            logger.info(f"Neural network trained. Final loss: {losses[-1]:.4f}")
        except Exception as e:
            logger.error(f"Error training neural network: {e}")
        
        # Train collaborative filtering
        try:
            self.collaborative_filter.fit(cf_data)
            logger.info("Collaborative filtering model trained.")
        except Exception as e:
            logger.error(f"Error training collaborative filter: {e}")
        
        # Train content-based features
        self._train_content_features(training_data)
        
        self.trained = True
        logger.info("All models trained successfully.")
    
    def _train_content_features(self, training_data: List[Dict]):
        """Train content-based features using TF-IDF"""
        try:
            # Combine flavor profiles for TF-IDF
            flavor_texts = []
            for example in training_data:
                food_item = example.get('food_item')
                alcohol_item = example.get('alcohol_item')
                
                food_flavors = getattr(food_item, 'flavor_profile', [])
                alcohol_flavors = getattr(alcohol_item, 'flavor_profile', [])
                
                combined_text = ' '.join(food_flavors + alcohol_flavors)
                flavor_texts.append(combined_text)
            
            if flavor_texts:
                self.tfidf_vectorizer = TfidfVectorizer(max_features=50)
                self.tfidf_vectorizer.fit(flavor_texts)
                logger.info("Content-based features trained.")
        
        except Exception as e:
            logger.error(f"Error training content features: {e}")
    
    def predict_compatibility(self, food_item, alcohol_item, user_profile=None) -> Tuple[float, Dict]:
        """
        Predict compatibility score using ensemble of ML models
        Returns:
            Tuple of (compatibility_score, model_scores_dict)
        """
        model_scores = {}
        
        # Extract features
        features = self.extract_features(food_item, alcohol_item, user_profile)
        
        # Neural network prediction
        if self.neural_network and self.neural_network.trained:
            try:
                features_scaled = self.scaler.transform([features])
                nn_score = self.neural_network.predict(features_scaled)[0] * 100
                model_scores['neural_network'] = nn_score
            except Exception as e:
                logger.error(f"Neural network prediction error: {e}")
                model_scores['neural_network'] = 60.0
        else:
            model_scores['neural_network'] = 60.0
        
        # Collaborative filtering prediction
        if user_profile and hasattr(user_profile, 'user_id'):
            try:
                cf_score = self.collaborative_filter.predict_user_rating(
                    user_profile.user_id,
                    getattr(food_item, 'id', 0),
                    getattr(alcohol_item, 'id', 0)
                ) * 20  # Convert to 0-100 scale
                model_scores['collaborative_filtering'] = cf_score
            except Exception as e:
                logger.error(f"Collaborative filtering error: {e}")
                model_scores['collaborative_filtering'] = 60.0
        else:
            model_scores['collaborative_filtering'] = 60.0
        
        # Content-based prediction
        model_scores['content_based'] = self._content_based_score(food_item, alcohol_item)
        
        # Rule-based prediction (original algorithm)
        model_scores['rule_based'] = self._rule_based_score(food_item, alcohol_item, user_profile)
        
        # Ensemble prediction
        final_score = 0
        for model_name, score in model_scores.items():
            weight = self.feature_weights.get(model_name, 0.25)
            final_score += weight * score
        
        return final_score, model_scores
    
    def _content_based_score(self, food_item, alcohol_item) -> float:
        """Calculate content-based similarity score"""
        try:
            if not self.tfidf_vectorizer:
                return 60.0
            
            food_flavors = getattr(food_item, 'flavor_profile', [])
            alcohol_flavors = getattr(alcohol_item, 'flavor_profile', [])
            
            combined_text = ' '.join(food_flavors + alcohol_flavors)
            
            # Transform to TF-IDF vector
            tfidf_vector = self.tfidf_vectorizer.transform([combined_text])
            
            # Calculate some simple compatibility based on feature presence
            feature_score = np.sum(tfidf_vector.toarray()) * 1000  # Scale up
            
            return max(30, min(90, 50 + feature_score))
        
        except Exception as e:
            logger.error(f"Content-based scoring error: {e}")
            return 60.0
    
    def _rule_based_score(self, food_item, alcohol_item, user_profile=None) -> float:
        """Calculate rule-based compatibility score (original algorithm)"""
        # This would contain the original pairing rules from the main system
        # For now, return a simple calculation
        
        try:
            food_intensity = getattr(food_item, 'intensity', 5)
            alcohol_content = getattr(alcohol_item, 'alcohol_content', 12)
            
            # Simple intensity matching
            intensity_diff = abs(food_intensity - (alcohol_content / 2))
            intensity_score = max(0, 100 - (intensity_diff * 10))
            
            # Flavor matching (simplified)
            food_flavors = set(getattr(food_item, 'flavor_profile', []))
            alcohol_flavors = set(getattr(alcohol_item, 'flavor_profile', []))
            
            common_flavors = len(food_flavors & alcohol_flavors)
            flavor_score = common_flavors * 20
            
            # Combine scores
            total_score = (intensity_score * 0.6) + (flavor_score * 0.4)
            
            return max(30, min(95, total_score))
        
        except Exception as e:
            logger.error(f"Rule-based scoring error: {e}")
            return 60.0
    
    def get_recommendations(self, food_item, user_profile=None, alcohol_items=None, top_n=5) -> List[Tuple]:
        """
        Get top N recommendations using ensemble model
        """
        if not alcohol_items:
            return []
        
        recommendations = []
        
        for alcohol_item in alcohol_items:
            compatibility_score, model_scores = self.predict_compatibility(
                food_item, alcohol_item, user_profile
            )
            
            explanation = self._generate_ml_explanation(food_item, alcohol_item, model_scores)
            
            recommendations.append((alcohol_item, compatibility_score, explanation, model_scores))
        
        # Sort by compatibility score
        recommendations.sort(key=lambda x: x[1], reverse=True)
        
        return recommendations[:top_n]
    
    def _generate_ml_explanation(self, food_item, alcohol_item, model_scores) -> str:
        """Generate explanation based on ML model contributions"""
        explanations = []
        
        # Determine dominant model
        dominant_model = max(model_scores.items(), key=lambda x: x[1] * self.feature_weights.get(x[0], 0.25))
        
        if dominant_model[0] == 'neural_network':
            explanations.append("AI neural network suggests strong compatibility")
        elif dominant_model[0] == 'collaborative_filtering':
            explanations.append("Users with similar tastes highly rated this pairing")
        elif dominant_model[0] == 'content_based':
            explanations.append("Flavor profiles show excellent harmony")
        else:
            explanations.append("Traditional pairing rules support this match")
        
        # Add specific insights
        food_flavors = getattr(food_item, 'flavor_profile', [])
        alcohol_flavors = getattr(alcohol_item, 'flavor_profile', [])
        common_flavors = set(food_flavors) & set(alcohol_flavors)
        
        if common_flavors:
            explanations.append(f"Shared {', '.join(list(common_flavors)[:2])} notes")
        
        final_score = sum(score * self.feature_weights.get(model, 0.25) 
                         for model, score in model_scores.items())
        
        if final_score >= 85:
            quality = "Exceptional"
        elif final_score >= 75:
            quality = "Excellent"
        elif final_score >= 65:
            quality = "Very Good"
        else:
            quality = "Good"
        
        return f"{quality} ML prediction: {'. '.join(explanations[:2])}"
    
    def save_models(self, filepath: str):
        """Save trained models to disk"""
        try:
            models_data = {
                'neural_network': {
                    'W1': self.neural_network.W1.tolist() if self.neural_network else None,
                    'b1': self.neural_network.b1.tolist() if self.neural_network else None,
                    'W2': self.neural_network.W2.tolist() if self.neural_network else None,
                    'b2': self.neural_network.b2.tolist() if self.neural_network else None,
                    'W3': self.neural_network.W3.tolist() if self.neural_network else None,
                    'b3': self.neural_network.b3.tolist() if self.neural_network else None,
                    'trained': self.neural_network.trained if self.neural_network else False
                },
                'feature_weights': self.feature_weights,
                'trained': self.trained
            }
            
            with open(filepath, 'w') as f:
                json.dump(models_data, f)
            
            # Save sklearn models separately
            if self.scaler:
                with open(filepath.replace('.json', '_scaler.pkl'), 'wb') as f:
                    pickle.dump(self.scaler, f)
            
            if self.tfidf_vectorizer:
                with open(filepath.replace('.json', '_tfidf.pkl'), 'wb') as f:
                    pickle.dump(self.tfidf_vectorizer, f)
            
            logger.info(f"Models saved to {filepath}")
            
        except Exception as e:
            logger.error(f"Error saving models: {e}")
    
    def load_models(self, filepath: str):
        """Eğitilmiş modelleri diskten yükle"""
        try:
            with open(filepath, 'r') as f:
                models_data = json.load(f)
            
            # Restore neural network
            nn_data = models_data.get('neural_network', {})
            if nn_data.get('trained') and nn_data.get('W1'):
                W1 = np.array(nn_data['W1'])
                input_size, hidden_size = W1.shape
                self.neural_network = NeuralNetworkRecommender(input_size, hidden_size)
                
                self.neural_network.W1 = np.array(nn_data['W1'])
                self.neural_network.b1 = np.array(nn_data['b1'])
                self.neural_network.W2 = np.array(nn_data['W2'])
                self.neural_network.b2 = np.array(nn_data['b2'])
                self.neural_network.W3 = np.array(nn_data['W3'])
                self.neural_network.b3 = np.array(nn_data['b3'])
                self.neural_network.trained = nn_data['trained']
            
            self.feature_weights = models_data.get('feature_weights', self.feature_weights)
            self.trained = models_data.get('trained', False)
            
            # Load sklearn models
            try:
                with open(filepath.replace('.json', '_scaler.pkl'), 'rb') as f:
                    self.scaler = pickle.load(f)
            except:
                pass
            
            try:
                with open(filepath.replace('.json', '_tfidf.pkl'), 'rb') as f:
                    self.tfidf_vectorizer = pickle.load(f)
            except:
                pass
            
            logger.info(f"Models loaded from {filepath}")
            
        except Exception as e:
            logger.error(f"Error loading models: {e}")

# Example usage and testing
if __name__ == "__main__":
    # This section can be used for testing the ML components
    matcher = AdvancedFoodAlcoholMatcher()
    logger.info("Advanced ML matcher initialized successfully!")
