"""
Ne Yenir? - Flask Web Uygulaması
Flask app factory pattern ile organize edilmiş yapı
"""

from flask import Flask, render_template
import secrets
from pathlib import Path
from app.config import Config

# Proje kök dizinini belirle
BASE_DIR = Path(__file__).parent.parent

def create_app(config_class=Config):
    """Flask uygulaması factory fonksiyonu"""
    # Template ve static klasörlerini kök dizinden belirt
    app = Flask(
        __name__,
        template_folder=str(BASE_DIR / 'templates'),
        static_folder=str(BASE_DIR / 'static')
    )
    app.config.from_object(config_class)
    app.secret_key = secrets.token_hex(16)
    
    # Blueprint'leri kaydet
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)
    
    # Jinja2 filtrelerini kaydet
    from app.utils.translations import register_filters
    register_filters(app)
    
    # 404 error handler
    @app.errorhandler(404)
    def not_found(error):
        """404 error handler"""
        return render_template('404.html'), 404
    
    return app

