"""
Configuration file for AI Food & Alcohol Pairing System
Contains all configurable parameters and settings
"""

import os
from pathlib import Path

class Config:
    """Main configuration class"""
    
    # Application Settings
    APP_NAME = "AI Food & Alcohol Pairing System"
    VERSION = "2.0.0"
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ai-food-alcohol-pairing-secret-key'
    
    # Database Settings
    DATABASE_PATH = Path(__file__).parent / 'food_alcohol_system.db'
    DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
    
    # AI Algorithm Parameters
    AI_CONFIG = {
        'flavor_matching_weight': 0.4,
        'intensity_matching_weight': 0.2,
        'texture_body_weight': 0.15,
        'regional_matching_weight': 0.1,
        'temperature_weight': 0.05,
        'user_profile_weight': 0.1,
        
        'min_compatibility_score': 30.0,
        'excellent_score_threshold': 80.0,
        'good_score_threshold': 70.0,
        'acceptable_score_threshold': 60.0,
    }
    
    # Flavor Pairing Rules
    FLAVOR_RULES = {
        'complementary_pairs': [
            ('spicy', 'sweet'),
            ('salty', 'sweet'), 
            ('rich', 'acidic'),
            ('smoky', 'oak'),
            ('fresh', 'citrus'),
            ('bitter', 'sweet'),
            ('umami', 'acidic')
        ],
        'similar_pairs': [
            ('earthy', 'earthy'),
            ('fruity', 'fruity'),
            ('herbal', 'herbal'),
            ('nutty', 'nutty'),
            ('floral', 'floral')
        ]
    }
    
    # Regional Cuisine Mappings
    REGIONAL_MAPPINGS = {
        'Turkish': ['Turkey'],
        'French': ['France', 'Champagne'],
        'Italian': ['Italy', 'Tuscany', 'Piedmont'],
        'Japanese': ['Japan'],
        'British': ['England', 'Scotland', 'Ireland'],
        'American': ['USA', 'California', 'Oregon'],
        'International': ['International']
    }
    
    # Price Categories
    PRICE_CATEGORIES = ['budget', 'mid-range', 'premium']
    
    # Alcohol Types and Icons
    ALCOHOL_TYPES = {
        'wine': {'icon': '🍷', 'subcategories': ['red', 'white', 'rosé', 'sparkling', 'fortified']},
        'beer': {'icon': '🍺', 'subcategories': ['ale', 'lager', 'stout', 'pilsner', 'wheat']},
        'spirits': {'icon': '🥃', 'subcategories': ['whiskey', 'gin', 'vodka', 'rum', 'brandy']},
        'cocktail': {'icon': '🍸', 'subcategories': ['gin-based', 'whiskey-based', 'rum-based', 'vodka-based']},
        'sake': {'icon': '🍶', 'subcategories': ['pure rice', 'honjozo', 'ginjo']},
        'liqueur': {'icon': '🥂', 'subcategories': ['cream', 'herbal', 'fruit', 'coffee']}
    }
    
    # Cuisine Types and Flags
    CUISINE_FLAGS = {
        'Turkish': '🇹🇷',
        'French': '🇫🇷', 
        'Italian': '🇮🇹',
        'Japanese': '🇯🇵',
        'British': '🇬🇧',
        'American': '🇺🇸',
        'Chinese': '🇨🇳',
        'Indian': '🇮🇳',
        'Mexican': '🇲🇽',
        'Thai': '🇹🇭',
        'International': '🌍'
    }
    
    # Flavor Profile Icons
    FLAVOR_ICONS = {
        'sweet': '🍯',
        'salty': '🧂', 
        'sour': '🍋',
        'bitter': '☕',
        'umami': '🍄',
        'spicy': '🌶️',
        'smoky': '🔥',
        'fruity': '🍇',
        'herbal': '🌿',
        'earthy': '🌰',
        'fresh': '🌊',
        'rich': '🧈',
        'acidic': '🍋',
        'floral': '🌸',
        'nutty': '🥜',
        'citrus': '🍊',
        'mineral': '🗿',
        'oak': '🌳',
        'vanilla': '🌟',
        'chocolate': '🍫',
        'coffee': '☕'
    }
    
    # Machine Learning Settings
    ML_CONFIG = {
        'min_ratings_for_trend': 3,
        'user_rating_weight': 0.6,
        'global_rating_weight': 0.4,
        'learning_rate': 0.01,
        'batch_size': 32,
        'epochs': 100
    }
    
    # Web Interface Settings
    WEB_CONFIG = {
        'items_per_page': 12,
        'max_recommendations': 8,
        'session_timeout': 3600,  # 1 hour
        'cache_timeout': 300      # 5 minutes
    }
    
    # API Rate Limiting
    RATE_LIMIT = {
        'requests_per_minute': 60,
        'requests_per_hour': 1000
    }
    
    # Logging Configuration
    LOGGING_CONFIG = {
        'level': 'INFO',
        'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        'file': 'app.log',
        'max_bytes': 1024*1024,  # 1MB
        'backup_count': 5
    }

class DevelopmentConfig(Config):
    """Development environment configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production environment configuration"""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or None
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for production environment")

class TestingConfig(Config):
    """Testing environment configuration"""
    DEBUG = True
    TESTING = True
    DATABASE_PATH = ':memory:'  # In-memory database for testing

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
