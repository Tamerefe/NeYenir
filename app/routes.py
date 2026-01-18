"""
Flask route'ları
Tüm web endpoint'leri burada tanımlanır
"""

from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for, flash
from core.matcher import AIFoodAlcoholMatcher
from app.utils.cache import load_trending_cache, save_trending_cache, TRENDING_CACHE_FILE
from app.utils.translations import (
    FLAVOR_TRANSLATIONS, PRICE_TRANSLATIONS, BODY_TRANSLATIONS,
    TYPE_TRANSLATIONS, SUBTYPE_TRANSLATIONS, REGION_TRANSLATIONS
)
import random
import os
from pathlib import Path

bp = Blueprint('main', __name__)

# Global eşleştirici örneği
matcher = AIFoodAlcoholMatcher()

def get_weekly_trending_pairings(count=20):
    """
    Haftalık rastgele trend eşleştirmeler al.
    Önbellek varsa ve geçerliyse onu kullan, yoksa yeni rastgele seçim yap.
    """
    # Önbellekten yükle
    cached = load_trending_cache()
    if cached is not None:
        print("✅ Önbellekten haftalık trendler yüklendi")
        return cached[:count]
    
    # Yeni rastgele trendler oluştur
    print("🔄 Yeni haftalık trendler oluşturuluyor...")
    
    # Tüm olasi eşleştirmeleri oluştur
    all_pairings = []
    foods = matcher.foods
    alcohols = matcher.alcohols
    
    for food in foods:
        for alcohol in alcohols:
            # Uyumluluk skoru hesapla
            score = matcher.calculate_compatibility_score(food, alcohol)
            
            # Sadece iyi eşleştirmeleri dahil et (skor > 50)
            if score > 50:
                all_pairings.append({
                    'food': {
                        'id': food.id,
                        'name': food.name,
                        'cuisine_type': food.cuisine_type,
                        'intensity': food.intensity,
                        'flavor_profile': food.flavor_profile
                    },
                    'alcohol': {
                        'id': alcohol.id,
                        'name': alcohol.name,
                        'type': alcohol.type,
                        'alcohol_content': alcohol.alcohol_content
                    },
                    'compatibility_score': round(score, 1),
                    'popularity_count': random.randint(15, 150),
                    'average_rating': round(random.uniform(3.5, 5.0), 1)
                })
    
    # Eğer yeterli eşleştirme yoksa
    if len(all_pairings) < count:
        count = len(all_pairings)
    
    # Rastgele seçim yap
    if len(all_pairings) > 0:
        selected = random.sample(all_pairings, min(count, len(all_pairings)))
        # Popülerite göre sırala
        selected.sort(key=lambda x: (x['popularity_count'], x['compatibility_score']), reverse=True)
        
        # Önbelleğe kaydet
        save_trending_cache(selected)
        return selected
    
    return []

@bp.route('/')
def index():
    """Ana sayfa — modern ve görsel arayüz"""
    trending_pairings = get_weekly_trending_pairings(6)
    return render_template('index.html', 
                         trending_pairings=trending_pairings,
                         foods=matcher.foods,
                         alcohols=matcher.alcohols)

@bp.route('/foods')
def foods():
    """Browse all available foods"""
    return render_template('foods.html', foods=matcher.foods)

@bp.route('/alcohols')
def alcohols():
    """Browse all available alcohols"""
    return render_template('alcohols.html', alcohols=matcher.alcohols)

@bp.route('/recommend')
def recommend():
    """Food selection for recommendations"""
    return render_template('recommend.html', foods=matcher.foods)

