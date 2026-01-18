"""
Önbellek yönetimi için yardımcı fonksiyonlar
"""

import json
import os
from datetime import datetime
from pathlib import Path

TRENDING_CACHE_FILE = Path('data/trending_cache.json')
TRENDING_CACHE_DAYS = 7

def load_trending_cache():
    """Önbellek dosyasından trend verileri yükle"""
    if not TRENDING_CACHE_FILE.exists():
        return None
    
    try:
        with open(TRENDING_CACHE_FILE, 'r', encoding='utf-8') as f:
            cache = json.load(f)
            
        # Zaman damgasını kontrol et
        cache_date = datetime.fromisoformat(cache['timestamp'])
        age_days = (datetime.now() - cache_date).days
        
        # Eğer 7 günden eskiyse geçersiz
        if age_days >= TRENDING_CACHE_DAYS:
            return None
            
        return cache['pairings']
    except Exception as e:
        print(f"⚠️ Önbellek yüklenirken hata: {e}")
        return None

def save_trending_cache(pairings):
    """Önbellek dosyasına trend verileri kaydet"""
    TRENDING_CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    cache = {
        'timestamp': datetime.now().isoformat(),
        'pairings': pairings
    }
    
    try:
        with open(TRENDING_CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"⚠️ Önbellek kaydedilirken hata: {e}")

