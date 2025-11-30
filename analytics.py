"""
Analitik ve Raporlama Modülü
Kullanıcı davranışları ve eşleştirme eğilimlerini anlamaya yönelik gelişmiş analizler
"""

import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
from typing import Dict, List, Tuple, Optional
import json
import logging

logger = logging.getLogger(__name__)

class AnalyticsEngine:
    """Yemek-alkol eşleştirme sistemi için gelişmiş analitik motoru"""
    
    def __init__(self, db_path: str = "food_alcohol_system.db"):
        self.db_path = db_path
        self.conn = None
    
    def get_connection(self):
        """Veritabanı bağlantısını al"""
        if not self.conn:
            self.conn = sqlite3.connect(self.db_path)
        return self.conn
    
    def get_user_statistics(self) -> Dict:
        """Kapsamlı kullanıcı istatistiklerini al"""
        conn = self.get_connection()
        
        stats = {}
        
        try:
            # Basic user stats
            stats['total_users'] = pd.read_sql_query(
                "SELECT COUNT(*) as count FROM users", conn
            )['count'].iloc[0]
            
            # User demographics
            stats['age_distribution'] = pd.read_sql_query(
                "SELECT age, COUNT(*) as count FROM users GROUP BY age ORDER BY age", conn
            )
            
            # Alcohol tolerance distribution
            stats['tolerance_distribution'] = pd.read_sql_query(
                "SELECT alcohol_tolerance, COUNT(*) as count FROM users GROUP BY alcohol_tolerance", conn
            )
            
            # Budget preferences
            stats['budget_distribution'] = pd.read_sql_query(
                "SELECT budget_preference, COUNT(*) as count FROM users GROUP BY budget_preference", conn
            )
            
            # Active users (users who rated in last 30 days)
            stats['active_users_30d'] = pd.read_sql_query("""
                SELECT COUNT(DISTINCT user_id) as count 
                FROM pairings 
                WHERE created_at >= datetime('now', '-30 days')
            """, conn)['count'].iloc[0]
            
        except Exception as e:
            logger.error(f"Error getting user statistics: {e}")
            stats = {'error': str(e)}
        
        return stats
    
    def get_pairing_analytics(self) -> Dict:
        """Detaylı eşleştirme analitiklerini al"""
        conn = self.get_connection()
        
        analytics = {}
        
        try:
            # Total pairings
            analytics['total_pairings'] = pd.read_sql_query(
                "SELECT COUNT(*) as count FROM pairings", conn
            )['count'].iloc[0]
            
            # Average rating
            analytics['average_rating'] = pd.read_sql_query(
                "SELECT AVG(rating) as avg_rating FROM pairings", conn
            )['avg_rating'].iloc[0]
            
            # Rating distribution
            analytics['rating_distribution'] = pd.read_sql_query(
                "SELECT rating, COUNT(*) as count FROM pairings GROUP BY rating ORDER BY rating", conn
            )
            
            # Most popular foods
            analytics['popular_foods'] = pd.read_sql_query("""
                SELECT f.name, COUNT(*) as pairing_count, AVG(p.rating) as avg_rating
                FROM pairings p
                JOIN foods f ON p.food_id = f.id
                GROUP BY f.id, f.name
                ORDER BY pairing_count DESC
                LIMIT 10
            """, conn)
            
            # Most popular alcohols
            analytics['popular_alcohols'] = pd.read_sql_query("""
                SELECT a.name, a.type, COUNT(*) as pairing_count, AVG(p.rating) as avg_rating
                FROM pairings p
                JOIN alcohols a ON p.alcohol_id = a.id
                GROUP BY a.id, a.name, a.type
                ORDER BY pairing_count DESC
                LIMIT 10
            """, conn)
            
            # Pairing trends over time
            analytics['pairing_trends'] = pd.read_sql_query("""
                SELECT DATE(created_at) as date, COUNT(*) as daily_pairings
                FROM pairings
                WHERE created_at >= datetime('now', '-30 days')
                GROUP BY DATE(created_at)
                ORDER BY date
            """, conn)
            
            # Highest rated pairings
            analytics['top_rated_pairings'] = pd.read_sql_query("""
                SELECT f.name as food_name, a.name as alcohol_name, 
                       AVG(p.rating) as avg_rating, COUNT(*) as rating_count
                FROM pairings p
                JOIN foods f ON p.food_id = f.id
                JOIN alcohols a ON p.alcohol_id = a.id
                GROUP BY p.food_id, p.alcohol_id, f.name, a.name
                HAVING COUNT(*) >= 2
                ORDER BY avg_rating DESC, rating_count DESC
                LIMIT 10
            """, conn)
            
        except Exception as e:
            logger.error(f"Error getting pairing analytics: {e}")
            analytics = {'error': str(e)}
        
        return analytics
    
    def get_cuisine_analytics(self) -> Dict:
        """Get cuisine-specific analytics"""
        conn = self.get_connection()
        
        cuisine_stats = {}
        
        try:
            # Popular cuisines
            cuisine_stats['popular_cuisines'] = pd.read_sql_query("""
                SELECT f.cuisine_type, COUNT(*) as pairing_count, AVG(p.rating) as avg_rating
                FROM pairings p
                JOIN foods f ON p.food_id = f.id
                GROUP BY f.cuisine_type
                ORDER BY pairing_count DESC
            """, conn)
            
            # Alcohol preferences by cuisine
            cuisine_stats['alcohol_by_cuisine'] = pd.read_sql_query("""
                SELECT f.cuisine_type, a.type as alcohol_type, 
                       COUNT(*) as pairing_count, AVG(p.rating) as avg_rating
                FROM pairings p
                JOIN foods f ON p.food_id = f.id
                JOIN alcohols a ON p.alcohol_id = a.id
                GROUP BY f.cuisine_type, a.type
                ORDER BY f.cuisine_type, pairing_count DESC
            """, conn)
            
        except Exception as e:
            logger.error(f"Error getting cuisine analytics: {e}")
            cuisine_stats = {'error': str(e)}
        
        return cuisine_stats
    
    def generate_user_report(self, user_id: int) -> Dict:
        """Generate personalized report for a specific user"""
        conn = self.get_connection()
        
        report = {}
        
        try:
            # User basic info
            user_info = pd.read_sql_query("""
                SELECT name, age, alcohol_tolerance, budget_preference, created_at
                FROM users WHERE user_id = ?
            """, conn, params=(user_id,))
            
            if user_info.empty:
                return {'error': 'User not found'}
            
            report['user_info'] = user_info.iloc[0].to_dict()
            
            # User rating history
            report['rating_history'] = pd.read_sql_query("""
                SELECT f.name as food_name, a.name as alcohol_name, 
                       p.rating, p.created_at
                FROM pairings p
                JOIN foods f ON p.food_id = f.id
                JOIN alcohols a ON p.alcohol_id = a.id
                WHERE p.user_id = ?
                ORDER BY p.created_at DESC
            """, conn, params=(user_id,))
            
            # User preferences analysis
            report['preference_analysis'] = pd.read_sql_query("""
                SELECT f.cuisine_type, a.type as alcohol_type,
                       COUNT(*) as pairing_count, AVG(p.rating) as avg_rating
                FROM pairings p
                JOIN foods f ON p.food_id = f.id
                JOIN alcohols a ON p.alcohol_id = a.id
                WHERE p.user_id = ?
                GROUP BY f.cuisine_type, a.type
                ORDER BY avg_rating DESC, pairing_count DESC
            """, conn, params=(user_id,))
            
            # User statistics
            total_ratings = len(report['rating_history'])
            if total_ratings > 0:
                avg_rating = report['rating_history']['rating'].mean()
                report['user_stats'] = {
                    'total_ratings': total_ratings,
                    'average_rating_given': round(avg_rating, 2),
                    'favorite_cuisine': report['preference_analysis'].iloc[0]['cuisine_type'] if not report['preference_analysis'].empty else 'N/A',
                    'preferred_alcohol_type': report['preference_analysis'].iloc[0]['alcohol_type'] if not report['preference_analysis'].empty else 'N/A'
                }
            else:
                report['user_stats'] = {
                    'total_ratings': 0,
                    'average_rating_given': 0,
                    'favorite_cuisine': 'N/A',
                    'preferred_alcohol_type': 'N/A'
                }
            
        except Exception as e:
            logger.error(f"Error generating user report: {e}")
            report = {'error': str(e)}
        
        return report
    
    def create_visualizations(self, save_path: str = "analytics_charts/") -> Dict:
        """Create comprehensive visualizations"""
        import os
        os.makedirs(save_path, exist_ok=True)
        
        charts = {}
        
        try:
            # Get data
            user_stats = self.get_user_statistics()
            pairing_analytics = self.get_pairing_analytics()
            cuisine_analytics = self.get_cuisine_analytics()
            
            # 1. User Age Distribution
            if 'age_distribution' in user_stats and not user_stats['age_distribution'].empty:
                plt.figure(figsize=(10, 6))
                age_data = user_stats['age_distribution']
                plt.hist(age_data['age'], weights=age_data['count'], bins=15, alpha=0.7, color='skyblue')
                plt.title('User Age Distribution')
                plt.xlabel('Age')
                plt.ylabel('Number of Users')
                plt.grid(True, alpha=0.3)
                plt.savefig(f"{save_path}age_distribution.png")
                plt.close()
                charts['age_distribution'] = f"{save_path}age_distribution.png"
            
            # 2. Rating Distribution
            if 'rating_distribution' in pairing_analytics:
                plt.figure(figsize=(8, 6))
                rating_data = pairing_analytics['rating_distribution']
                bars = plt.bar(rating_data['rating'], rating_data['count'], color='lightcoral')
                plt.title('Rating Distribution')
                plt.xlabel('Rating (1-5 stars)')
                plt.ylabel('Number of Ratings')
                
                # Add value labels on bars
                for bar in bars:
                    height = bar.get_height()
                    plt.text(bar.get_x() + bar.get_width()/2., height,
                           f'{int(height)}', ha='center', va='bottom')
                
                plt.savefig(f"{save_path}rating_distribution.png")
                plt.close()
                charts['rating_distribution'] = f"{save_path}rating_distribution.png"
            
            # 3. Popular Foods
            if 'popular_foods' in pairing_analytics:
                plt.figure(figsize=(12, 8))
                food_data = pairing_analytics['popular_foods'].head(10)
                bars = plt.barh(range(len(food_data)), food_data['pairing_count'])
                plt.yticks(range(len(food_data)), food_data['name'])
                plt.xlabel('Number of Pairings')
                plt.title('Most Popular Foods')
                plt.gca().invert_yaxis()
                
                # Add value labels
                for i, bar in enumerate(bars):
                    width = bar.get_width()
                    plt.text(width + 0.1, bar.get_y() + bar.get_height()/2,
                           f'{int(width)}', ha='left', va='center')
                
                plt.tight_layout()
                plt.savefig(f"{save_path}popular_foods.png")
                plt.close()
                charts['popular_foods'] = f"{save_path}popular_foods.png"
            
            # 4. Cuisine Popularity
            if 'popular_cuisines' in cuisine_analytics:
                plt.figure(figsize=(10, 8))
                cuisine_data = cuisine_analytics['popular_cuisines']
                plt.pie(cuisine_data['pairing_count'], labels=cuisine_data['cuisine_type'], 
                       autopct='%1.1f%%', startangle=90)
                plt.title('Cuisine Popularity')
                plt.axis('equal')
                plt.savefig(f"{save_path}cuisine_popularity.png")
                plt.close()
                charts['cuisine_popularity'] = f"{save_path}cuisine_popularity.png"
            
            # 5. Pairing Trends (if data available)
            if 'pairing_trends' in pairing_analytics and not pairing_analytics['pairing_trends'].empty:
                plt.figure(figsize=(12, 6))
                trend_data = pairing_analytics['pairing_trends']
                trend_data['date'] = pd.to_datetime(trend_data['date'])
                plt.plot(trend_data['date'], trend_data['daily_pairings'], marker='o', linewidth=2)
                plt.title('Daily Pairing Trends (Last 30 Days)')
                plt.xlabel('Date')
                plt.ylabel('Number of Pairings')
                plt.xticks(rotation=45)
                plt.grid(True, alpha=0.3)
                plt.tight_layout()
                plt.savefig(f"{save_path}pairing_trends.png")
                plt.close()
                charts['pairing_trends'] = f"{save_path}pairing_trends.png"
            
        except Exception as e:
            logger.error(f"Error creating visualizations: {e}")
            charts['error'] = str(e)
        
        return charts
    
    def generate_business_report(self) -> Dict:
        """Generate comprehensive business intelligence report"""
        report = {
            'generated_at': datetime.now().isoformat(),
            'user_statistics': self.get_user_statistics(),
            'pairing_analytics': self.get_pairing_analytics(),
            'cuisine_analytics': self.get_cuisine_analytics(),
        }
        
        # Add insights and recommendations
        report['insights'] = self._generate_insights(report)
        
        return report
    
    def _generate_insights(self, report_data: Dict) -> List[str]:
        """Generate business insights from analytics data"""
        insights = []
        
        try:
            user_stats = report_data.get('user_statistics', {})
            pairing_analytics = report_data.get('pairing_analytics', {})
            cuisine_analytics = report_data.get('cuisine_analytics', {})
            
            # User insights
            total_users = user_stats.get('total_users', 0)
            active_users = user_stats.get('active_users_30d', 0)
            
            if total_users > 0:
                activity_rate = (active_users / total_users) * 100
                insights.append(f"User Activity: {activity_rate:.1f}% of users are active (rated in last 30 days)")
            
            # Rating insights
            avg_rating = pairing_analytics.get('average_rating', 0)
            if avg_rating:
                insights.append(f"Quality Score: Average rating is {avg_rating:.2f}/5.0 - {'Excellent' if avg_rating >= 4.5 else 'Good' if avg_rating >= 4.0 else 'Average'}")
            
            # Popular cuisine insights
            popular_cuisines = cuisine_analytics.get('popular_cuisines')
            if popular_cuisines is not None and not popular_cuisines.empty:
                top_cuisine = popular_cuisines.iloc[0]
                insights.append(f"Top Cuisine: {top_cuisine['cuisine_type']} leads with {top_cuisine['pairing_count']} pairings")
            
            # Growth recommendations
            if total_users < 100:
                insights.append("Growth Opportunity: Consider marketing campaigns to increase user base")
            
            if activity_rate < 50:
                insights.append("Engagement Opportunity: Implement user retention strategies")
            
        except Exception as e:
            logger.error(f"Error generating insights: {e}")
            insights.append(f"Error generating insights: {str(e)}")
        
        return insights
    
    def export_data_to_csv(self, export_path: str = "exports/") -> Dict:
        """Export all analytics data to CSV files"""
        import os
        os.makedirs(export_path, exist_ok=True)
        
        exported_files = {}
        
        try:
            conn = self.get_connection()
            
            # Export users data
            users_df = pd.read_sql_query("SELECT * FROM users", conn)
            users_file = f"{export_path}users_export.csv"
            users_df.to_csv(users_file, index=False)
            exported_files['users'] = users_file
            
            # Export pairings data
            pairings_df = pd.read_sql_query("""
                SELECT p.*, f.name as food_name, f.cuisine_type,
                       a.name as alcohol_name, a.type as alcohol_type
                FROM pairings p
                JOIN foods f ON p.food_id = f.id
                JOIN alcohols a ON p.alcohol_id = a.id
            """, conn)
            pairings_file = f"{export_path}pairings_export.csv"
            pairings_df.to_csv(pairings_file, index=False)
            exported_files['pairings'] = pairings_file
            
            # Export foods data
            foods_df = pd.read_sql_query("SELECT * FROM foods", conn)
            foods_file = f"{export_path}foods_export.csv"
            foods_df.to_csv(foods_file, index=False)
            exported_files['foods'] = foods_file
            
            # Export alcohols data
            alcohols_df = pd.read_sql_query("SELECT * FROM alcohols", conn)
            alcohols_file = f"{export_path}alcohols_export.csv"
            alcohols_df.to_csv(alcohols_file, index=False)
            exported_files['alcohols'] = alcohols_file
            
        except Exception as e:
            logger.error(f"Error exporting data: {e}")
            exported_files['error'] = str(e)
        
        return exported_files
    
    def close_connection(self):
        """Veritabanı bağlantısını kapat"""
        if self.conn:
            self.conn.close()
            self.conn = None

# Analitik için CLI arayüzü
def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="NeYenir için Analitik Motoru")
    parser.add_argument('--report', choices=['business', 'user'], help='Rapor oluştur (business veya user)')
    parser.add_argument('--user-id', type=int, help='Kullanıcı raporu için kullanıcı ID')
    parser.add_argument('--charts', action='store_true', help='Görselleştirme grafikleri oluştur')
    parser.add_argument('--export', action='store_true', help='Verileri CSV formatında dışa aktar')
    
    args = parser.parse_args()
    
    analytics = AnalyticsEngine()
    
    if args.report == 'business':
        report = analytics.generate_business_report()
        print(json.dumps(report, indent=2, default=str))
    
    elif args.report == 'user' and args.user_id:
        report = analytics.generate_user_report(args.user_id)
        print(json.dumps(report, indent=2, default=str))
    
    elif args.charts:
        charts = analytics.create_visualizations()
        print("Charts generated:", charts)
    
    elif args.export:
        exported = analytics.export_data_to_csv()
        print("Data exported:", exported)
    
    else:
        print("NeYenir Analitik Motoru")
        print("Kullanılabilir seçenekler için --help kullanın")

if __name__ == "__main__":
    main()
