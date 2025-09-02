"""
Ne Yenir? - Web Arayüzü
Modern Flask web uygulaması ile responsive tasarım
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for, flash
from main import AIFoodAlcoholMatcher, UserProfile
import json
from datetime import datetime
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Global matcher instance
matcher = AIFoodAlcoholMatcher()

@app.route('/')
def index():
    """Homepage with beautiful interface"""
    trending_pairings = matcher.get_trending_pairings(6)
    return render_template('index.html', trending_pairings=trending_pairings)

@app.route('/foods')
def foods():
    """Browse all available foods"""
    return render_template('foods.html', foods=matcher.foods)

@app.route('/alcohols')
def alcohols():
    """Browse all available alcohols"""
    return render_template('alcohols.html', alcohols=matcher.alcohols)

@app.route('/recommend')
def recommend():
    """Food selection for recommendations"""
    return render_template('recommend.html', foods=matcher.foods)

@app.route('/api/recommendations/<food_name>')
def api_recommendations(food_name):
    """API endpoint for getting recommendations"""
    user_profile = None
    if 'user_id' in session and session['user_id'] in matcher.user_profiles:
        user_profile = matcher.user_profiles[session['user_id']]
    
    all_recommendations = matcher.get_recommendations(food_name.replace('-', ' '), user_profile, top_n=5)
    
    # AI Recommendations
    ai_result = []
    for alcohol, score, explanation in all_recommendations["ai_recommendations"]:
        ai_result.append({
            'name': alcohol.name,
            'type': alcohol.type,
            'subtype': alcohol.subtype,
            'alcohol_content': alcohol.alcohol_content,
            'region': alcohol.region,
            'price_range': alcohol.price_range,
            'flavor_profile': alcohol.flavor_profile,
            'body': alcohol.body,
            'score': round(score, 1),
            'explanation': explanation,
            'source': 'ai'
        })
    
    # Expert Recommendations
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

@app.route('/profile')
def profile():
    """User profile page"""
    if 'user_id' not in session:
        return redirect(url_for('create_profile'))
    
    user_profile = matcher.user_profiles.get(session['user_id'])
    if not user_profile:
        return redirect(url_for('create_profile'))
    
    history = matcher.get_user_history(user_profile.user_id)
    return render_template('profile.html', user=user_profile, history=history)

@app.route('/create_profile', methods=['GET', 'POST'])
def create_profile():
    """Create user profile"""
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

@app.route('/api/rate_pairing', methods=['POST'])
def rate_pairing():
    """Rate a food-alcohol pairing"""
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

@app.route('/trending')
def trending():
    """Trending pairings page"""
    trending_pairings = matcher.get_trending_pairings(20)
    return render_template('trending.html', pairings=trending_pairings)

@app.route('/logout')
def logout():
    """Logout user"""
    session.pop('user_id', None)
    flash('Başarıyla çıkış yapıldı!', 'info')
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found(error):
    """404 error handler with logo"""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
