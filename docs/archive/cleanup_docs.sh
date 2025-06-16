#!/bin/bash

# 🧹 AMALEA Documentation Cleanup Script
# Bereinigt redundante und veraltete Dokumentations-Dateien

echo "🧹 AMALEA Documentation Cleanup gestartet..."
echo "============================================"

cd "/Users/kqc/Dropbox/Vorlesungen/13. IU - Data Analytics und Big Data/amalea"

# Erstelle docs/ Verzeichnis für Archivierung
mkdir -p "docs/archive"

echo "📦 Archiviere redundante Dokumentations-Dateien..."

# === DATEIEN FÜR ARCHIVIERUNG ===
# Diese Dateien sind redundant oder veraltet, aber werden als Backup archiviert

archive_files=(
    "AMALEA_INHALTE_VOLLSTÄNDIG_INTEGRIERT.md"     # Redundant zu REFACTORING_COMPLETED.md
    "MIGRATION_LOG.md"                             # Veraltet nach Refactoring
    "MODERNISIERUNG_ABGESCHLOSSEN.md"              # Redundant zu README.md
    "MODERNISIERUNG_PLAN_2025.md"                  # In README.md integriert
    "TODO_NÄCHSTE_SCHRITTE.md"                     # Größtenteils erledigt
    "WEITERES_VORGEHEN_PLAN.md"                    # In README.md integriert
    "cleanup_repo.sh"                              # Veraltet nach Refactoring
    "refactor_structure.sh"                        # Nach Refactoring nicht mehr nötig
)

echo ""
echo "📁 Folgende Dateien werden archiviert:"
for file in "${archive_files[@]}"; do
    if [ -f "$file" ]; then
        echo "   📄 $file"
        mv "$file" "docs/archive/"
    fi
done

# === DATEIEN BEHALTEN ===
echo ""
echo "✅ Folgende Dateien bleiben im Hauptverzeichnis:"
essential_files=(
    "README.md"                    # Haupt-Dokumentation
    "LICENSE.md"                   # Legal erforderlich
    "EXECUTIVE_SUMMARY.md"         # Für Stakeholder wichtig
    "REFACTORING_COMPLETED.md"     # Aktuelle Struktur-Dokumentation
    "requirements-2025.txt"        # Technical dependency
    "docker-compose.yml"           # Development environment
    "amalea.yml"                   # Conda environment
    "Dockerfile.jupyter"           # Container config
    "Dockerfile.streamlit"         # Container config
)

for file in "${essential_files[@]}"; do
    if [ -f "$file" ]; then
        echo "   ✅ $file"
    fi
done

# === ARCHIV-README ERSTELLEN ===
echo ""
echo "📝 Erstelle Archive-README..."

cat > "docs/archive/README.md" << 'EOF'
# 📦 Archivierte AMALEA-Dokumentation

**Zweck**: Dieses Verzeichnis enthält Dokumentations-Dateien, die während der AMALEA-Modernisierung entstanden sind, aber nach dem Refactoring redundant oder veraltet wurden.

## 📋 Archivierte Dateien

### Entwicklungs-Logs
- `MIGRATION_LOG.md` - Log der ersten Modernisierungsschritte
- `MODERNISIERUNG_ABGESCHLOSSEN.md` - Zwischenstatus-Dokumentation
- `AMALEA_INHALTE_VOLLSTÄNDIG_INTEGRIERT.md` - Integrations-Bericht

### Planungs-Dokumente
- `MODERNISIERUNG_PLAN_2025.md` - Ursprünglicher Modernisierungsplan
- `TODO_NÄCHSTE_SCHRITTE.md` - Aufgabenliste (größtenteils erledigt)
- `WEITERES_VORGEHEN_PLAN.md` - Weitere Planungsschritte

### Technische Scripts
- `cleanup_repo.sh` - Erstes Repository-Cleanup Script
- `refactor_structure.sh` - Ordner-Refactoring Script

## 🎯 Warum archiviert?

