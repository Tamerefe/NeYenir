# NeYenir - GitHub Pages

Bu klasör GitHub Pages için statik HTML dosyalarını içerir.

## Yapı

```
docs/
├── index.html              # Ana sayfa
├── recommend.html          # Öneri sayfası
├── foods.html              # Yemekler listesi
├── alcohols.html           # İçecekler listesi
├── trending.html           # Trend eşleştirmeler
├── cocktails.html          # Kokteyl önerileri
├── bac-calculator.html     # Promil hesaplayıcı
├── create-profile.html     # Profil oluşturma
├── assets/
│   ├── css/
│   │   └── style.css       # Stil dosyası
│   └── images/
│       └── logo.png        # Logo ve görseller
└── README.md              # Bu dosya
```

## GitHub Pages Kurulumu

1. GitHub repository'nize gidin
2. Settings > Pages bölümüne gidin
3. Source olarak "Deploy from a branch" seçin
4. Branch: `main` (veya `master`)
5. Folder: `/docs` seçin
6. Save butonuna tıklayın

Site birkaç dakika içinde `https://[kullanıcı-adı].github.io/[repo-adı]/` adresinde yayınlanacaktır.

## Notlar

- Bu statik HTML dosyaları Flask backend'i olmadan çalışır
- API çağrıları çalışmayacaktır (sadece görsel demo)
- Tüm linkler göreceli path'ler kullanır (`assets/`, `index.html` vb.)
- CSS ve görseller `assets/` klasöründe bulunur

