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
pip install -r requirements.txt
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
