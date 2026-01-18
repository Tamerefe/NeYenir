# Ne Yenir? - Deployment Sistemi

Bu proje iki farklı deployment sistemi kullanır:

## 🎨 Demo Site (GitHub Pages)
**Statik HTML versiyonu** - Projenin demo/dökümantasyon sayfası

- **URL**: `https://[kullanıcıadı].github.io/NeYenir/`
- **Kaynak**: `docs/` klasörü
- **Deployment**: Otomatik (main branch'e push sonrası)
- **Workflow**: `.github/workflows/deploy-demo.yml`
- **İçerik**: 
  - index.html - Ana sayfa ve proje tanıtımı
  - README.md - Proje dökümantasyonu
  - assets/ - CSS, images
  - Statik dökümantasyon sayfaları

### Demo Site Güncelleme
```bash
# docs/ klasöründeki dosyaları düzenleyin
git add docs/
git commit -m "Update demo site"
git push origin main
# GitHub Pages otomatik deploy eder
```

---

## 🚀 Ana Site (Production)
**Flask uygulaması** - Tam özellikli web uygulaması

- **Platform**: Render.com / Railway.app / Heroku
- **Kaynak**: Tüm proje (app/, core/, templates/, static/)
- **Deployment**: Otomatik (main branch'e push sonrası)
- **Workflow**: `.github/workflows/deploy-production.yml`
- **Özellikler**:
  - AI destekli yemek önerileri
  - Kullanıcı profilleri
  - Dinamik içerik
  - Veritabanı entegrasyonu
  - API endpoints

### Production Deployment Seçenekleri

#### Option 1: Render.com (Önerilen)
1. [Render.com](https://render.com) hesabı oluşturun
2. "New Web Service" > GitHub repo'nuzu bağlayın
3. Ayarlar:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn run:app`
   - **Environment**: Python 3.12
4. Environment Variables:
   ```
   FLASK_ENV=production
   SECRET_KEY=your-secret-key
   ```
5. Deploy > Otomatik deploy aktif

#### Option 2: Railway.app
1. [Railway.app](https://railway.app) hesabı oluşturun
2. "New Project" > "Deploy from GitHub repo"
3. Repo'nuzu seçin
4. Railway otomatik olarak Flask uygulamasını algılar
5. Environment variables ekleyin
6. Deploy edilir

#### Option 3: Heroku
1. [Heroku](https://heroku.com) hesabı oluşturun
2. `Procfile` oluşturun:
   ```
   web: gunicorn run:app
   ```
3. Heroku CLI ile:
   ```bash
   heroku create neyenir-app
   git push heroku main
   ```

### Production Site Güncelleme
```bash
# Uygulama kodunu düzenleyin
git add .
git commit -m "Update production app"
git push origin main
# Platform otomatik deploy eder
```

---

## 📁 Klasör Yapısı

```
NeYenir/
├── .github/
│   └── workflows/
│       ├── deploy-demo.yml       # Demo site workflow
│       └── deploy-production.yml # Production workflow
├── docs/                         # Demo site (GitHub Pages)
│   ├── index.html
│   ├── README.md
│   └── assets/
├── app/                          # Flask uygulaması
├── core/                         # İş mantığı
├── templates/                    # HTML templates
├── static/                       # CSS, JS, images
├── run.py                        # Flask entry point
└── requirements.txt              # Python dependencies
```

---

## 🔧 Geliştirme Ortamı

### Lokal Çalıştırma
```bash
# Sanal ortam oluştur
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Bağımlılıkları yükle
pip install -r requirements.txt

# Uygulamayı çalıştır
python run.py
```

### Test
```bash
# Demo site - Tarayıcıda aç
open docs/index.html

# Production site - Flask dev server
python run.py
# http://localhost:5000
```

---

## 🔄 Deployment İş Akışı

1. **Geliştirme** → Kod değişiklikleri yap
2. **Commit** → `git commit -m "message"`
3. **Push** → `git push origin main`
4. **Otomatik Deploy**:
   - `docs/` değişirse → GitHub Pages deploy
   - `app/` değişirse → Production platform deploy
   - Her iki değişiklik de → İkisi de deploy

---

## 🌐 Siteler

| Site | Amaç | URL | Güncelleme |
|------|------|-----|------------|
| **Demo** | Dökümantasyon, tanıtım | GitHub Pages | `docs/` push |
| **Production** | Canlı uygulama | Render/Railway | `app/` push |

---

## 📝 Notlar

- Demo site sadece statik HTML, JavaScript ile çalışır
- Production site tam Flask backend gerektirir
- Her iki site de bağımsız güncellenir
- GitHub Actions her deploy'u otomatik yapar
