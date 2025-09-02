"""
Ne Yenir? - AI Destekli Yemek & Alkol Eşleştirme Sistemi
========================================================
Yapay zeka ve gurme uzmanları ile gelişmiş yemek-alkol öneri sistemi
Author: Ne Yenir? Ekibi
Version: 2.0
"""

import json
import random
import sqlite3
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import numpy as np
from dataclasses import dataclass, asdict
import pickle
import os

@dataclass
class Food:
    """Food item with detailed characteristics"""
    id: int
    name: str
    cuisine_type: str
    flavor_profile: List[str]  # sweet, salty, sour, bitter, umami, spicy
    intensity: int  # 1-10 scale
    texture: str  # creamy, crispy, tender, chewy
    cooking_method: str
    main_ingredients: List[str]
    dietary_tags: List[str]  # vegetarian, vegan, gluten-free, etc.
    price_range: str  # budget, mid-range, premium
    serving_temp: str  # hot, cold, room-temp

@dataclass 
class Alcohol:
    """Alcohol beverage with detailed characteristics"""
    id: int
    name: str
    type: str  # wine, beer, spirits, cocktail
    subtype: str  # red wine, IPA, whiskey, etc.
    alcohol_content: float
    flavor_profile: List[str]
    body: str  # light, medium, full
    sweetness: int  # 1-10 scale
    acidity: int  # 1-10 scale
    tannins: int  # 1-10 scale (for wines)
    price_range: str
    region: str
    vintage: Optional[int]

@dataclass
class UserProfile:
    """User preferences and history"""
    user_id: int
    name: str
    age: int
    alcohol_tolerance: str  # low, medium, high
    preferred_flavors: List[str]
    dietary_restrictions: List[str]
    budget_preference: str
    favorite_cuisines: List[str]
    disliked_alcohols: List[str]
    previous_pairings: List[Tuple[int, int, int]]  # food_id, alcohol_id, rating

@dataclass
class GourmetExpert:
    """Famous gourmet expert with their specialities"""
    name: str
    country: str
    speciality: List[str]
    bio: str
    michelin_stars: int
    famous_for: List[str]

