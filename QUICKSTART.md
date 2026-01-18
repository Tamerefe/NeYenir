# 🚀 Ne Yenir? - Deployment Hızlı Başlangıç

## 📦 Sistem Yapısı

Bu proje **iki ayrı deployment** sistemi kullanır:

### 1️⃣ Demo Site (GitHub Pages) 🎨
- **Amaç**: Tanıtım, dökümantasyon
- **Teknoloji**: Statik HTML/CSS/JS
- **URL**: https://[username].github.io/NeYenir/
- **Klasör**: `docs/`

### 2️⃣ Production Site (Flask App) 🚀
- **Amaç**: Canlı uygulama
- **Teknoloji**: Python Flask + AI
- **Platform**: Render.com / Railway / Heroku
- **Klasör**: Tüm proje

---

## ⚡ Hızlı Kurulum

### Demo Site (5 dakika)

1. **GitHub Pages'i Aktifleştir**
   ```
   GitHub repo → Settings → Pages
   Source: Deploy from a branch
   Branch: main
   Folder: /docs
   ```

2. **Push yap**
   ```bash
   git add .
   git commit -m "Setup GitHub Pages"
   git push origin main
   ```

3. **✅ Hazır!** 
   Site URL: `https://[username].github.io/NeYenir/`

### Production Site - Render.com (10 dakika)

1. **Render.com'a Git**
   - https://render.com → Kayıt ol/Giriş yap

2. **Web Service Oluştur**
   - "New +" → "Web Service"
   - GitHub repo'nuzu bağlayın
   - Repository seçin: `NeYenir`

3. **Ayarlar**
   ```
   Name: neyenir
   Region: Frankfurt (veya en yakın)
   Branch: main
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn run:app
   ```

4. **Environment Variables**
   ```
   FLASK_ENV=production
   SECRET_KEY=[otomatik oluşturulur]
   ```

5. **Create Web Service** → Deploy başlar

6. **✅ Hazır!**
   Site URL: `https://neyenir.onrender.com`

### Production Site - Railway (5 dakika)

1. **Railway.app'e Git**
   - https://railway.app → GitHub ile giriş

2. **New Project**
   - "New Project"
   - "Deploy from GitHub repo"
   - `NeYenir` seçin

3. **✅ Otomatik Deploy!**
   - Railway Flask uygulamasını algılar
   - Otomatik deploy eder
   - URL verilir

### Production Site - Heroku (10 dakika)

1. **Heroku CLI Kur**
   ```bash
   # Windows: https://devcenter.heroku.com/articles/heroku-cli
   # Mac: brew install heroku/brew/heroku
   ```

2. **Deploy**
   ```bash
   heroku login
   heroku create neyenir-app
   git push heroku main
   heroku open
   ```

---

## 📁 Dosyalar

Deployment için oluşturulan dosyalar:

```
✅ Procfile              # Heroku için
✅ railway.json          # Railway için
✅ app.json              # Heroku button için
✅ requirements.txt      # Python dependencies (gunicorn eklendi)
✅ .github/workflows/
   ├── deploy-demo.yml       # GitHub Pages workflow
   └── deploy-production.yml # Production CI/CD
✅ .github/
   ├── DEPLOYMENT.md    # Detaylı deployment dokümantasyonu
   └── PAGES.md         # GitHub Pages bilgisi
```

---

## 🔄 Otomatik Deploy

Her `git push` ile:

1. **`docs/` değişirse** → GitHub Pages deploy
2. **`app/` değişirse** → Production platform deploy
3. **Her ikisi de** → İkisi de deploy

---

## 🛠️ Lokal Test

```bash
# Virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Dependencies
pip install -r requirements.txt

# Run
python run.py

# Test
# http://localhost:5000
```

---

## ✅ Deployment Checklist

- [ ] GitHub repo oluşturuldu
- [ ] `docs/` klasörü hazır
- [ ] GitHub Pages aktif
- [ ] Workflow dosyaları eklendi
- [ ] Production platform seçildi
- [ ] Environment variables ayarlandı
- [ ] İlk deploy yapıldı
- [ ] Site test edildi

---

## 📊 Platform Karşılaştırma

| Platform | Ücretsiz | Kolay Kurulum | Özellikler | Önerilen |
|----------|----------|---------------|------------|----------|
| **Render.com** | ✅ 750h/ay | ⭐⭐⭐⭐⭐ | DB, CRON, SSL | ✅ En iyi |
| **Railway** | ✅ $5 kredi | ⭐⭐⭐⭐⭐ | Otomatik, hızlı | ✅ Kolay |
| **Heroku** | ⚠️ Sınırlı | ⭐⭐⭐ | Eski, güvenilir | ⚠️ Pahalı |

---

## 🆘 Sorun Giderme

### Demo site görünmüyor
```bash
# GitHub Pages ayarlarını kontrol et
# Settings → Pages → Branch: main, Folder: /docs
```

### Production deploy hatası
```bash
# Logs kontrolü
# Render: Dashboard → Logs
# Railway: Project → Deployments → View logs
# Heroku: heroku logs --tail
```

### Bağımlılık hatası
```bash
# requirements.txt güncelle
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push
```

---

## 📖 Detaylı Dökümantasyon

- [DEPLOYMENT.md](.github/DEPLOYMENT.md) - Detaylı deployment rehberi
- [PAGES.md](.github/PAGES.md) - GitHub Pages bilgisi
- [README.md](README.md) - Proje ana dökümantasyonu

---

## 🎯 Sonraki Adımlar

1. ✅ Demo site deploy
2. ✅ Production platform seçimi
3. ✅ İlk deploy
4. ⏭️ Custom domain (opsiyonel)
5. ⏭️ SSL sertifikası (otomatik)
6. ⏭️ Monitoring kurulumu

---

**Hazır! İyi deploylar! 🚀**
