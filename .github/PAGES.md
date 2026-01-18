# Ne Yenir? - GitHub Pages Demo Site

Bu klasör, projenin **demo/dökümantasyon** versiyonunu içerir.
Statik HTML sayfaları olarak GitHub Pages üzerinde yayınlanır.

## Demo Site vs Production Site

| Özellik | Demo Site (GitHub Pages) | Production Site |
|---------|-------------------------|-----------------|
| **Teknoloji** | Statik HTML/CSS/JS | Flask (Python) |
| **URL** | github.io | Render/Railway |
| **Backend** | ❌ Yok | ✅ Var |
| **Database** | ❌ Yok | ✅ Var |
| **AI Öneriler** | ⚠️ Mock data | ✅ Gerçek AI |
| **Kullanıcı Profili** | ❌ Yok | ✅ Var |
| **Amaç** | Tanıtım/Demo | Canlı uygulama |

## Deployment

### Otomatik Deploy
- **Trigger**: `docs/` klasöründe değişiklik olduğunda
- **Workflow**: `.github/workflows/deploy-demo.yml`
- **Branch**: main

### Manuel Deploy
```bash
git add docs/
git commit -m "Update demo site"
git push origin main
```

## Site Yapısı

```
docs/
├── index.html          # Ana sayfa
├── README.md           # Dökümantasyon
└── assets/
    ├── css/
    │   └── style.css
    └── images/
```

## GitHub Pages Ayarları

1. **Repository Settings** → **Pages**
2. **Source**: Deploy from a branch
3. **Branch**: main
4. **Folder**: /docs
5. **Save**

Site URL: `https://[username].github.io/NeYenir/`

## Notlar

- Bu sadece demo/tanıtım sitesidir
- Gerçek uygulama için production deployment gerekir
- Detaylı bilgi için: [DEPLOYMENT.md](DEPLOYMENT.md)
