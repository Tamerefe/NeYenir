"""
Advanced Data Models and Database Management
Enhanced models with additional features and validation
"""

from dataclasses import dataclass, field, asdict
from typing import Dict, List, Optional, Tuple, Union
from datetime import datetime, timedelta
import json
import sqlite3
import hashlib
from enum import Enum
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AlcoholTolerance(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class PriceRange(Enum):
    BUDGET = "budget"
    MID_RANGE = "mid-range"
    PREMIUM = "premium"

class CookingMethod(Enum):
    GRILLED = "grilled"
    BAKED = "baked"
    FRIED = "fried"
    BOILED = "boiled"
    STEAMED = "steamed"
    RAW = "raw"
    BRAISED = "braised"
    ROASTED = "roasted"
    STIRRED = "stirred"

@dataclass
class NutritionalInfo:
    """Nutritional information for food items"""
    calories_per_100g: Optional[int] = None
    protein_g: Optional[float] = None
    fat_g: Optional[float] = None
    carbs_g: Optional[float] = None
    fiber_g: Optional[float] = None
    sodium_mg: Optional[float] = None

@dataclass
class AlcoholDetails:
    """Detailed alcohol information"""
    alcohol_content: float
    serving_size_ml: int = 150
    calories_per_serving: Optional[int] = None
    sugar_content_g: Optional[float] = None
    sulfites: bool = False
    organic: bool = False

@dataclass
class FoodItem:
    """Enhanced food item with comprehensive details"""
    id: int
    name: str
    cuisine_type: str
    flavor_profile: List[str]
    intensity: int  # 1-10 scale
    texture: str
    cooking_method: CookingMethod
    main_ingredients: List[str]
    dietary_tags: List[str]
    price_range: PriceRange
    serving_temp: str
    nutritional_info: Optional[NutritionalInfo] = None
    description: str = ""
    image_url: str = ""
    preparation_time_minutes: int = 0
    difficulty_level: int = 1  # 1-5 scale
    origin_country: str = ""
    seasonal_availability: List[str] = field(default_factory=list)
    allergens: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        if isinstance(self.cooking_method, str):
            self.cooking_method = CookingMethod(self.cooking_method)
        if isinstance(self.price_range, str):
            self.price_range = PriceRange(self.price_range)

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization"""
        data = asdict(self)
        data['cooking_method'] = self.cooking_method.value
        data['price_range'] = self.price_range.value
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def get_compatibility_vector(self) -> Dict[str, float]:
        """Get numerical vector for ML algorithms"""
        return {
            'intensity': self.intensity / 10.0,
            'spicy': 1.0 if 'spicy' in self.flavor_profile else 0.0,
            'sweet': 1.0 if 'sweet' in self.flavor_profile else 0.0,
            'salty': 1.0 if 'salty' in self.flavor_profile else 0.0,
            'sour': 1.0 if 'sour' in self.flavor_profile else 0.0,
            'bitter': 1.0 if 'bitter' in self.flavor_profile else 0.0,
            'umami': 1.0 if 'umami' in self.flavor_profile else 0.0,
            'price_level': {'budget': 1, 'mid-range': 2, 'premium': 3}[self.price_range.value],
            'difficulty': self.difficulty_level / 5.0
        }

@dataclass  
class AlcoholItem:
    """Enhanced alcohol item with comprehensive details"""
    id: int
    name: str
    type: str
    subtype: str
    alcohol_details: AlcoholDetails
    flavor_profile: List[str]
    body: str
    sweetness: int  # 1-10 scale
    acidity: int   # 1-10 scale  
    tannins: int   # 1-10 scale
    price_range: PriceRange
    region: str
    vintage: Optional[int] = None
    producer: str = ""
    description: str = ""
    image_url: str = ""
    serving_temp_celsius: Optional[Tuple[int, int]] = None
    glassware: str = ""
    food_pairing_notes: str = ""
    awards: List[str] = field(default_factory=list)
    rating_average: float = 0.0
    rating_count: int = 0
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        if isinstance(self.price_range, str):
            self.price_range = PriceRange(self.price_range)

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization"""
        data = asdict(self)
        data['price_range'] = self.price_range.value
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def get_compatibility_vector(self) -> Dict[str, float]:
        """Get numerical vector for ML algorithms"""
        return {
            'alcohol_content': self.alcohol_details.alcohol_content / 50.0,
            'sweetness': self.sweetness / 10.0,
            'acidity': self.acidity / 10.0,
            'tannins': self.tannins / 10.0,
            'body_light': 1.0 if self.body == 'light' else 0.0,
            'body_medium': 1.0 if self.body == 'medium' else 0.0,
            'body_full': 1.0 if self.body == 'full' else 0.0,
            'price_level': {'budget': 1, 'mid-range': 2, 'premium': 3}[self.price_range.value],
            'vintage_quality': (self.vintage - 1900) / 125.0 if self.vintage else 0.5
        }

@dataclass
class EnhancedUserProfile:
    """Enhanced user profile with advanced preferences"""
    user_id: int
    name: str
    email: str = ""
    age: int = 25
    alcohol_tolerance: AlcoholTolerance = AlcoholTolerance.MEDIUM
    preferred_flavors: List[str] = field(default_factory=list)
    disliked_flavors: List[str] = field(default_factory=list)
    dietary_restrictions: List[str] = field(default_factory=list)
    allergies: List[str] = field(default_factory=list)
    budget_preference: PriceRange = PriceRange.MID_RANGE
    favorite_cuisines: List[str] = field(default_factory=list)
    disliked_alcohols: List[str] = field(default_factory=list)
    preferred_alcohol_types: List[str] = field(default_factory=list)
    spice_tolerance: int = 5  # 1-10 scale
    adventurous_level: int = 5  # 1-10 scale
    health_conscious: bool = False
    location: str = ""
    timezone: str = "UTC"
    preferred_meal_times: List[str] = field(default_factory=list)
    social_settings: List[str] = field(default_factory=list)  # casual, formal, party, etc.
    rating_history: List[Tuple[int, int, int, datetime]] = field(default_factory=list)
    favorite_pairings: List[Tuple[int, int]] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    last_login: datetime = field(default_factory=datetime.now)
    profile_completion: float = 0.0

    def __post_init__(self):
        if isinstance(self.alcohol_tolerance, str):
            self.alcohol_tolerance = AlcoholTolerance(self.alcohol_tolerance)
        if isinstance(self.budget_preference, str):
            self.budget_preference = PriceRange(self.budget_preference)
        self.calculate_profile_completion()

    def calculate_profile_completion(self):
        """Calculate profile completion percentage"""
        fields = [
            self.name, self.age, len(self.preferred_flavors) > 0,
            len(self.favorite_cuisines) > 0, self.budget_preference,
            self.spice_tolerance, self.adventurous_level
        ]
        completed = sum(1 for field in fields if field)
        self.profile_completion = (completed / len(fields)) * 100

    def get_preference_vector(self) -> Dict[str, float]:
        """Get user preference vector for ML algorithms"""
        return {
            'age_normalized': (self.age - 18) / 62.0,  # 18-80 range
            'spice_tolerance': self.spice_tolerance / 10.0,
            'adventurous_level': self.adventurous_level / 10.0,
            'budget_level': {'budget': 0.2, 'mid-range': 0.6, 'premium': 1.0}[self.budget_preference.value],
            'alcohol_tolerance': {'low': 0.3, 'medium': 0.6, 'high': 1.0}[self.alcohol_tolerance.value],
            'health_conscious': 1.0 if self.health_conscious else 0.0,
            'rating_count': min(len(self.rating_history) / 50.0, 1.0)  # Normalize to max 50 ratings
        }

@dataclass
class PairingRating:
    """Enhanced pairing rating with context"""
    id: int
    user_id: int
    food_id: int
    alcohol_id: int
    rating: int  # 1-5 scale
    context: str = ""  # dinner, lunch, party, etc.
    occasion: str = ""  # birthday, date, casual, etc.
    season: str = ""
    weather: str = ""
    mood: str = ""
    companions: int = 1  # number of people
    location_type: str = ""  # home, restaurant, bar, etc.
    notes: str = ""
    would_recommend: bool = True
    created_at: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization"""
        data = asdict(self)
        data['created_at'] = self.created_at.isoformat()
        return data

@dataclass
class TrendingPairing:
    """Trending pairing with analytics"""
    food_id: int
    alcohol_id: int
    food_name: str
    alcohol_name: str
    average_rating: float
    rating_count: int
    trend_score: float
    popularity_rank: int
    growth_rate: float  # week over week
    demographic_breakdown: Dict[str, Dict] = field(default_factory=dict)
    seasonal_trend: Dict[str, float] = field(default_factory=dict)
    last_updated: datetime = field(default_factory=datetime.now)

class EnhancedDatabaseManager:
    """Enhanced database manager with advanced features"""
    
    def __init__(self, db_path: str = "enhanced_food_alcohol_system.db"):
        self.db_path = db_path
        self.conn = None
        self.initialize_database()
    
    def get_connection(self):
        """Get database connection with proper error handling"""
        if not self.conn:
            self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
            self.conn.execute("PRAGMA foreign_keys = ON")
        return self.conn
    
    def initialize_database(self):
        """Initialize enhanced database schema"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # Enhanced users table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE,
                    age INTEGER CHECK(age >= 18),
                    alcohol_tolerance TEXT CHECK(alcohol_tolerance IN ('low', 'medium', 'high')),
                    preferred_flavors TEXT,
                    disliked_flavors TEXT,
                    dietary_restrictions TEXT,
                    allergies TEXT,
                    budget_preference TEXT CHECK(budget_preference IN ('budget', 'mid-range', 'premium')),
                    favorite_cuisines TEXT,
                    disliked_alcohols TEXT,
                    preferred_alcohol_types TEXT,
                    spice_tolerance INTEGER CHECK(spice_tolerance BETWEEN 1 AND 10),
                    adventurous_level INTEGER CHECK(adventurous_level BETWEEN 1 AND 10),
                    health_conscious BOOLEAN DEFAULT FALSE,
                    location TEXT,
                    timezone TEXT DEFAULT 'UTC',
                    preferred_meal_times TEXT,
                    social_settings TEXT,
                    profile_completion REAL DEFAULT 0.0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Enhanced foods table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS foods (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    cuisine_type TEXT NOT NULL,
                    flavor_profile TEXT NOT NULL,
                    intensity INTEGER CHECK(intensity BETWEEN 1 AND 10),
                    texture TEXT,
                    cooking_method TEXT,
                    main_ingredients TEXT,
                    dietary_tags TEXT,
                    price_range TEXT CHECK(price_range IN ('budget', 'mid-range', 'premium')),
                    serving_temp TEXT,
                    description TEXT,
                    image_url TEXT,
                    preparation_time_minutes INTEGER DEFAULT 0,
                    difficulty_level INTEGER CHECK(difficulty_level BETWEEN 1 AND 5),
                    origin_country TEXT,
                    seasonal_availability TEXT,
                    allergens TEXT,
                    calories_per_100g INTEGER,
                    protein_g REAL,
                    fat_g REAL,
                    carbs_g REAL,
                    fiber_g REAL,
                    sodium_mg REAL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Enhanced alcohols table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS alcohols (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    type TEXT NOT NULL,
                    subtype TEXT,
                    alcohol_content REAL NOT NULL,
                    serving_size_ml INTEGER DEFAULT 150,
                    calories_per_serving INTEGER,
                    sugar_content_g REAL,
                    sulfites BOOLEAN DEFAULT FALSE,
                    organic BOOLEAN DEFAULT FALSE,
                    flavor_profile TEXT NOT NULL,
                    body TEXT CHECK(body IN ('light', 'medium', 'full')),
                    sweetness INTEGER CHECK(sweetness BETWEEN 1 AND 10),
                    acidity INTEGER CHECK(acidity BETWEEN 1 AND 10),
                    tannins INTEGER CHECK(tannins BETWEEN 1 AND 10),
                    price_range TEXT CHECK(price_range IN ('budget', 'mid-range', 'premium')),
                    region TEXT NOT NULL,
                    vintage INTEGER,
                    producer TEXT,
                    description TEXT,
                    image_url TEXT,
                    serving_temp_min INTEGER,
                    serving_temp_max INTEGER,
                    glassware TEXT,
                    food_pairing_notes TEXT,
                    awards TEXT,
                    rating_average REAL DEFAULT 0.0,
                    rating_count INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Enhanced pairings table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS pairings (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    food_id INTEGER NOT NULL,
                    alcohol_id INTEGER NOT NULL,
                    rating INTEGER CHECK(rating BETWEEN 1 AND 5),
                    context TEXT,
                    occasion TEXT,
                    season TEXT,
                    weather TEXT,
                    mood TEXT,
                    companions INTEGER DEFAULT 1,
                    location_type TEXT,
                    notes TEXT,
                    would_recommend BOOLEAN DEFAULT TRUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (user_id),
                    FOREIGN KEY (food_id) REFERENCES foods (id),
                    FOREIGN KEY (alcohol_id) REFERENCES alcohols (id),
                    UNIQUE(user_id, food_id, alcohol_id)
                )
            ''')
            
            # User sessions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_sessions (
                    session_id TEXT PRIMARY KEY,
                    user_id INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    expires_at TIMESTAMP NOT NULL,
                    ip_address TEXT,
                    user_agent TEXT,
                    is_active BOOLEAN DEFAULT TRUE,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            ''')
            
            # Analytics table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS analytics (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_type TEXT NOT NULL,
                    event_data TEXT,
                    user_id INTEGER,
                    session_id TEXT,
                    ip_address TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (user_id)
                )
            ''')
            
            # Create indexes for better performance
            indexes = [
                "CREATE INDEX IF NOT EXISTS idx_pairings_user_id ON pairings(user_id)",
                "CREATE INDEX IF NOT EXISTS idx_pairings_food_id ON pairings(food_id)",
                "CREATE INDEX IF NOT EXISTS idx_pairings_alcohol_id ON pairings(alcohol_id)",
                "CREATE INDEX IF NOT EXISTS idx_pairings_rating ON pairings(rating)",
                "CREATE INDEX IF NOT EXISTS idx_pairings_created_at ON pairings(created_at)",
                "CREATE INDEX IF NOT EXISTS idx_users_email ON users(email)",
                "CREATE INDEX IF NOT EXISTS idx_foods_cuisine_type ON foods(cuisine_type)",
                "CREATE INDEX IF NOT EXISTS idx_alcohols_type ON alcohols(type)",
                "CREATE INDEX IF NOT EXISTS idx_alcohols_region ON alcohols(region)",
                "CREATE INDEX IF NOT EXISTS idx_sessions_user_id ON user_sessions(user_id)",
                "CREATE INDEX IF NOT EXISTS idx_sessions_expires_at ON user_sessions(expires_at)",
                "CREATE INDEX IF NOT EXISTS idx_analytics_event_type ON analytics(event_type)",
                "CREATE INDEX IF NOT EXISTS idx_analytics_timestamp ON analytics(timestamp)"
            ]
            
            for index_sql in indexes:
                cursor.execute(index_sql)
            
            conn.commit()
            logger.info("Enhanced database initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing database: {e}")
            conn.rollback()
            raise
    
    def create_user(self, user_profile: EnhancedUserProfile) -> int:
        """Create a new user in the database"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO users (
                    name, email, age, alcohol_tolerance, preferred_flavors,
                    disliked_flavors, dietary_restrictions, allergies, budget_preference,
                    favorite_cuisines, disliked_alcohols, preferred_alcohol_types,
                    spice_tolerance, adventurous_level, health_conscious, location,
                    timezone, preferred_meal_times, social_settings, profile_completion
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                user_profile.name, user_profile.email, user_profile.age,
                user_profile.alcohol_tolerance.value, json.dumps(user_profile.preferred_flavors),
                json.dumps(user_profile.disliked_flavors), json.dumps(user_profile.dietary_restrictions),
                json.dumps(user_profile.allergies), user_profile.budget_preference.value,
                json.dumps(user_profile.favorite_cuisines), json.dumps(user_profile.disliked_alcohols),
                json.dumps(user_profile.preferred_alcohol_types), user_profile.spice_tolerance,
                user_profile.adventurous_level, user_profile.health_conscious,
                user_profile.location, user_profile.timezone,
                json.dumps(user_profile.preferred_meal_times), json.dumps(user_profile.social_settings),
                user_profile.profile_completion
            ))
            
            user_id = cursor.lastrowid
            conn.commit()
            logger.info(f"Created user with ID: {user_id}")
            return user_id
            
        except Exception as e:
            logger.error(f"Error creating user: {e}")
            conn.rollback()
            raise
    
    def log_event(self, event_type: str, event_data: Dict, user_id: Optional[int] = None, 
                  session_id: Optional[str] = None, ip_address: Optional[str] = None):
        """Log analytics event"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO analytics (event_type, event_data, user_id, session_id, ip_address)
                VALUES (?, ?, ?, ?, ?)
            ''', (event_type, json.dumps(event_data), user_id, session_id, ip_address))
            
            conn.commit()
            
        except Exception as e:
            logger.error(f"Error logging event: {e}")
    
    def get_trending_pairings(self, limit: int = 10, days: int = 30) -> List[TrendingPairing]:
        """Get trending pairings with advanced analytics"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # Complex query to get trending pairings
            cursor.execute('''
                SELECT 
                    p.food_id, p.alcohol_id,
                    f.name as food_name, a.name as alcohol_name,
                    AVG(p.rating) as avg_rating,
                    COUNT(*) as rating_count,
                    COUNT(*) * AVG(p.rating) as trend_score
                FROM pairings p
                JOIN foods f ON p.food_id = f.id
                JOIN alcohols a ON p.alcohol_id = a.id
                WHERE p.created_at >= datetime('now', '-{} days')
                GROUP BY p.food_id, p.alcohol_id
                HAVING COUNT(*) >= 2
                ORDER BY trend_score DESC, avg_rating DESC
                LIMIT ?
            '''.format(days), (limit,))
            
            results = cursor.fetchall()
            trending_pairings = []
            
            for i, row in enumerate(results):
                pairing = TrendingPairing(
                    food_id=row[0], alcohol_id=row[1],
                    food_name=row[2], alcohol_name=row[3],
                    average_rating=round(row[4], 2), rating_count=row[5],
                    trend_score=row[6], popularity_rank=i + 1,
                    growth_rate=0.0  # Could be calculated with more complex query
                )
                trending_pairings.append(pairing)
            
            return trending_pairings
            
        except Exception as e:
            logger.error(f"Error getting trending pairings: {e}")
            return []
    
    def close_connection(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()
            self.conn = None
    
    def __del__(self):
        """Destructor to ensure connection is closed"""
        self.close_connection()
