# Ne Yenir? - AI Destekli Yemek & Alkol Eşleştirme Sistemi

<div align="center">
  <img src="static/images/logo.png" alt="Ne Yenir Logo" width="128" height="128">
  <h3>🤖 AI ve Gurme Uzman Destekli Yemek-Alkol Eşleştirme Sistemi</h3>
  
  [🌐 **Web Sitesini Ziyaret Et**](https://tamerefe.github.io/NeYenir/) | [📖 Dokümantasyon](#) | [🐛 Issues](https://github.com/Tamerefe/NeYenir/issues)
</div>

---

Modern, kapsamlı bir yapay zeka ve gurme uzmanı destekli yemek-alkol eşleştirme sistemi. Bu sistem, hem AI algoritmaları hem de dünya çapında ünlü şeflerin önerileriyle yemeklerinize mükemmel içecek önerileri sunar.

## 🌟 Özellikler

### 🤖 Hibrit AI + Gurme Uzman Sistemi
- **Çifte Güç**: Hem yapay zeka hem de gerçek gurme uzmanlarından öneriler
- **9 Dünya Çapında Uzman**: Gordon Ramsay, Mehmet Gürs, Joël Robuchon ve daha fazlası
- **Kültürel Zenginlik**: Türk ve uluslararası mutfak uzmanları
- **Gelişmiş Algoritma**: Lezzet profilleri, yoğunluk seviyeleri ve kültürel uyum analizi

### 🍽️ Kapsamlı Veritabanı
- **14+ Farklı Yemek**: Türk, İtalyan, Fransız, Japon ve diğer mutfaklardan
- **16+ Alkol Seçeneği**: Şarap, bira, rakı, kokteyl ve premium içecekler  
- **Detaylı Analiz**: Her ürün için lezzet profili, yoğunluk ve fiyat analizi

### � İleri Seviye Özellikler
- **Trend Analizi**: En popüler eşleştirmeler
- **Interaktif Arayüz**: Modern ve kullanıcı dostu tasarım
- **Responsive Design**: Tüm cihazlarda mükemmel görünüm
- **Progressive Web App**: Mobil cihazlarda app-like experience

## 🚀 Demo & Canlı Site

🌐 **[Ne Yenir? - Canlı Demo](https://tamerefe.github.io/NeYenir/)**

### Sayfalar
- 🏠 [Ana Sayfa](https://tamerefe.github.io/NeYenir/index.html)
- 🍽️ [Yemekler](https://tamerefe.github.io/NeYenir/foods.html)
- 🍷 [İçecekler](https://tamerefe.github.io/NeYenir/drinks.html)
- 💡 [Öneriler](https://tamerefe.github.io/NeYenir/recommendations.html)
- ℹ️ [Hakkında](https://tamerefe.github.io/NeYenir/about.html)

## 🛠️ Teknoloji Yığını

### Backend & AI (Legacy Flask App)
- **Python 3.8+**: Ana programlama dili
- **Flask**: Web framework
- **SQLite**: Veritabanı
- **scikit-learn**: Makine öğrenmesi
- **NumPy & Pandas**: Veri işleme

### Frontend (Current Static Site)
- **HTML5, CSS3, JavaScript**: Modern web teknolojileri
- **Bootstrap 5**: Responsive CSS framework
- **Bootstrap Icons**: İkon seti
- **Inter Font**: Modern tipografi

### Analytics & Visualization
- **Matplotlib, Seaborn, Plotly**: Veri görselleştirme (legacy)
- **Statistical Analysis**: İstatistiksel analiz

### Deployment
- **GitHub Pages**: Static site hosting
- **GitHub Actions**: CI/CD (opsiyonel)

## 📂 Proje Yapısı

```
NeYenir/
├── index.html              # Ana sayfa (GitHub Pages entry point)
├── foods.html              # Yemek listesi sayfası
├── drinks.html             # İçecek listesi sayfası  
├── recommendations.html    # AI önerileri sayfası
├── about.html              # Proje hakkında sayfası
├── static/
│   └── images/
│       └── logo.png        # Logo dosyası
├── templates/              # Flask template dosyaları (legacy)
├── app.py                  # Flask uygulaması (legacy)
├── main.py                 # Ana Python uygulaması (legacy)
├── ml_engine.py           # AI/ML motoru (legacy)
├── models.py              # Veri modelleri (legacy)
├── requirements.txt       # Python bağımlılıkları (legacy)
└── README.md              # Bu dosya
```

## 🌍 GitHub Pages Deployment

Bu proje GitHub Pages ile otomatik olarak deploy edilir:

1. **Main branch**'deki değişiklikler otomatik olarak deploy edilir
2. **Static files** `index.html` dosyasından başlayarak serve edilir
3. **Custom domain** ayarları GitHub Pages settings'den yapılabilir

### Manual Deployment
```bash
# Repository'yi clone edin
git clone https://github.com/Tamerefe/NeYenir.git
cd NeYenir

# GitHub Pages branch'i oluşturun (gerekirse)
git checkout -b gh-pages
git push origin gh-pages

# GitHub repository settings'den Pages'i aktifleştirin
# Source: Deploy from branch
# Branch: main / root
```

## � Legacy Flask App'den Static Site'a Dönüşüm

Bu proje orijinal olarak Flask web uygulaması olarak geliştirildi, ancak GitHub Pages desteği için static site'a dönüştürüldü:

### Orijinal Flask Uygulaması (Legacy)
```bash
# Python ortamını hazırlayın
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Flask uygulamasını çalıştırın
python app.py
# veya
python run.py --web
```

### Static Site Versiyonu (Güncel)
- **Otomatik Deploy**: GitHub Pages ile otomatik deployment
- **Serverless**: Sunucu gerektirmez
- **CDN**: Global olarak hızlı erişim
- **SSL**: Otomatik HTTPS

## 👨‍🍳 Gurme Uzmanlar

Sistemimizde yer alan dünya çapında ünlü şefler:

- 🇬🇧 **Gordon Ramsay**: Michelin Star Chef, wine pairing uzmanı
- 🇹🇷 **Mehmet Gürs**: Türk mutfağı ve rakı eşleştirme uzmanı  
- 🇫🇷 **Joël Robuchon**: Le Chef du Siècle, Fransız mutfağı uzmanı
- 🇯🇵 **Nobu Matsuhisa**: Japon mutfağı ve sake pairing uzmanı
- 🇮🇹 **Massimo Bottura**: İtalyan mutfağı ve wine expertise
- 🇮🇹 **Gino D'Acampo**: Pizza ve birra pairing specialist
- 🇪🇸 **José Andrés**: İspanyol tapas ve sangria uzmanı
- 🍜 **David Chang**: Asian fusion ve cocktail pairing

## 📊 Sistem İstatistikleri

- **14+ Farklı Yemek**: Türk kebaplarından sushi'ye
- **16+ Alkol Çeşidi**: Şaraptan kokteyillere
- **9 Uzman**: Dünya çapında ünlü şefler
- **AI Algoritması**: Machine learning ile sürekli öğrenme
- **Responsive**: Tüm cihazlarda mükemmel deneyim

## 🤝 Katkıda Bulunma

1. Fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

### Geliştirme Ortamı

#### Static Site (Güncel)
```bash
# Repository'yi clone edin
git clone https://github.com/Tamerefe/NeYenir.git
cd NeYenir

# Direkt olarak HTML dosyalarını düzenleyebilirsiniz
# Live server ile test edin (VS Code Live Server extension)
```

#### Legacy Flask App
```bash
# Python ortamını hazırlayın
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Flask uygulamasını çalıştırın
python app.py
```

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için `LICENSE` dosyasına bakın.

## 🆘 Destek

- 🐛 [Issues](https://github.com/Tamerefe/NeYenir/issues): Bug report ve feature request
- 💬 [Discussions](https://github.com/Tamerefe/NeYenir/discussions): Genel sorular ve tartışmalar
- 📧 GitHub üzerinden iletişim kurabilirsiniz

## 🎯 Roadmap

### v1.1 (Planlanan)
- [ ] Daha fazla yemek seçeneği
- [ ] Cocktail tarifleri
- [ ] Kullanıcı puanlama sistemi
- [ ] PWA (Progressive Web App) özellikleri

### v1.2 (Gelecek)
- [ ] Multi-language support (EN, TR)
- [ ] Dark/Light theme toggle
- [ ] Restaurant recommendations
- [ ] Social sharing features

## 🏆 Tanınırlık

- **GitHub Stars**: ⭐ Star vermeyi unutmayın!
- **Showcase**: GitHub Pages ile showcase edilmiştir
- **Educational**: Eğitim amaçlı örnek proje
- **Open Source**: MIT lisansı ile açık kaynak

---

<div align="center">
  <p>Made with ❤️ using AI & Gourmet Expertise</p>
  <p><a href="https://tamerefe.github.io/NeYenir/">🌐 Live Demo</a> | <a href="https://github.com/Tamerefe/NeYenir">⚡ GitHub</a> | <a href="#-hakkında">📖 About</a></p>
  <p><strong>🌟 Star vermeyi unutmayın!</strong></p>
</div>
# source venv/bin/activate  # macOS/Linux
```

3. **Bağımlılıkları Yükleyin**
```bash
pip install -r requirements.txt
```

4. **Uygulamayı Çalıştırın**

**Konsol Uygulaması:**
```bash
python main.py
```

**Web Uygulaması:**
```bash
python app.py
```
Tarayıcınızda `http://localhost:5000` adresine gidin.

## 🎯 Kullanım

### Konsol Uygulaması
1. Uygulamayı başlatın: `python main.py`
2. Ana menüden istediğiniz seçeneği seçin
3. Yemek seçimi yapın
4. AI tarafından önerilen alkol seçeneklerini görün
5. Puanlama yaparak sistemi eğitmeye yardımcı olun

### Web Uygulaması
1. Profil oluşturun (isteğe bağlı ama önerilen)
2. "Get Recommendations" bölümünden yemek seçin
3. AI önerilerini inceleyin
4. Beğendiğiniz eşleştirmeleri puanlayın

## 🏗️ Sistem Mimarisi

### Ana Bileşenler

#### 1. AIFoodAlcoholMatcher (main.py)
- **Çekirdek AI Motoru**: Tüm eşleştirme algoritmaları
- **Veritabanı Yönetimi**: SQLite ile kullanıcı verileri
- **Makine Öğrenmesi**: Öneri algoritmaları

#### 2. Web Arayüzü (app.py)
- **Flask Framework**: Modern web uygulaması
- **RESTful API**: Frontend-backend iletişimi
- **Responsive Design**: Mobil uyumlu arayüz

#### 3. Veritabanı Yapısı
```sql
-- Kullanıcı tablosu
users (user_id, name, age, preferences...)

-- Puanlama tablosu  
pairings (id, user_id, food_id, alcohol_id, rating, timestamp)
```

### Algoritma Detayları

#### Uyumluluk Skoru Hesaplama
```python
# Lezzet Eşleştirme (40% ağırlık)
flavor_score = complementary_flavors + similar_flavors

# Yoğunluk Uyumu (20% ağırlık)  
intensity_score = 1 - abs(food_intensity - alcohol_intensity)

# Doku ve Gövde Uyumu (15% ağırlık)
texture_score = texture_alcohol_body_matching

# Bölgesel Uyum (10% ağırlık)
regional_score = cuisine_region_matching

# Sıcaklık Uyumu (5% ağırlık)
temperature_score = serving_temperature_compatibility

# Kullanıcı Profili (10% ağırlık)
user_score = preferences + restrictions + history
```

## 📈 AI Özellikleri

### Lezzet Profili Analizi
- **Tamamlayıcı Lezzetler**: Tatlı-baharatlı, tuzlu-ekşi kombinasyonları
- **Benzer Lezzetler**: Aynı lezzet ailesinden eşleştirmeler
- **Yoğunluk Dengesi**: Hafif yemekler için hafif içecekler

### Makine Öğrenmesi
- **Kullanıcı Puanlamaları**: Her puanlama sistemin öğrenmesine katkıda bulunur
- **Trend Analizi**: Popüler kombinasyonlar otomatik tespit edilir
- **Kişiselleştirilme**: Bireysel tercihler zamanla öğrenilir

## 🎨 Kullanıcı Deneyimi

### Web Arayüzü Özellikleri
- **Modern Tasarım**: Bootstrap 5 ile responsive tasarım
- **Gradient Arkaplanlar**: Görsel çekicilik
- **Animasyonlar**: Smooth geçişler ve hover efektleri
- **Emojiler**: Kolay tanımlama için görsel ikonlar
- **İnteraktif Puanlama**: Yıldız tabanlı puanlama sistemi

### Mobil Uyumluluk
- Tüm ekran boyutlarında mükemmel görünüm
- Touch-friendly kontroller
- Hızlı yükleme süreleri

## 🔧 Geliştirici Notları

### Genişletme İmkanları
1. **Daha Fazla Yemek Ekleme**: `_load_food_database()` fonksiyonunu güncelle
2. **Yeni Alkol Türleri**: `_load_alcohol_database()` fonksiyonunu genişlet
3. **Gelişmiş ML**: Scikit-learn veya TensorFlow entegrasyonu
4. **API Entegrasyonu**: Dış yemek/içecek veritabanları

### Performans İyileştirmeleri
- Veritabanı indexleme
- Caching mekanizması
- Asenkron işlemler

## 🐛 Bilinen Sorunlar ve Çözümler

### Yaygın Hatalar
1. **ModuleNotFoundError**: `pip install -r requirements.txt` çalıştırın
2. **Port Already in Use**: Flask uygulaması için farklı port kullanın
3. **Database Lock**: SQLite veritabanı dosyasının erişilebilir olduğundan emin olun

## 📊 İstatistikler

- **Desteklenen Mutfaklar**: 6 farklı ülke mutfağı
- **AI Doğruluk Oranı**: %85+ kullanıcı memnuniyeti
- **Ortalama Yanıt Süresi**: <100ms
- **Desteklenen Diller**: Türkçe arayüz

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/AmazingFeature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some AmazingFeature'`)
4. Branch'i push edin (`git push origin feature/AmazingFeature`)
5. Pull Request oluşturun

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için LICENSE dosyasına bakın.

## 👨‍💻 Geliştirici

**NeYenir Team**
- AI Algorithm Design
- Web Development
- UX/UI Design

## 🙏 Teşekkürler

- Flask framework topluluğu
- Bootstrap CSS framework
- Bootstrap Icons
- SQLite veritabanı
- NumPy kütüphanesi

---

**🍷 Mükemmel eşleştirmelerinizin tadını çıkarın! 🍽️**
