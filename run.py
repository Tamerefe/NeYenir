#!/usr/bin/env python3
"""
NeYenir - AI Destekli Yemek & Alkol Eşleştirme Sistemi
Uygulamayı başlatmak için başlangıç betiği
"""

import sys
import os
import argparse
import subprocess
from pathlib import Path

def check_dependencies():
    """Gerekli tüm paketlerin yüklü olup olmadığını kontrol et"""
    required_packages = [
        'flask', 'numpy', 'sqlite3', 'sklearn'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            if package == 'sklearn':
                import sklearn
            else:
                __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Eksik gerekli paketler:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n📦 Eksik paketleri şu komutla yükleyin:")
        print("   pip install -r requirements.txt")
        return False
    
    print("✅ Tüm bağımlılıklar yüklü!")
    return True

def run_console_app():
    """Uygulamanın konsol sürümünü çalıştır"""
    print("🍷 AI Destekli Yemek & Alkol Eşleştirme Sistemi Başlatılıyor (Konsol)")
    print("=" * 60)
    
    try:
        from core.matcher import main
        main()
    except KeyboardInterrupt:
        print("\n\n👋 NeYenir'i kullandığınız için teşekkürler!")
    except Exception as e:
        print(f"❌ Konsol uygulaması çalıştırılırken hata: {e}")

def run_web_app(host='localhost', port=5000, debug=True):
    """Uygulamanın web sürümünü çalıştır"""
    print(f"🌐 AI Destekli Yemek & Alkol Eşleştirme Sistemi Başlatılıyor (Web)")
    print(f"🔗 Sunucu şu adreste kullanıma hazır olacak: http://{host}:{port}")
    print("=" * 60)
    
    try:
        from app import create_app
        app = create_app()
        app.run(host=host, port=port, debug=debug)
    except KeyboardInterrupt:
        print("\n\n👋 Sunucu durduruldu. NeYenir'i kullandığınız için teşekkürler!")
    except Exception as e:
        print(f"❌ Web uygulaması çalıştırılırken hata: {e}")

def setup_database():
    """Veritabanını örnek verilerle başlat"""
    print("🗄️ Veritabanı kuruluyor...")
    
    try:
        from main import AIFoodAlcoholMatcher
        matcher = AIFoodAlcoholMatcher()
        print("✅ Veritabanı başarıyla başlatıldı!")
    except Exception as e:
        print(f"❌ Veritabanı kurulurken hata: {e}")

def show_system_info():
    """Sistem bilgilerini ve istatistiklerini göster"""
    print("📊 AI Food & Alcohol Pairing System Information")
    print("=" * 60)
    
    try:
        from core.matcher import AIFoodAlcoholMatcher
        matcher = AIFoodAlcoholMatcher()
        
        print(f"🍽️ Available Foods: {len(matcher.foods)}")
        print(f"🍺 Available Alcohols: {len(matcher.alcohols)}")
        print(f"🤖 AI Algorithm: Advanced Neural Network + Rule-based")
        print(f"📊 Machine Learning: Collaborative Filtering + Content-based")
        print(f"🗄️ Database: SQLite with analytics")
        print(f"🌐 Web Interface: Flask + Bootstrap 5")
        print(f"📱 Mobile Support: Responsive design")
        
        # Show database statistics
        import sqlite3
        conn = sqlite3.connect('food_alcohol_system.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM pairings")
        pairing_count = cursor.fetchone()[0]
        
        print(f"👤 Registered Users: {user_count}")
        print(f"⭐ Total Ratings: {pairing_count}")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error getting system info: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="NeYenir - AI Destekli Yemek & Alkol Eşleştirme Sistemi",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Örnekler:
  python run.py console          # Konsol sürümünü çalıştır
  python run.py web             # Web sürümünü çalıştır (varsayılan)
  python run.py web --port 8080 # Web sürümünü 8080 portunda çalıştır
  python run.py setup           # Veritabanını başlat
  python run.py info            # Sistem bilgilerini göster
        """
    )
    
    parser.add_argument(
        'mode', 
        nargs='?', 
        default='web',
        choices=['console', 'web', 'setup', 'info'],
        help='Uygulama modu (varsayılan: web)'
    )
    
    parser.add_argument(
        '--host',
        default='localhost',
        help='Web sunucusunun bağlanacağı host (varsayılan: localhost)'
    )
    
    parser.add_argument(
        '--port',
        type=int,
        default=5000,
        help='Web sunucusunun bağlanacağı port (varsayılan: 5000)'
    )
    
    parser.add_argument(
        '--no-debug',
        action='store_true',
        help='Web sunucusu için debug modunu devre dışı bırak'
    )
    
    args = parser.parse_args()
    
    print("🍷 NeYenir - AI Destekli Yemek & Alkol Eşleştirme Sistemi")
    print("Sürüm 2.0 - Gelişmiş AI Sürümü")
    print("=" * 60)
    
    # Önce bağımlılıkları kontrol et
    if not check_dependencies():
        sys.exit(1)
    
    if args.mode == 'setup':
        setup_database()
    elif args.mode == 'info':
        show_system_info()
    elif args.mode == 'console':
        run_console_app()
    elif args.mode == 'web':
        debug_mode = not args.no_debug
        run_web_app(args.host, args.port, debug_mode)

if __name__ == "__main__":
    main()