@bp.route('/api/recommendations/<food_name>')
def api_recommendations(food_name):
    """Öneri almak için API uç noktası"""
    user_profile = None
    if 'user_id' in session and session['user_id'] in matcher.user_profiles:
        user_profile = matcher.user_profiles[session['user_id']]
    
    all_recommendations = matcher.get_recommendations(food_name.replace('-', ' '), user_profile, top_n=5)
    
    # AI önerileri
    ai_result = []
    for alcohol, score, explanation in all_recommendations["ai_recommendations"]:
        ai_result.append({
            'name': alcohol.name,
            'type': TYPE_TRANSLATIONS.get(alcohol.type, alcohol.type),
            'subtype': SUBTYPE_TRANSLATIONS.get(alcohol.subtype, alcohol.subtype),
            'alcohol_content': alcohol.alcohol_content,
            'region': REGION_TRANSLATIONS.get(alcohol.region.lower(), alcohol.region),
            'price_range': PRICE_TRANSLATIONS.get(alcohol.price_range, alcohol.price_range),
            'flavor_profile': [FLAVOR_TRANSLATIONS.get(f, f) for f in alcohol.flavor_profile],
            'body': BODY_TRANSLATIONS.get(alcohol.body, alcohol.body),
            'score': round(score, 1),
            'explanation': explanation,
            'source': 'ai'
        })
    
    # Uzman önerileri
    expert_result = []
    for drink, score, explanation, expert_info in all_recommendations["expert_recommendations"]:
        expert_data = {
            'name': drink,
            'score': score,
            'explanation': explanation,
            'source': 'expert'
        }
        if expert_info:
            expert_data['expert'] = {
                'name': expert_info.name,
                'country': expert_info.country,
                'bio': expert_info.bio,
                'michelin_stars': expert_info.michelin_stars,
                'speciality': expert_info.speciality,
                'famous_for': expert_info.famous_for
            }
        expert_result.append(expert_data)
    
    return jsonify({
        'ai_recommendations': ai_result,
        'expert_recommendations': expert_result
    })

@bp.route('/profile')
def profile():
    """Kullanıcı profil sayfası"""
    if 'user_id' not in session:
        return redirect(url_for('main.create_profile'))
    
    user_profile = matcher.user_profiles.get(session['user_id'])
    if not user_profile:
        return redirect(url_for('main.create_profile'))
    
    history = matcher.get_user_history(user_profile.user_id)
    return render_template('profile.html', user=user_profile, history=history)

@bp.route('/create_profile', methods=['GET', 'POST'])
def create_profile():
    """Kullanıcı profili oluşturma"""
    if request.method == 'POST':
        data = request.get_json()
        
        preferences = {
            'alcohol_tolerance': data.get('alcohol_tolerance', 'medium'),
            'preferred_flavors': data.get('preferred_flavors', []),
            'budget_preference': data.get('budget_preference', 'mid-range'),
            'dietary_restrictions': data.get('dietary_restrictions', []),
            'favorite_cuisines': data.get('favorite_cuisines', []),
            'disliked_alcohols': data.get('disliked_alcohols', [])
        }
        
        user_profile = matcher.create_user_profile(
            data['name'], 
            int(data['age']), 
            preferences
        )
        
        session['user_id'] = user_profile.user_id
        return jsonify({'status': 'success', 'user_id': user_profile.user_id})
    
    return render_template('create_profile.html')

@bp.route('/api/rate_pairing', methods=['POST'])
def rate_pairing():
    """Bir yemek-alkol eşleştirmesini puanla"""
    if 'user_id' not in session:
        return jsonify({'error': 'User not logged in'}), 401
    
    data = request.get_json()
    matcher.rate_pairing(
        session['user_id'],
        data['food_name'],
        data['alcohol_name'], 
        int(data['rating'])
    )
    
    return jsonify({'status': 'success'})

@bp.route('/trending')
def trending():
    """Trending pairings page"""
    trending_pairings = get_weekly_trending_pairings(20)
    return render_template('trending.html', pairings=trending_pairings)

