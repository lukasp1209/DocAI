# 🎓 AMALEA 2025 - Data Analytics & Big Data

**Modernisierter Kurs für IU Studierende - 5. Semester**

> 🚀 **Vollständig überarbeitet**: Streamlit-basiert, Docker-ready, Portfolio-orientiert

## 📚 Kursstruktur (7 Wochen)

| Woche | Thema | Status | Hauptinhalte |
|-------|-------|--------|--------------|
| **01** | [Python Grundlagen](./01_Python_Grundlagen/) | ✅ | Python Crashkurs, Docker, Glossar |
| **02** | [Streamlit & Pandas](./02_Streamlit_und_Pandas/) | ✅ | Web-Apps, Datenanalyse |
| **03** | [Machine Learning](./03_Machine_Learning/) | ✅ | Iris Klassifikation, ML Pipeline |
| **04** | [Advanced Algorithms](./04_Advanced_Algorithms/) | ✅ | Trees, KNN, Clustering |
| **05** | [Neural Networks](./05_Neural_Networks/) | ✅ | Deep Learning, Backpropagation |
| **06** | [Computer Vision & NLP](./06_Computer_Vision_NLP/) | ✅ | CNNs, Transfer Learning |
| **07** | [Deployment & Portfolio](./07_Deployment_Portfolio/) | ✅ | MLOps, Cloud, APIs |

## 🚀 Quick Start

### Mit Docker (Empfohlen)
```bash
# Repository klonen
git clone <repo-url>
cd amalea

# Entwicklungsumgebung starten
docker-compose up

# Jupyter: http://localhost:8888
# Streamlit: http://localhost:8501
```

### Lokal
```bash
# Dependencies installieren
pip install -r requirements-2025.txt

# Jupyter starten
jupyter notebook

# Streamlit Apps starten
cd 02_Streamlit_und_Pandas
streamlit run app.py
```

## 🎯 Lernziele

Nach dem Kurs kannst du:

- ✅ **Python für Data Science** professionell einsetzen
- ✅ **Interactive Web-Apps** mit Streamlit entwickeln
- ✅ **Machine Learning Pipelines** erstellen und deployen
- ✅ **Neural Networks** verstehen und implementieren
- ✅ **Portfolio-Projekte** für Bewerbungen präsentieren
- ✅ **Cloud Deployment** für echte Nutzer

## 🏆 Bewertung (Portfolio statt Klausur)

| Komponente | Gewichtung | Beschreibung |
|------------|------------|--------------|
| **Wöchentliche Aufgaben** | 40% | Jupyter Notebooks + Streamlit Apps |
| **Hauptprojekt** | 40% | End-to-End ML Projekt mit Deployment |
| **Präsentation** | 20% | Portfolio-Präsentation (10 Min) |

## 📊 Technischer Stack

### Core Technologies
- 🐍 **Python 3.11+** - Programmiersprache
- 📊 **Pandas** - Datenverarbeitung
- 🤖 **Scikit-learn** - Machine Learning
- 🧠 **TensorFlow/Keras** - Deep Learning
- 🚀 **Streamlit** - Web-Apps
- 🐳 **Docker** - Entwicklungsumgebung

### Deployment & Tools
- ☁️ **Streamlit Cloud** - App Hosting
- 🐙 **GitHub** - Version Control
- 📈 **Plotly** - Interaktive Visualisierungen
- 🔧 **VS Code** - Development Environment

## 🛠️ Projektbeispiele

### Beginner-Projekte (Wochen 1-3)
- 📊 **Daten-Dashboard** - CSV Upload + Visualisierung
- 🏠 **House Price Predictor** - Regression mit Feature Engineering
- 🌸 **Iris Classifier** - Klassifikation mit verschiedenen Algorithmen

### Advanced-Projekte (Wochen 4-7)
- 🧠 **Neural Network Playground** - Interaktive Deep Learning Demo
- 👁️ **Image Classifier** - CNNs für Computer Vision
- 📝 **Sentiment Analyzer** - NLP für Text Analysis
- 🚀 **Full-Stack ML App** - End-to-End Deployment

## 📁 Repository-Struktur

```
amalea/
├── 01_Python_Grundlagen/          # Python Basics + Docker
├── 02_Streamlit_und_Pandas/       # Web-Apps + Data Analysis
├── 03_Machine_Learning/           # ML Fundamentals
├── 04_Advanced_Algorithms/        # Trees, KNN, Clustering
├── 05_Neural_Networks/            # Deep Learning
├── 06_Computer_Vision_NLP/        # CNNs + Text Processing
├── 07_Deployment_Portfolio/       # Cloud + Presentations
├── BACKUP_Original_AMALEA_Notebooks/  # Original Content
├── requirements-2025.txt          # Python Dependencies
├── docker-compose.yml             # Development Environment
└── README.md                      # This file
```

## 🔧 Troubleshooting

### Häufige Probleme

**Docker startet nicht:**
```bash
# Docker Desktop installiert und gestartet?
docker --version
docker-compose --version
```

**Import Errors:**
```bash
# Requirements installieren
pip install -r requirements-2025.txt

# Oder Docker verwenden
docker-compose up --build
```

**Streamlit App läuft nicht:**
```bash
# Port bereits belegt?
streamlit run app.py --server.port 8502
```

## 📚 Zusätzliche Ressourcen

### Offizielle Dokumentation
- 🐍 [Python Docs](https://docs.python.org/3/)
- 🚀 [Streamlit Docs](https://docs.streamlit.io/)
- 📊 [Pandas Docs](https://pandas.pydata.org/docs/)
- 🤖 [Scikit-learn Docs](https://scikit-learn.org/stable/)

### Online Kurse & Tutorials
- 📺 [3Blue1Brown Neural Networks](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- 🎓 [CS231n Stanford Course](http://cs231n.stanford.edu/)
- 📖 [Hands-On Machine Learning](https://github.com/ageron/handson-ml3)

## 👨‍🏫 Support

Bei Fragen oder Problemen:

1. 📖 **Erst Dokumentation checken** (README in den Ordnern)
2. 🔍 **Google/StackOverflow** für spezifische Errors
3. 💬 **Kurs-Forum** für fachliche Fragen
4. 📧 **Instructor** für größere Probleme

---

## 🎉 Los geht's!

1. **Starte mit [01_Python_Grundlagen](./01_Python_Grundlagen/)**
2. **Arbeite dich chronologisch durch die Wochen**
3. **Experimentiere mit den Streamlit-Apps**
4. **Erstelle dein eigenes Portfolio-Projekt**

**Ziel**: Am Ende des Kurses hast du 5-7 deployed ML-Apps in deinem Portfolio! 🚀

---

*AMALEA 2025 - Modernized for the Future of Data Science* ✨
