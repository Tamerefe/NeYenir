#!/usr/bin/env python3
"""
NeYenir - AI Food & Alcohol Pairing System
Startup script for running the application
"""

import sys
import os
import argparse
import subprocess
from pathlib import Path

def check_dependencies():
    """Check if all required packages are installed"""
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
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n📦 Install missing packages with:")
        print("   pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies are installed!")
    return True

def run_console_app():
    """Run the console version of the application"""
    print("🍷 Starting AI Food & Alcohol Pairing System (Console)")
    print("=" * 60)
    
    try:
        from main import main
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Thank you for using NeYenir!")
    except Exception as e:
        print(f"❌ Error running console app: {e}")

def run_web_app(host='localhost', port=5000, debug=True):
    """Run the web version of the application"""
    print(f"🌐 Starting AI Food & Alcohol Pairing System (Web)")
    print(f"🔗 Server will be available at: http://{host}:{port}")
    print("=" * 60)
    
    try:
        from app import app
        app.run(host=host, port=port, debug=debug)
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Thank you for using NeYenir!")
    except Exception as e:
        print(f"❌ Error running web app: {e}")

def setup_database():
    """Initialize the database with sample data"""
    print("🗄️ Setting up database...")
    
    try:
        from main import AIFoodAlcoholMatcher
        matcher = AIFoodAlcoholMatcher()
        print("✅ Database initialized successfully!")
    except Exception as e:
        print(f"❌ Error setting up database: {e}")

def show_system_info():
    """Show system information and statistics"""
    print("📊 AI Food & Alcohol Pairing System Information")
    print("=" * 60)
    
    try:
        from main import AIFoodAlcoholMatcher
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
        description="NeYenir - AI Food & Alcohol Pairing System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run.py console          # Run console version
  python run.py web             # Run web version (default)
  python run.py web --port 8080 # Run web on port 8080
  python run.py setup           # Initialize database
  python run.py info            # Show system information
        """
    )
    
    parser.add_argument(
        'mode', 
        nargs='?', 
        default='web',
        choices=['console', 'web', 'setup', 'info'],
        help='Application mode (default: web)'
    )
    
    parser.add_argument(
        '--host',
        default='localhost',
        help='Host to bind web server (default: localhost)'
    )
    
    parser.add_argument(
        '--port',
        type=int,
        default=5000,
        help='Port to bind web server (default: 5000)'
    )
    
    parser.add_argument(
        '--no-debug',
        action='store_true',
        help='Disable debug mode for web server'
    )
    
    args = parser.parse_args()
    
    print("🍷 NeYenir - AI Food & Alcohol Pairing System")
    print("Version 2.0 - Advanced AI Edition")
    print("=" * 60)
    
    # Check dependencies first
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