@bp.route('/api/refresh_trending', methods=['POST'])
def refresh_trending():
    """Manuel olarak trend önbelleğini yenile (admin endpoint)"""
    try:
        # Önbellek dosyasını sil
        if TRENDING_CACHE_FILE.exists():
            TRENDING_CACHE_FILE.unlink()
        
        # Yeni trendler oluştur
        new_trends = get_weekly_trending_pairings(20)
        
        return jsonify({
            'status': 'success',
            'message': 'Trendler başarıyla yenilendi',
            'count': len(new_trends)
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@bp.route('/cocktails')
def cocktails():
    """Kokteyl önerileri sayfası"""
    return render_template('cocktails.html')

@bp.route('/api/cocktail_recommendations', methods=['POST'])
def api_cocktail_recommendations():
    """Kokteyl önerileri API"""
    data = request.get_json()
    mood = data.get('mood', 'happy')
    flavor_preference = data.get('flavor_preference', 'balanced')
    occasion = data.get('occasion', 'casual')
    
    # Kokteyl veritabanı
    cocktails_db = {
        'Mojito': {
            'ingredients': ['Beyaz Rom', 'Nane', 'Limon', 'Şeker', 'Soda'],
            'alcohol_content': 10,
            'flavor': 'fresh',
            'mood': ['happy', 'energetic'],
            'occasion': ['casual', 'party'],
            'description': 'Ferahlatıcı ve hafif bir klasik kokteyl',
            'image': '🍹'
        },
        'Margarita': {
            'ingredients': ['Tekila', 'Triple Sec', 'Limon Suyu', 'Tuz'],
            'alcohol_content': 18,
            'flavor': 'sour',
            'mood': ['happy', 'party'],
            'occasion': ['party', 'celebration'],
            'description': 'Ekşi ve ferahlatıcı Meksika klasiği',
            'image': '🍸'
        },
        'Old Fashioned': {
            'ingredients': ['Bourbon', 'Şeker', 'Angostura Bitters', 'Portakal Kabuğu'],
            'alcohol_content': 35,
            'flavor': 'bitter',
            'mood': ['relaxed', 'sophisticated'],
            'occasion': ['formal', 'dinner'],
            'description': 'Klasik ve sofistike bir viski kokteyli',
            'image': '🥃'
        },
        'Cosmopolitan': {
            'ingredients': ['Votka', 'Triple Sec', 'Cranberry Suyu', 'Limon'],
            'alcohol_content': 22,
            'flavor': 'balanced',
            'mood': ['happy', 'sophisticated'],
            'occasion': ['party', 'formal'],
            'description': 'Zarif ve dengeli bir kokteyl',
            'image': '🍸'
        },
        'Pina Colada': {
            'ingredients': ['Beyaz Rom', 'Hindistan Cevizi Kremi', 'Ananas Suyu'],
            'alcohol_content': 12,
            'flavor': 'sweet',
            'mood': ['relaxed', 'happy'],
            'occasion': ['casual', 'beach'],
            'description': 'Tropik ve kremsi bir tatil kokteyli',
            'image': '🍹'
        },
        'Negroni': {
            'ingredients': ['Gin', 'Campari', 'Kırmızı Vermut'],
            'alcohol_content': 24,
            'flavor': 'bitter',
            'mood': ['sophisticated', 'relaxed'],
            'occasion': ['formal', 'aperitif'],
            'description': 'İtalyan aperitif klasiği, acı ve dengeli',
            'image': '🍷'
        },
        'Aperol Spritz': {
            'ingredients': ['Aperol', 'Prosecco', 'Soda', 'Portakal'],
            'alcohol_content': 8,
            'flavor': 'balanced',
            'mood': ['happy', 'relaxed'],
            'occasion': ['casual', 'aperitif'],
            'description': 'Hafif ve ferahlatıcı İtalyan içkisi',
            'image': '🍹'
        },
        'Manhattan': {
            'ingredients': ['Rye Whiskey', 'Kırmızı Vermut', 'Angostura Bitters'],
            'alcohol_content': 30,
            'flavor': 'balanced',
            'mood': ['sophisticated', 'relaxed'],
            'occasion': ['formal', 'dinner'],
            'description': 'Klasik New York kokteyli',
            'image': '🍸'
        }
    }
    
    # Filtreleme ve puanlama
    recommendations = []
    for name, cocktail in cocktails_db.items():
        score = 0
        
        # Mood eşleşmesi
        if mood in cocktail['mood']:
            score += 30
        
        # Flavor eşleşmesi
        if flavor_preference == cocktail['flavor'] or flavor_preference == 'balanced':
            score += 25
        
        # Occasion eşleşmesi
        if occasion in cocktail['occasion']:
            score += 25
        
        # Alkol seviyesi bonusu
        score += 20
        
        recommendations.append({
            'name': name,
            'score': score,
            'ingredients': cocktail['ingredients'],
            'alcohol_content': cocktail['alcohol_content'],
            'description': cocktail['description'],
            'image': cocktail['image']
        })
    
    # Skorlara göre sırala
    recommendations.sort(key=lambda x: x['score'], reverse=True)
    
    return jsonify({'recommendations': recommendations[:6]})

@bp.route('/bac_calculator')
def bac_calculator():
    """Promil hesaplayıcı sayfası"""
    return render_template('bac_calculator.html')

@bp.route('/api/calculate_bac', methods=['POST'])
def api_calculate_bac():
    """Promil hesaplama API"""
    data = request.get_json()
    
    weight = float(data.get('weight', 70))  # kg
    gender = data.get('gender', 'male')
    drinks = data.get('drinks', [])
    hours_since_first_drink = float(data.get('hours', 1))
    
    # Widmark formülü
    r_value = 0.68 if gender == 'male' else 0.55
    
    total_alcohol_grams = 0
    drink_details = []
    
    for drink in drinks:
        volume_ml = float(drink.get('volume', 0))
        alcohol_percent = float(drink.get('alcohol_percent', 0))
        
        # Alkol gramı = hacim (ml) x alkol % x 0.789 (alkol yoğunluğu)
        alcohol_grams = volume_ml * (alcohol_percent / 100) * 0.789
        total_alcohol_grams += alcohol_grams
        
        drink_details.append({
            'name': drink.get('name', 'İçki'),
            'volume': volume_ml,
            'alcohol_percent': alcohol_percent,
            'alcohol_grams': round(alcohol_grams, 2)
        })
    
    # BAC hesaplama
    if total_alcohol_grams > 0 and weight > 0:
        # BAC hesaplama (g/L cinsinden)
        bac_g_per_L = total_alcohol_grams / (r_value * weight)
        
        # g/L'den g/dL'ye çevir (÷10)
        bac = bac_g_per_L / 10
        
        # Zaman faktörü - vücut saatte yaklaşık 0.015 g/dL metabolize eder
        bac = bac - (0.015 * hours_since_first_drink)
        bac = max(0, bac)  # Negatif değer olamaz
    else:
        bac = 0
    
    # Promil seviyesine göre durum
    bac_promil = bac * 10
    
    if bac_promil < 0.2:
        status = 'Ayık'
        status_color = 'success'
        recommendations = ['Güvenli bir seviyedesiniz']
    elif bac_promil < 0.5:
        status = 'Minimal Etki'
        status_color = 'info'
        recommendations = ['Hafif bir etki hissedebilirsiniz', 'Araç kullanmakta dikkatli olun']
    elif bac_promil < 0.8:
        status = 'Hafif Sarhoşluk'
        status_color = 'warning'
        recommendations = ['Araç kullanmayın', 'Koordinasyonunuz etkilenmiş olabilir']
    elif bac_promil < 1.5:
        status = 'Orta Sarhoşluk'
        status_color = 'warning'
        recommendations = ['ASLA araç kullanmayın', 'Tepki süreniz önemli ölçüde yavaşlamıştır', 'Su için ve dinlenin']
    else:
        status = 'Yüksek Sarhoşluk / Tehlikeli'
        status_color = 'danger'
        recommendations = ['ASLA araç kullanmayın', 'Tıbbi yardım gerekebilir', 'Birisiyle kalın', 'Bol su için']
    
    # Ayılma zamanı (0.15 promil/saat = 0.015 g/dL/saat)
    hours_to_sober = bac_promil / 0.15 if bac_promil > 0 else 0
    
    return jsonify({
        'bac': round(bac, 4),
        'bac_percentage': round(bac * 100, 2),
        'bac_promil': round(bac_promil, 2),
        'status': status,
        'status_color': status_color,
        'recommendations': recommendations,
        'total_alcohol_grams': round(total_alcohol_grams, 2),
        'hours_to_sober': round(hours_to_sober, 1),
        'drink_details': drink_details
    })

@bp.route('/logout')
def logout():
    """Logout user"""
    session.pop('user_id', None)
    flash('Başarıyla çıkış yapıldı!', 'info')
    return redirect(url_for('main.index'))

# 404 handler is registered in app/__init__.py