class GourmetRecommendationSystem:
    """System for gourmet expert recommendations"""
    
    def __init__(self):
        self.experts = self._load_gourmet_experts()
        self.expert_pairings = self._load_expert_pairings()
    
    def _load_gourmet_experts(self) -> List[GourmetExpert]:
        """Load famous gourmet experts from around the world"""
        experts = [
            # Dünya çapında ünlü gurmeler
            GourmetExpert("Gordon Ramsay", "İngiltere", ["Modern European", "Steakhouse"], 
                         "16 Michelin yıldızlı dünyaca ünlü şef", 16, 
                         ["Hell's Kitchen", "MasterChef", "Beef Wellington"]),
            
            GourmetExpert("Joël Robuchon", "Fransa", ["French Fine Dining", "Molecular Gastronomy"], 
                         "32 Michelin yıldızı ile en çok yıldız sahibi şef", 32, 
                         ["Atelier restaurants", "French technique"]),
            
            GourmetExpert("Massimo Bottura", "İtalya", ["Italian", "Contemporary"], 
                         "Osteria Francescana'nın sahibi, dünyanın en iyi restoranı", 3, 
                         ["Tortellini", "Parmigiano Reggiano", "Traditional Italian"]),
            
            GourmetExpert("Jiro Ono", "Japonya", ["Sushi", "Japanese"], 
                         "Dünyanın en ünlü sushi şefi, Sukiyabashi Jiro sahibi", 3, 
                         ["Perfect sushi", "Omakase", "Traditional techniques"]),
            
            GourmetExpert("Daniel Boulud", "Fransa/ABD", ["French-American", "Fine Dining"], 
                         "New York'un en prestijli şeflerinden", 2, 
                         ["Daniel restaurant", "French-American cuisine"]),
            
            # Türk gurmeler
            GourmetExpert("Mehmet Gürs", "Türkiye", ["Modern Turkish", "Fusion"], 
                         "Mikla restaurant sahibi, modern Türk mutfağının öncüsü", 0, 
                         ["Modern Turkish", "Anatolian ingredients", "Istanbul cuisine"]),
            
            GourmetExpert("Maksut Aşkar", "Türkiye", ["Turkish", "Mediterranean"], 
                         "Neolokal restaurant sahibi, yerel malzeme uzmanı", 0, 
                         ["Local ingredients", "Turkish herbs", "Anatolian cuisine"]),
            
            GourmetExpert("Vedat Milor", "Türkiye", ["Food Critic", "Turkish Cuisine"], 
                         "Türkiye'nin en tanınmış yemek eleştirmeni", 0, 
                         ["Food criticism", "Turkish restaurants", "Culinary journalism"]),
            
            GourmetExpert("Somer Sivrioğlu", "Türkiye/Avustralya", ["Turkish", "Modern Australian"], 
                         "Efendy ve Anason restaurant sahibi", 0, 
                         ["Turkish-Australian fusion", "Meze culture", "Modern Turkish"]),
        ]
        return experts
    
    def _load_expert_pairings(self) -> Dict:
        """Load expert pairing recommendations"""
        return {
            "Adana Kebab": [
                ("Gordon Ramsay", "🍷 Zinfandel", "Baharatlı etin yoğunluğu ile mükemmel uyum", 95),
                ("Mehmet Gürs", "🥃 Rakı", "Geleneksel Türk içeceği, kebap ile klasik ikili", 98),
                ("Vedat Milor", "🍺 IPA Beer", "Baharatların keskinliğini dengeler", 88)
            ],
            "İskender Kebab": [
                ("Maksut Aşkar", "🍷 Kalecik Karası", "Türk şarabı ile mükemmel bölgesel uyum", 94),
                ("Mehmet Gürs", "🥃 Rakı", "Yoğurt sosuyla birlikte klasik Turkish pairing", 96),
                ("Somer Sivrioğlu", "🍺 Red Ale", "Et ve domates sosuna uygun", 90)
            ],
            "Manti": [
                ("Vedat Milor", "🍷 Riesling", "Yoğurt sosuna mükemmel asidite", 92),
                ("Mehmet Gürs", "🥃 Rakı", "Türk mantısı ile geleneksel içecek", 95),
                ("Maksut Aşkar", "🍺 Wheat Beer", "Hamur işine uygun hafif bira", 87)
            ],
            "Beef Wellington": [
                ("Gordon Ramsay", "🍷 Cabernet Sauvignon", "Signature yemeğim için favori şarabım", 98),
                ("Joël Robuchon", "🍷 Bordeaux", "Klasik Fransız eşleştirmesi", 96),
                ("Daniel Boulud", "🥃 Cognac", "Et yoğunluğu ile mükemmel", 93)
            ],
            "Sushi Omakase": [
                ("Jiro Ono", "🍶 Junmai Sake", "Geleneksel sushi eşleştirmesi, balık lezzetini öne çıkarır", 99),
                ("Joël Robuchon", "🍾 Champagne", "Taze balık ile mükemmel asidite", 95),
                ("Gordon Ramsay", "🍷 Sancerre", "Mineral ve taze, sushi ile uyumlu", 92)
            ],
            "Coq au Vin": [
                ("Joël Robuchon", "🍷 Burgundy Pinot Noir", "Geleneksel Fransız eşleştirmesi", 97),
                ("Daniel Boulud", "🍷 Côtes du Rhône", "Şarap soslu yemekler için ideal", 94),
                ("Gordon Ramsay", "🍷 Chardonnay", "Kremsi sosla mükemmel uyum", 91)
            ],
            "Margherita Pizza": [
                ("Massimo Bottura", "🍷 Chianti Classico", "Geleneksel İtalyan eşleştirmesi", 95),
                ("Joël Robuchon", "🍷 Barbera", "Domates ve fesleğen ile uyumlu", 90),
                ("Gordon Ramsay", "🍺 Italian Lager", "Pizza ile klasik kombinasyon", 87)
            ],
            "Chocolate Lava Cake": [
                ("Gordon Ramsay", "🍷 Port Wine", "Çikolata ile mükemmel tatlı eşleştirmesi", 96),
                ("Joël Robuchon", "🥃 Cognac", "Zengin çikolata için ideal", 94),
                ("Daniel Boulud", "🍾 Moscato", "Tatlılık dengesi", 89)
            ],
            "Grilled Salmon": [
                ("Gordon Ramsay", "🍷 Pinot Noir", "Somon ile klasik eşleştirme", 94),
                ("Jiro Ono", "🍶 Sake", "Balık ile geleneksel Japon içeceği", 92),
                ("Daniel Boulud", "🍷 Chardonnay", "Izgara balık için mükemmel", 90)
            ],
            "Oysters": [
                ("Joël Robuchon", "🍾 Chablis", "İstiridye ile klasik Fransız eşleştirmesi", 98),
                ("Gordon Ramsay", "🍾 Champagne", "Deniz ürünleri için mükemmel", 95),
                ("Daniel Boulud", "🍷 Muscadet", "Mineral ve taze", 92)
            ],
            "Mushroom Risotto": [
                ("Massimo Bottura", "🍷 Barolo", "İtalyan mantarı ile mükemmel", 96),
                ("Joël Robuchon", "🍷 White Burgundy", "Kremalı risotto için ideal", 93),
                ("Gordon Ramsay", "🍷 Pinot Grigio", "Hafif ve uyumlu", 88)
            ],
            "Caesar Salad": [
                ("Gordon Ramsay", "🍷 Sauvignon Blanc", "Taze salata için ideal asidite", 90),
                ("Daniel Boulud", "🍾 Pinot Grigio", "Hafif ve ferahlatıcı", 87),
                ("Joël Robuchon", "🍺 Wheat Beer", "Salata ile hafif içecek", 85)
            ],
            "Lahmacun": [
                ("Mehmet Gürs", "🥃 Rakı", "Türk pizza ile geleneksel içecek", 96),
                ("Vedat Milor", "🍷 Grenache", "Baharatlı ete uygun", 91),
                ("Maksut Aşkar", "🍺 Turkish Beer", "Yerel lezzet ile yerel içecek", 89)
            ],
            "Baklava": [
                ("Mehmet Gürs", "☕ Turkish Coffee", "Geleneksel Türk tatlısı ile türk kahvesi", 97),
                ("Vedat Milor", "🥃 Rakı", "Tatlı sonrası geleneksel", 93),
                ("Somer Sivrioğlu", "🍷 Moscato", "Bal tatlısı ile uyumlu", 90)
            ]
        }
    
    def get_expert_recommendations(self, food_name: str, top_n: int = 3) -> List[Tuple]:
        """Get expert recommendations for a food item"""
        if food_name not in self.expert_pairings:
            return []
        
        expert_recs = self.expert_pairings[food_name]
        return expert_recs[:top_n]
    
    def get_expert_info(self, expert_name: str) -> GourmetExpert:
        """Get information about a specific expert"""
        for expert in self.experts:
            if expert.name == expert_name:
                return expert
        return None

