# 🚀 Deployment Documentation

## ☁️ Streamlit Cloud Deployment

### Setup
1. **GitHub Repository** mit korrekter Struktur
2. **Streamlit Cloud Account** verbinden
3. **App deployen** aus spezifischem Ordner

### Konfiguration
```toml
# .streamlit/config.toml
[theme]
primaryColor = "#FF6B6B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"

[server]
maxUploadSize = 200
```

## 🐳 Docker Production

### Build & Deploy
```bash
# Production Build
docker build -f Dockerfile.streamlit -t amalea-app .

# Run in Production
docker run -p 8501:8501 amalea-app
```

### Environment Variables
```bash
STREAMLIT_SERVER_PORT=8501
STREAMLIT_SERVER_ADDRESS=0.0.0.0
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

## 📋 Deployment Checklist

### Pre-Deployment
- [ ] Alle Notebooks getestet
- [ ] Streamlit Apps funktional
- [ ] Requirements.txt aktuell
- [ ] README.md vollständig
- [ ] Sensitive Daten entfernt

### Post-Deployment
- [ ] Live-URLs testen
- [ ] Performance monitoring
- [ ] User feedback sammeln
- [ ] Dokumentation aktualisieren

# 📚 Archivierte Dokumentation

Dieses Verzeichnis enthält archivierte Dokumentations-Dateien, Skripte und Präsentationen.

## 📁 Inhalt

### 📋 Dokumentation & READMEs
- `06_Computer_Vision_README_OLD.md` - Alte Computer Vision Dokumentation
- `06_Computer_Vision_README_NEW.md` - Überarbeitete Computer Vision Dokumentation
- `README.md` (development) - Entwickler-Dokumentation (archiviert)
- `README.md` (deployment) - Deployment-Dokumentation (archiviert)

### 🎤 Präsentationen & Status
- `STATUS_UPDATE_FINAL.md` - Finaler Status-Update

**Hinweis:** Die aktuelle `BEGRÜSSUNG_PRÄSENTATION.md` befindet sich im Hauptverzeichnis

### 🔧 Skripte & Tools
- `cleanup_docs.sh` - Dokumentations-Bereinigungsskript (Prozess-Dokumentation)
- `check_repository.sh` - Repository-Prüfungsskript

## 📋 Zweck
Diese Dateien wurden archiviert, da sie:
- Redundant zu aktueller Dokumentation sind
- Historischen/Referenz-Wert haben
- Den Bereinigungsprozess dokumentieren

## 🔄 Wiederherstellung
Bei Bedarf können archivierte Dateien konsultiert oder wiederhergestellt werden.