Diese Dateien wurden archiviert, weil:
1. **Redundanz**: Inhalte sind in `README.md` oder `REFACTORING_COMPLETED.md` integriert
2. **Veraltung**: Nach dem Refactoring nicht mehr aktuell
3. **Übersichtlichkeit**: Hauptverzeichnis soll sauber und fokussiert bleiben

## 💾 Backup-Strategie

- ✅ **Nichts gelöscht**: Alle Inhalte sind in diesem Archiv verfügbar
- ✅ **Versioniert**: Git-History bleibt erhalten
- ✅ **Referenzierbar**: Bei Bedarf wieder zugänglich

---

*Archiviert am: 15. Juni 2025*
*Grund: Repository-Cleanup nach erfolgreichem Refactoring*
EOF

# === DOCS-VERZEICHNIS STRUKTURIEREN ===
echo ""
echo "📁 Erstelle docs/ Struktur..."

mkdir -p "docs/development"
mkdir -p "docs/deployment"

# Entwicklungs-Dokumentation
cat > "docs/development/README.md" << 'EOF'
# 🛠️ Development Documentation

## 🔧 Setup für Entwickler

### Lokale Entwicklung
```bash
# Repository klonen
git clone <repo-url>
cd amalea

# Docker-Entwicklung (empfohlen)
docker-compose up

# Oder lokale Installation
pip install -r requirements-2025.txt
```

### Code-Struktur
```
amalea/
├── 01_Python_Grundlagen/      # Woche 1: Python Basics
├── 02_Streamlit_und_Pandas/   # Woche 2: Web-Apps
├── 03_Machine_Learning/       # Woche 3: ML Fundamentals
├── 04_Advanced_Algorithms/    # Woche 4: Advanced ML
├── 05_Neural_Networks/        # Woche 5: Deep Learning
├── 06_Computer_Vision_NLP/    # Woche 6: Computer Vision
├── 07_Deployment_Portfolio/   # Woche 7: Deployment
└── docs/                      # Dokumentation
```

### Contributing Guidelines
1. **Branch-Naming**: `feature/woche-x-topic` oder `fix/issue-description`
2. **Commit-Messages**: `[WocheX] Beschreibung der Änderung`
3. **Testing**: Alle Notebooks vor Commit testen
4. **Documentation**: README.md in jedem Wochenordner aktuell halten

### Technische Standards
- **Python**: 3.11+
- **Jupyter**: Notebooks als .ipynb mit klarer Struktur
- **Streamlit**: Apps in eigenen .py Dateien
- **Docker**: Alle Services über docker-compose
- **Requirements**: Nur produktionsreife, stabile Pakete
EOF

# Deployment-Dokumentation
cat > "docs/deployment/README.md" << 'EOF'
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
EOF

# === HAUPT-README BEREINIGEN ===
echo ""
echo "📝 Bereinige Haupt-README von redundanten Verweisen..."

# Das aktuelle README.md lesen und später gegebenenfalls updates machen
echo "   ℹ️  README.md wird separat überprüft und ggf. aktualisiert"

# === ZUSAMMENFASSUNG ===
echo ""
echo "✅ CLEANUP ABGESCHLOSSEN!"
echo "========================="
echo ""
echo "📦 Archivierte Dateien: $(ls docs/archive/ | wc -l | tr -d ' ') Dateien"
echo "📁 Neue Struktur:"
echo "   docs/"
echo "   ├── archive/          # Archivierte Dateien + README"
echo "   ├── development/      # Entwickler-Dokumentation"
echo "   └── deployment/       # Deployment-Guides"
echo ""
echo "🎯 Hauptverzeichnis ist jetzt sauberer und fokussierter!"
echo ""
echo "📋 Verbliebene Hauptdateien:"
ls -la *.md *.yml *.txt 2>/dev/null | wc -l | xargs echo "   Anzahl:"

echo ""
echo "🚀 Repository ist jetzt production-ready!"
EOF