class AIFoodAlcoholMatcher:
    """Advanced AI system for food-alcohol pairing"""
    
    def __init__(self):
        self.foods = self._load_food_database()
        self.alcohols = self._load_alcohol_database()
        self.pairing_rules = self._load_pairing_rules()
        self.user_profiles = {}
        self.pairing_history = []
        self.ml_model = None
        self.gourmet_system = GourmetRecommendationSystem()  # Gurme sistem entegrasyonu
        self._initialize_database()
        self._train_model()
    
    def _load_food_database(self) -> List[Food]:
        """Load comprehensive food database"""
        foods = [
            # Turkish Cuisine
            Food(1, "Adana Kebab", "Turkish", ["spicy", "smoky", "salty"], 8, "tender", "grilled", 
                 ["lamb", "spices"], [], "mid-range", "hot"),
            Food(2, "İskender Kebab", "Turkish", ["savory", "rich", "salty"], 7, "tender", "grilled",
                 ["lamb", "yogurt", "tomato"], [], "mid-range", "hot"),
            Food(3, "Manti", "Turkish", ["savory", "rich"], 6, "tender", "boiled",
                 ["beef", "dough", "yogurt"], [], "mid-range", "hot"),
            Food(4, "Lahmacun", "Turkish", ["spicy", "savory"], 7, "crispy", "baked",
                 ["lamb", "vegetables", "spices"], [], "budget", "hot"),
            Food(5, "Baklava", "Turkish", ["sweet", "rich"], 8, "crispy", "baked",
                 ["phyllo", "nuts", "honey"], ["vegetarian"], "mid-range", "room-temp"),
            
            # International Cuisine
            Food(6, "Beef Wellington", "British", ["rich", "savory", "umami"], 9, "tender", "roasted",
                 ["beef", "mushroom", "pastry"], [], "premium", "hot"),
            Food(7, "Sushi Omakase", "Japanese", ["fresh", "umami", "delicate"], 8, "tender", "raw",
                 ["fish", "rice", "seaweed"], [], "premium", "cold"),
            Food(8, "Coq au Vin", "French", ["rich", "savory", "complex"], 8, "tender", "braised",
                 ["chicken", "wine", "herbs"], [], "premium", "hot"),
            Food(9, "Margherita Pizza", "Italian", ["savory", "rich"], 6, "crispy", "baked",
                 ["tomato", "mozzarella", "basil"], ["vegetarian"], "budget", "hot"),
            Food(10, "Chocolate Lava Cake", "French", ["sweet", "rich"], 9, "creamy", "baked",
                  ["chocolate", "butter", "eggs"], ["vegetarian"], "mid-range", "hot"),
            
            # Seafood
            Food(11, "Grilled Salmon", "International", ["rich", "smoky"], 6, "tender", "grilled",
                 ["salmon", "herbs"], [], "premium", "hot"),
            Food(12, "Oysters", "French", ["briny", "fresh", "mineral"], 7, "tender", "raw",
                 ["oysters"], [], "premium", "cold"),
            
            # Vegetarian Options
            Food(13, "Mushroom Risotto", "Italian", ["rich", "earthy", "creamy"], 7, "creamy", "stirred",
                 ["rice", "mushrooms", "cheese"], ["vegetarian"], "mid-range", "hot"),
            Food(14, "Caesar Salad", "American", ["fresh", "salty", "tangy"], 5, "crispy", "raw",
                 ["lettuce", "cheese", "croutons"], ["vegetarian"], "budget", "cold"),
        ]
        return foods
    
    def _load_alcohol_database(self) -> List[Alcohol]:
        """Load comprehensive alcohol database"""
        alcohols = [
            # Turkish Alcohols
            Alcohol(1, "Rakı", "spirits", "anise", 45.0, ["anise", "herbal"], "full", 1, 2, 0, "mid-range", "Turkey", None),
            Alcohol(2, "Turkish Red Wine (Kalecik Karası)", "wine", "red", 13.5, ["fruity", "earthy"], "medium", 3, 6, 6, "mid-range", "Turkey", 2020),
            
            # Wines
            Alcohol(3, "Cabernet Sauvignon", "wine", "red", 14.0, ["dark fruit", "oak", "tannins"], "full", 2, 5, 8, "premium", "France", 2019),
            Alcohol(4, "Chardonnay", "wine", "white", 13.0, ["citrus", "oak", "butter"], "medium", 4, 7, 2, "premium", "France", 2021),
            Alcohol(5, "Pinot Noir", "wine", "red", 12.5, ["red fruit", "earthy"], "light", 3, 6, 4, "premium", "France", 2020),
            Alcohol(6, "Sauvignon Blanc", "wine", "white", 12.0, ["citrus", "grass", "mineral"], "light", 2, 8, 1, "mid-range", "New Zealand", 2022),
            Alcohol(7, "Champagne", "wine", "sparkling", 12.5, ["citrus", "yeast", "mineral"], "light", 3, 8, 2, "premium", "France", 2018),
            
            # Beers
            Alcohol(8, "IPA", "beer", "ale", 6.5, ["hoppy", "bitter", "citrus"], "medium", 2, 4, 0, "budget", "USA", None),
            Alcohol(9, "Pilsner", "beer", "lager", 4.8, ["crisp", "light", "malty"], "light", 3, 5, 0, "budget", "Czech Republic", None),
            Alcohol(10, "Stout", "beer", "ale", 5.5, ["roasted", "chocolate", "coffee"], "full", 1, 3, 0, "mid-range", "Ireland", None),
            
            # Spirits & Cocktails
            Alcohol(11, "Single Malt Whiskey", "spirits", "whiskey", 40.0, ["smoky", "vanilla", "oak"], "full", 2, 3, 0, "premium", "Scotland", None),
            Alcohol(12, "Gin & Tonic", "cocktail", "gin-based", 8.0, ["juniper", "citrus", "bitter"], "light", 3, 6, 0, "mid-range", "International", None),
            Alcohol(13, "Manhattan", "cocktail", "whiskey-based", 25.0, ["sweet", "bitter", "strong"], "full", 6, 4, 0, "premium", "USA", None),
            Alcohol(14, "Mojito", "cocktail", "rum-based", 10.0, ["mint", "lime", "sweet"], "light", 7, 7, 0, "mid-range", "Cuba", None),
            
            # Sake & Asian Spirits
            Alcohol(15, "Junmai Sake", "sake", "pure rice", 15.5, ["rice", "floral", "clean"], "light", 4, 5, 0, "premium", "Japan", None),
            
            # Dessert Wines
            Alcohol(16, "Port Wine", "wine", "fortified", 20.0, ["sweet", "rich", "dark fruit"], "full", 8, 4, 7, "premium", "Portugal", None),
        ]
        return alcohols
    
    def _load_pairing_rules(self) -> Dict:
        """Load AI pairing rules and weights"""
        return {
            "flavor_matching": {
                "complementary": {
                    ("spicy", "sweet"): 0.9,
                    ("salty", "sweet"): 0.8,
                    ("rich", "acidic"): 0.9,
                    ("smoky", "oak"): 0.8,
                    ("fresh", "citrus"): 0.9,
                },
                "similar": {
                    ("earthy", "earthy"): 0.7,
                    ("fruity", "fruity"): 0.8,
                    ("herbal", "herbal"): 0.7,
                }
            },
            "intensity_matching": 0.8,  # Similar intensities work better
            "texture_alcohol_body": {
                ("creamy", "full"): 0.8,
                ("crispy", "light"): 0.7,
                ("tender", "medium"): 0.8,
            },
            "cuisine_regional": {
                ("Turkish", "Turkey"): 0.9,
                ("French", "France"): 0.9,
                ("Italian", "Italy"): 0.8,
                ("Japanese", "Japan"): 0.9,
            },
            "temperature_matching": {
                ("hot", "room-temp"): 0.8,
                ("cold", "cold"): 0.9,
                ("room-temp", "room-temp"): 0.8,
            }
        }
    
    def _initialize_database(self):
        """Initialize SQLite database for storing user data and history"""
        # Remove the class-level connection, use get_db_connection instead
        conn = self.get_db_connection()
        cursor = conn.cursor()
        
        # Create tables
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                alcohol_tolerance TEXT,
                preferred_flavors TEXT,
                dietary_restrictions TEXT,
                budget_preference TEXT,
                favorite_cuisines TEXT,
                disliked_alcohols TEXT
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS pairings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                food_id INTEGER,
                alcohol_id INTEGER,
                rating INTEGER,
                timestamp TEXT,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def get_db_connection(self):
        """Get a new database connection for each request (thread-safe)"""
        return sqlite3.connect('food_alcohol_system.db', check_same_thread=False)
    
    def _train_model(self):
        """Train a simple ML model for better recommendations"""
        # Simple weighted scoring model
        self.ml_model = {
            'flavor_weights': np.random.random(10),
            'intensity_weight': 0.3,
            'user_preference_weight': 0.4,
            'historical_weight': 0.2,
            'regional_weight': 0.1
        }
    
    def calculate_compatibility_score(self, food: Food, alcohol: Alcohol, user_profile: Optional[UserProfile] = None) -> float:
        """Calculate AI-powered compatibility score between food and alcohol"""
        score = 0.0
        max_score = 0.0
        
        # 1. Flavor Profile Matching
        flavor_score = 0.0
        for food_flavor in food.flavor_profile:
            for alcohol_flavor in alcohol.flavor_profile:
                # Check complementary flavors
                for (f1, f2), weight in self.pairing_rules["flavor_matching"]["complementary"].items():
                    if (food_flavor == f1 and alcohol_flavor == f2) or (food_flavor == f2 and alcohol_flavor == f1):
                        flavor_score += weight
                
                # Check similar flavors
                if food_flavor == alcohol_flavor:
                    flavor_score += self.pairing_rules["flavor_matching"]["similar"].get((food_flavor, alcohol_flavor), 0.5)
        
        score += flavor_score * 0.4
        max_score += 0.4
        
        # 2. Intensity Matching
        intensity_diff = abs(food.intensity - (alcohol.alcohol_content / 5))  # Normalize alcohol content
        intensity_score = max(0, 1 - (intensity_diff / 10)) * self.pairing_rules["intensity_matching"]
        score += intensity_score * 0.2
        max_score += 0.2
        
        # 3. Texture and Body Matching
        texture_body_score = self.pairing_rules["texture_alcohol_body"].get((food.texture, alcohol.body), 0.5)
        score += texture_body_score * 0.15
        max_score += 0.15
        
        # 4. Regional/Cuisine Matching
        regional_score = self.pairing_rules["cuisine_regional"].get((food.cuisine_type, alcohol.region), 0.3)
        score += regional_score * 0.1
        max_score += 0.1
        
        # 5. Temperature Compatibility
        temp_score = self.pairing_rules["temperature_matching"].get((food.serving_temp, "room-temp"), 0.6)
        score += temp_score * 0.05
        max_score += 0.05
        
        # 6. User Profile Matching (if available)
        if user_profile:
            user_score = 0.0
            
            # Preferred flavors
            for pref_flavor in user_profile.preferred_flavors:
                if pref_flavor in alcohol.flavor_profile:
                    user_score += 0.3
            
            # Budget matching
            if user_profile.budget_preference == food.price_range == alcohol.price_range:
                user_score += 0.2
            
            # Dietary restrictions
            dietary_compatible = all(restriction not in food.dietary_tags for restriction in user_profile.dietary_restrictions)
            if not dietary_compatible:
                user_score -= 0.5
            
            # Disliked alcohols
            if alcohol.name in user_profile.disliked_alcohols or alcohol.type in user_profile.disliked_alcohols:
                user_score -= 0.8
            
            score += user_score * 0.1
            max_score += 0.1
        
        # Normalize score to 0-100 scale
        final_score = (score / max_score) * 100 if max_score > 0 else 0
        return min(100, max(0, final_score))
    
    def get_recommendations(self, food_name: str, user_profile: Optional[UserProfile] = None, top_n: int = 5) -> Dict:
        """Get top N alcohol recommendations for a given food with both AI and expert opinions"""
        # Find the food
        food = None
        for f in self.foods:
            if f.name.lower() == food_name.lower():
                food = f
                break
        
        if not food:
            return {"ai_recommendations": [], "expert_recommendations": []}
        
        # AI Recommendations
        ai_recommendations = []
        for alcohol in self.alcohols:
            score = self.calculate_compatibility_score(food, alcohol, user_profile)
            explanation = self._generate_explanation(food, alcohol, score)
            ai_recommendations.append((alcohol, score, explanation))
        
        # Sort AI recommendations by score
        ai_recommendations.sort(key=lambda x: x[1], reverse=True)
        ai_recommendations = ai_recommendations[:top_n]
        
        # Expert Recommendations
        expert_recommendations = self.gourmet_system.get_expert_recommendations(food_name, top_n)
        
        # Format expert recommendations with emoji prefix
        formatted_expert_recs = []
        for expert_name, drink, explanation, score in expert_recommendations:
            expert_info = self.gourmet_system.get_expert_info(expert_name)
            formatted_explanation = f"👨‍🍳 {expert_name}: {explanation}"
            formatted_expert_recs.append((drink, score, formatted_explanation, expert_info))
        
        return {
            "ai_recommendations": ai_recommendations,
            "expert_recommendations": formatted_expert_recs
        }
    
    def _generate_explanation(self, food: Food, alcohol: Alcohol, score: float) -> str:
        """Generate AI explanation for the pairing recommendation"""
        explanations = []
        
        # Flavor explanations - Türkçe lezzet açıklamaları
        flavor_translations = {
            "spicy": "baharatlı", "sweet": "tatlı", "salty": "tuzlu", "sour": "ekşi",
            "bitter": "acı", "umami": "umami", "rich": "zengin", "fresh": "taze",
            "smoky": "dumanlı", "savory": "lezzetli", "acidic": "asitli", "mineral": "mineral",
            "fruity": "meyveli", "floral": "çiçeksi", "earthy": "toprak", "creamy": "kremsi",
            "crispy": "gevrek", "briny": "tuzlu"
        }
        
        common_flavors = set(food.flavor_profile) & set(alcohol.flavor_profile)
        if common_flavors:
            tr_flavors = [flavor_translations.get(f, f) for f in common_flavors]
            explanations.append(f"Ortak {', '.join(tr_flavors)} lezzet notaları")
        
        # Complementary flavors - Tamamlayıcı lezzetler
        complementary_pairs = [
            ("spicy", "sweet"), ("salty", "sweet"), ("rich", "acidic")
        ]
        for food_flavor in food.flavor_profile:
            for alcohol_flavor in alcohol.flavor_profile:
                for pair in complementary_pairs:
                    if (food_flavor, alcohol_flavor) == pair or (alcohol_flavor, food_flavor) == pair:
                        tr_food = flavor_translations.get(food_flavor, food_flavor)
                        tr_alcohol = flavor_translations.get(alcohol_flavor, alcohol_flavor)
                        explanations.append(f"Tamamlayıcı {tr_food}-{tr_alcohol} dengesi")
        
        # Regional matching - Bölgesel uyum
        if food.cuisine_type.lower() == alcohol.region.lower():
            explanations.append(f"Geleneksel {food.cuisine_type} eşleştirmesi")
        
        # Intensity matching - Yoğunluk uyumu
        if abs(food.intensity - (alcohol.alcohol_content / 5)) < 2:
            explanations.append("İyi dengeli yoğunluk seviyeleri")
        
        # Turkish quality descriptions
        if score >= 80:
            quality = "Mükemmel"
        elif score >= 70:
            quality = "Çok İyi"
        elif score >= 60:
            quality = "İyi"
        else:
            quality = "Uygun"
        
        base_explanation = f"🤖 AI: {quality} eşleştirme ({score:.1f}/100)"
        if explanations:
            return f"{base_explanation}: {'. '.join(explanations[:2])}"
        else:
            return base_explanation
    
    def create_user_profile(self, name: str, age: int, preferences: Dict) -> UserProfile:
        """Create a new user profile"""
        user_id = len(self.user_profiles) + 1
        profile = UserProfile(
            user_id=user_id,
            name=name,
            age=age,
            alcohol_tolerance=preferences.get('alcohol_tolerance', 'medium'),
            preferred_flavors=preferences.get('preferred_flavors', []),
            dietary_restrictions=preferences.get('dietary_restrictions', []),
            budget_preference=preferences.get('budget_preference', 'mid-range'),
            favorite_cuisines=preferences.get('favorite_cuisines', []),
            disliked_alcohols=preferences.get('disliked_alcohols', []),
            previous_pairings=[]
        )
        
        self.user_profiles[user_id] = profile
        self._save_user_to_db(profile)
        return profile
    
    def _save_user_to_db(self, profile: UserProfile):
        """Save user profile to database"""
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO users 
            (user_id, name, age, alcohol_tolerance, preferred_flavors, 
             dietary_restrictions, budget_preference, favorite_cuisines, disliked_alcohols)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            profile.user_id, profile.name, profile.age, profile.alcohol_tolerance,
            json.dumps(profile.preferred_flavors), json.dumps(profile.dietary_restrictions),
            profile.budget_preference, json.dumps(profile.favorite_cuisines),
            json.dumps(profile.disliked_alcohols)
        ))
        conn.commit()
        conn.close()
    
    def rate_pairing(self, user_id: int, food_name: str, alcohol_name: str, rating: int):
        """Rate a food-alcohol pairing for learning"""
        food_id = next((f.id for f in self.foods if f.name == food_name), None)
        alcohol_id = next((a.id for a in self.alcohols if a.name == alcohol_name), None)
        
        if food_id and alcohol_id and user_id in self.user_profiles:
            conn = self.get_db_connection()
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO pairings (user_id, food_id, alcohol_id, rating, timestamp)
                VALUES (?, ?, ?, ?, ?)
            ''', (user_id, food_id, alcohol_id, rating, datetime.now().isoformat()))
            conn.commit()
            conn.close()
            
            # Update user profile
            self.user_profiles[user_id].previous_pairings.append((food_id, alcohol_id, rating))
    
    def get_user_history(self, user_id: int) -> List[Dict]:
        """Get user's pairing history"""
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT food_id, alcohol_id, rating, timestamp FROM pairings 
            WHERE user_id = ? ORDER BY timestamp DESC
        ''', (user_id,))
        
        history = []
        for row in cursor.fetchall():
            food_id, alcohol_id, rating, timestamp = row
            food_name = next((f.name for f in self.foods if f.id == food_id), "Unknown")
            alcohol_name = next((a.name for a in self.alcohols if a.id == alcohol_id), "Unknown")
            
            history.append({
                'food': food_name,
                'alcohol': alcohol_name,
                'rating': rating,
                'timestamp': timestamp
            })
        
        conn.close()
        return history
    
    def get_trending_pairings(self, top_n: int = 10) -> List[Dict]:
        """Get trending food-alcohol pairings based on ratings"""
        conn = self.get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT food_id, alcohol_id, AVG(rating) as avg_rating, COUNT(*) as count
            FROM pairings 
            GROUP BY food_id, alcohol_id 
            HAVING count >= 2
            ORDER BY avg_rating DESC, count DESC
            LIMIT ?
        ''', (top_n,))
        
        trending = []
        for row in cursor.fetchall():
            food_id, alcohol_id, avg_rating, count = row
            food_name = next((f.name for f in self.foods if f.id == food_id), "Unknown")
            alcohol_name = next((a.name for a in self.alcohols if a.id == alcohol_id), "Unknown")
            
            trending.append({
                'food': food_name,
                'alcohol': alcohol_name,
                'rating': round(avg_rating, 1),
                'votes': count
            })
        
        conn.close()
        return trending

def main():
    """Ana uygulama arayüzü"""
    print("�️ Ne Yenir? - AI Destekli Yemek & Alkol Eşleştirme �️")
    print("=" * 55)
    
    matcher = AIFoodAlcoholMatcher()
    current_user = None
    
    while True:
        print("\n📋 ANA MENÜ:")
        print("1. 🍽️  Yemek-Alkol Önerilerini Al")
        print("2. 👤 Kullanıcı Profili Oluştur/Giriş Yap") 
        print("3. ⭐ Bir Eşleştirmeyi Puanla")
        print("4. 📊 Geçmişimi Görüntüle")
        print("5. 🔥 Trend Eşleştirmeleri")
        print("6. 🍴 Mevcut Yemekleri İncele")
        print("7. 🍺 Mevcut Alkolleri İncele")
        print("8. 🚪 Çıkış")
        
        choice = input("\nBir seçenek belirleyin (1-8): ").strip()
        
        if choice == "1":
            print("\n🍽️ MEVCUT YEMEKLER:")
            for i, food in enumerate(matcher.foods, 1):
                cuisine_emoji = {"Turkish": "🇹🇷", "French": "🇫🇷", "Italian": "🇮🇹", "Japanese": "🇯🇵", "British": "🇬🇧", "American": "🇺🇸"}.get(food.cuisine_type, "🌍")
                print(f"{i}. {cuisine_emoji} {food.name} ({food.cuisine_type}) - {food.price_range}")
            
            try:
                food_choice = int(input("\nYemek numarası seçin: ")) - 1
                if 0 <= food_choice < len(matcher.foods):
                    selected_food = matcher.foods[food_choice]
                    
                    print(f"\n🔍 {selected_food.name} için öneriler alınıyor...")
                    all_recommendations = matcher.get_recommendations(
                        selected_food.name, 
                        current_user, 
                        top_n=5
                    )
                    
                    ai_recs = all_recommendations["ai_recommendations"]
                    expert_recs = all_recommendations["expert_recommendations"]
                    
                    # AI Önerileri
                    print(f"\n🤖 AI ÖNERİLERİ - {selected_food.name.upper()}:")
                    print("-" * 60)
                    
                    for i, (alcohol, score, explanation) in enumerate(ai_recs, 1):
                        type_emoji = {"wine": "🍷", "beer": "🍺", "spirits": "🥃", "cocktail": "🍸", "sake": "🍶"}.get(alcohol.type, "🥂")
                        print(f"\n{i}. {type_emoji} {alcohol.name}")
                        print(f"   Tür: {alcohol.type.title()} ({alcohol.subtype})")
                        print(f"   Alkol: {alcohol.alcohol_content}%")
                        print(f"   Bölge: {alcohol.region}")
                        print(f"   Fiyat: {alcohol.price_range}")
                        print(f"   {explanation}")
                        print(f"   💯 Uyumluluk Puanı: {score:.1f}/100")
                        
                        # Visual score bar
                        bar_length = 20
                        filled_length = int(score * bar_length // 100)
                        bar = "█" * filled_length + "░" * (bar_length - filled_length)
                        print(f"   [{bar}] {score:.1f}%")
                    
                    # Gurme Uzmanı Önerileri
                    if expert_recs:
                        print(f"\n👨‍🍳 GURME UZMANI ÖNERİLERİ - {selected_food.name.upper()}:")
                        print("-" * 60)
                        
                        for i, (drink, score, explanation, expert_info) in enumerate(expert_recs, 1):
                            print(f"\n{i}. {drink}")
                            print(f"   {explanation}")
                            print(f"   💯 Uzman Puanı: {score}/100")
                            if expert_info:
                                stars = "⭐" * expert_info.michelin_stars if expert_info.michelin_stars > 0 else "🏆"
                                print(f"   🌟 Uzman: {expert_info.name} ({expert_info.country}) {stars}")
                                print(f"   📝 Bio: {expert_info.bio}")
                            
                            # Visual score bar for experts
                            bar_length = 20
                            filled_length = int(score * bar_length // 100)
                            bar = "█" * filled_length + "░" * (bar_length - filled_length)
                            print(f"   [{bar}] {score}%")
                    else:
                        print(f"\n👨‍🍳 Bu yemek için henüz gurme uzmanı önerisi bulunmuyor.")
                
                else:
                    print("❌ Geçersiz yemek seçimi!")
            except ValueError:
                print("❌ Lütfen geçerli bir numara girin!")
        
        elif choice == "2":
            print("\n👤 KULLANICI PROFİLİ KURULUMU:")
            name = input("İsminizi girin: ").strip()
            
            try:
                age = int(input("Yaşınızı girin: "))
                
                print("\nAlkol tolerans seviyesi:")
                print("1. Düşük (1-2 içecek)")
                print("2. Orta (3-4 içecek)")  
                print("3. Yüksek (5+ içecek)")
                tolerance_choice = input("Seçin (1-3): ").strip()
                tolerance_map = {"1": "düşük", "2": "orta", "3": "yüksek"}
                tolerance = tolerance_map.get(tolerance_choice, "orta")
                
                print("\nTercih ettiğiniz lezzetler (birden fazla seçebilir, virgülle ayırın):")
                flavors = ["tatlı", "tuzlu", "ekşi", "acı", "umami", "baharatlı", "dumanlı", "meyveli", "bitkisel"]
                for i, flavor in enumerate(flavors, 1):
                    print(f"{i}. {flavor}")
                
                flavor_input = input("Numaraları girin (örn: 1,3,5): ").strip()
                preferred_flavors = []
                if flavor_input:
                    try:
                        indices = [int(x.strip()) - 1 for x in flavor_input.split(",")]
                        preferred_flavors = [flavors[i] for i in indices if 0 <= i < len(flavors)]
                    except:
                        preferred_flavors = []
                
                print("\nBütçe tercihi:")
                print("1. Ekonomik")
                print("2. Orta seviye") 
                print("3. Premium")
                budget_choice = input("Seçin (1-3): ").strip()
                budget_map = {"1": "budget", "2": "mid-range", "3": "premium"}
                budget = budget_map.get(budget_choice, "mid-range")
                
                preferences = {
                    'alcohol_tolerance': tolerance,
                    'preferred_flavors': preferred_flavors,
                    'budget_preference': budget,
                    'dietary_restrictions': [],
                    'favorite_cuisines': [],
                    'disliked_alcohols': []
                }
                
                current_user = matcher.create_user_profile(name, age, preferences)
                print(f"\n✅ Profil başarıyla oluşturuldu! Hoş geldin, {name}! 🎉")
                
            except ValueError:
                print("❌ Geçersiz giriş! Lütfen tekrar deneyin.")
        
        elif choice == "3":
            if not current_user:
                print("❌ Lütfen önce bir kullanıcı profili oluşturun!")
                continue
                
            print("\n⭐ BİR EŞLEŞTİRMEYİ PUANLA:")
            print("Mevcut yemekler:")
            for i, food in enumerate(matcher.foods[:10], 1):  # Show first 10
                print(f"{i}. {food.name}")
            
            try:
                food_idx = int(input("Yemek numarası seçin: ")) - 1
                if 0 <= food_idx < len(matcher.foods):
                    selected_food = matcher.foods[food_idx].name
                    
                    print("Mevcut alkol seçenekleri:")
                    for i, alcohol in enumerate(matcher.alcohols[:10], 1):  # Show first 10
                        print(f"{i}. {alcohol.name}")
                    
                    alcohol_idx = int(input("Alkol numarası seçin: ")) - 1
                    if 0 <= alcohol_idx < len(matcher.alcohols):
                        selected_alcohol = matcher.alcohols[alcohol_idx].name
                        
                        rating = int(input("Bu eşleştirmeyi puanlayın (1-5 yıldız): "))
                        if 1 <= rating <= 5:
                            matcher.rate_pairing(current_user.user_id, selected_food, selected_alcohol, rating)
                            print(f"✅ Teşekkürler! Puanladığınız: {selected_food} + {selected_alcohol}: {'⭐' * rating}")
                        else:
                            print("❌ Puan 1-5 arası olmalıdır!")
                    else:
                        print("❌ Geçersiz alkol seçimi!")
                else:
                    print("❌ Geçersiz yemek seçimi!")
            except ValueError:
                print("❌ Lütfen geçerli numaralar girin!")
        
        elif choice == "4":
            if not current_user:
                print("❌ Lütfen önce bir kullanıcı profili oluşturun!")
                continue
                
            print(f"\n📊 {current_user.name.upper()} İÇİN EŞLEŞTİRME GEÇMİŞİ:")
            history = matcher.get_user_history(current_user.user_id)
            
            if not history:
                print("Henüz eşleştirme geçmişi yok. Bazı eşleştirmeleri puanlamayı deneyin!")
            else:
                print("-" * 60)
                for entry in history[:10]:  # Show last 10
                    stars = "⭐" * entry['rating']
                    date = datetime.fromisoformat(entry['timestamp']).strftime("%Y-%m-%d %H:%M")
                    print(f"{entry['food']} + {entry['alcohol']}")
                    print(f"   Puan: {stars} ({entry['rating']}/5)")
                    print(f"   Tarih: {date}")
                    print()
        
        elif choice == "5":
            print("\n🔥 TREND EŞLEŞTİRMELER:")
            trending = matcher.get_trending_pairings(10)
            
            if not trending:
                print("Henüz trend eşleştirme bulunmuyor!")
            else:
                print("-" * 60)
                for i, pairing in enumerate(trending, 1):
                    stars = "⭐" * int(pairing['rating'])
                    print(f"{i}. {pairing['food']} + {pairing['alcohol']}")
                    print(f"   Puan: {stars} ({pairing['rating']}/5.0)")
                    print(f"   Oylar: {pairing['votes']} kullanıcı")
                    print()
        
        elif choice == "6":
            print("\n🍴 MEVCUT YEMEKLER:")
            print("-" * 60)
            for food in matcher.foods:
                cuisine_emoji = {"Turkish": "🇹🇷", "French": "🇫🇷", "Italian": "🇮🇹", "Japanese": "🇯🇵", "British": "🇬🇧", "American": "🇺🇸"}.get(food.cuisine_type, "🌍")
                print(f"{cuisine_emoji} {food.name}")
                print(f"   Mutfak: {food.cuisine_type}")
                print(f"   Lezzetler: {', '.join(food.flavor_profile)}")
                print(f"   Yoğunluk: {food.intensity}/10")
                print(f"   Fiyat: {food.price_range}")
                print()
        
        elif choice == "7":
            print("\n🍺 MEVCUT ALKOL SEÇENEKLERİ:")
            print("-" * 60)
            for alcohol in matcher.alcohols:
                type_emoji = {"wine": "🍷", "beer": "🍺", "spirits": "🥃", "cocktail": "🍸", "sake": "🍶"}.get(alcohol.type, "🥂")
                print(f"{type_emoji} {alcohol.name}")
                print(f"   Tür: {alcohol.type.title()} ({alcohol.subtype})")
                print(f"   Alkol: {alcohol.alcohol_content}%")
                print(f"   Lezzetler: {', '.join(alcohol.flavor_profile)}")
                print(f"   Bölge: {alcohol.region}")
                print(f"   Fiyat: {alcohol.price_range}")
                print()
        
        elif choice == "8":
            print("\n👋 Ne Yenir? sistemini kullandığınız için teşekkürler!")
            print("�️ Lezzetli eşleştirmelerinizin tadını çıkarın! 🥂")
            break
        
        else:
            print("❌ Geçersiz seçenek! Lütfen 1-8 arası seçin.")

if __name__ == "__main__":
    main()
