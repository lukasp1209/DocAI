# 🎓 AMALEA 2025 - Data Analytics & Big Data

**Modernisierter Kurs für IU Studierende - 5. Semester**

> 🚀 **Vollständig modernisiert**: 15 Notebooks + 8 Streamlit Apps + Docker + Portfolio-Assessment

## 📚 Kursstruktur (7 Wochen + 23 Interactive Apps)

> 🌟 **Highlight**: Das **"Big 3" Notebook** in Woche 4 bietet eine umfassende praktische Einführung in Decision Trees, K-Nearest Neighbors und K-Means Clustering - die drei wichtigsten ML-Algorithmen!

| Woche | Thema | Notebooks | Apps | Hauptinhalte |
|-------|-------|-----------|------|--------------|
| **01** | [Python Grundlagen](./01_Python_Grundlagen/) | 3 | 0 | Python in 3 Stunden, Docker, Glossar |
| **02** | [Streamlit & Pandas](./02_Streamlit_und_Pandas/) | 1 | 1 | Web-Apps, Datenanalyse |
| **03** | [Machine Learning](./03_Machine_Learning/) | 1 | 0 | ML in Streamlit, Klassifikation |
| **04** | [Advanced Algorithms](./04_Advanced_Algorithms/) | 1 | 0 | Decision Trees, KNN, K-Means Clustering |
| **05** | [Neural Networks](./05_Neural_Networks/) | 1 | 1 | Neural Networks in Streamlit |
| **06** | [Computer Vision & NLP](./06_Computer_Vision_NLP/) | 4 | 4 | CNNs, Transfer Learning, CV Apps |
| **07** | [Deployment & Portfolio](./07_Deployment_Portfolio/) | 4 | 2 | MLOps, Cloud, APIs, NLP |

**📊 Gesamt: 15 Notebooks + 8 Streamlit Apps = 23 Portfolio-Komponenten**

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
# MLflow: http://localhost:5001
```

### Lokal
```bash
# Dependencies installieren
pip install -r requirements.txt

# Jupyter starten
jupyter notebook

# Streamlit Apps starten
cd 02_Streamlit_und_Pandas
streamlit run app.py
```

## 🎯 Lernziele

Nach dem Kurs kannst du:

- ✅ **Python für Data Science** professionell einsetzen
- ✅ **8 Interactive Web-Apps** mit Streamlit entwickeln  
- ✅ **Machine Learning Pipelines** erstellen und deployen
- ✅ **Neural Networks & Computer Vision** implementieren
- ✅ **Modern NLP** mit Transformers und Hugging Face
- ✅ **MLOps Pipelines** für Production-Deployment
- ✅ **Portfolio-Projekte** für Bewerbungen präsentieren
- ✅ **Cloud Deployment** für echte Nutzer

## 🏆 Bewertung (Fallstudie statt Klausur)

### 📋 Prüfungsleistung: MLOps-Fallstudie

Die **Fallstudie** ist die offizielle Prüfungsleistung laut IU Modulbeschreibung. In diesem Kurs bedeutet das konkret:

🎯 **Entwicklung einer produktionsreifen MLOps-App mit Streamlit**
- End-to-End Machine Learning Pipeline
- Interactive Web-App mit Streamlit
- **Deployment in die Streamlit Cloud** (öffentlich zugänglich)
- Professional Documentation & GitHub Repository

Die Fallstudie zeigt, dass du nicht nur ML-Algorithmen verstehst, sondern auch **echte Business-Anwendungen** entwickeln kannst, die von realen Nutzern verwendet werden können.

### 💡 Beispiele für Fallstudien

> 🎯 **Maximale Freiheit**: Diese sind nur Inspirationen! Wähle ein Thema, das dich interessiert - ideal als **Vorstudie für dein Bachelorprojekt**.

**Beispiel 1: Predictive Analytics** 📈
- Hauspreisvorhersage mit Interactive Dashboard
- Upload eigener Immobiliendaten
- Live-Deployment: `https://deine-app.streamlit.app`

**Beispiel 2: Computer Vision** 👁️
- Bildklassifikation (Medical Images, Produkterkennung)
- Drag & Drop Interface für Bilder
- Real-time Predictions mit CNNs

**Beispiel 3: NLP & Text Analytics** 📝
- Sentiment Analysis für Social Media
- Text-to-Insights Dashboard
- Multi-Language Support

**Beispiel 4: Business Intelligence** 💼
- Sales Forecasting Dashboard
- Interactive KPI Monitoring
- Automated Report Generation

**Deine eigene Idee?** 🚀 Entwickle etwas, das zu deinen Karrierezielen passt!

### 📊 Big Data Quellen für deine Fallstudie

**Öffentliche Datensätze (kostenlos & legal):**

🌍 **Allgemeine Datenportale**
- [Kaggle Datasets](https://www.kaggle.com/datasets) - Millionen von Datensätzen + Competitions
- [Google Dataset Search](https://datasetsearch.research.google.com/) - Google's Datensuche
- [AWS Open Data](https://registry.opendata.aws/) - Amazon's öffentliche Datensätze
- [Data.gov](https://data.gov/) - US Regierungsdaten
- [European Data Portal](https://data.europa.eu/) - EU Datensätze

🏢 **Business & Finance**
- [Yahoo Finance API](https://finance.yahoo.com/) - Aktienkurse & Finanzdaten
- [World Bank Open Data](https://data.worldbank.org/) - Wirtschaftsdaten weltweit
- [IMF Data](https://data.imf.org/) - Internationale Wirtschaftsstatistiken

🧬 **Science & Research**
- [UCI ML Repository](https://archive.ics.uci.edu/ml/) - Klassische ML Datensätze
- [Papers with Code](https://paperswithcode.com/datasets) - Research Datasets
- [NASA Open Data](https://data.nasa.gov/) - Weltraumdaten

🎬 **Social Media & Entertainment**
- [MovieLens](https://grouplens.org/datasets/movielens/) - Film-Bewertungen
- [Spotify API](https://developer.spotify.com/documentation/web-api/) - Musikdaten
- [Reddit API](https://www.reddit.com/dev/api/) - Social Media Analytics

**💡 Tipp**: Wähle Daten aus einem Bereich, der dich interessiert - das macht die Fallstudie authentischer!

Alle Apps müssen **live deployed** und **öffentlich zugänglich** sein!

### 📊 Bewertungsschema

| Komponente | Gewichtung | Beschreibung |
|------------|------------|--------------|
| **Fallstudie** | 80% | MLOps-App: Jupyter Notebook + Streamlit-App + **Live-Deployment** (Streamlit Cloud) |
| **Präsentation** | 20% | Live-Demo der deployed App + Erklärung der Implementierung (15 Min) |

## 📊 Technischer Stack

### Core Technologies
- 🐍 **Python 3.11+** - Programmiersprache
- 📊 **Pandas & NumPy** - Datenverarbeitung
- 🤖 **Scikit-learn** - Machine Learning
- 🧠 **TensorFlow/Keras** - Deep Learning
- 🤗 **Hugging Face** - Modern NLP & Transformers
- 🚀 **Streamlit** - Interactive Web-Apps
- 🐳 **Docker** - Containerized Development
- 🎬 **Original AMALEA Videos** - KIT 2021 Integration

### Deployment & Tools
- ☁️ **Streamlit Cloud** - App Hosting
- 🔧 **FastAPI** - ML API Development
- 🐙 **GitHub** - Version Control + CI/CD
- 📈 **Plotly & Matplotlib** - Visualisierungen
- 🔧 **VS Code** - Development Environment
- 📊 **MLflow** - Experiment Tracking

## 8 Portfolio-Projekte (Production-Ready)

### Current Web Applications
1. **Streamlit Pandas Demo** (02_Streamlit_und_Pandas/example_app.py)
2. **Neural Network Playground** (05_Neural_Networks/neural_network_playground.py)
3. **CNN Filter Explorer** (06_Computer_Vision_NLP/06_01_streamlit_cnn_filter.py)
4. **Computer Vision Apps** (06_Computer_Vision_NLP/06_02_streamlit_cv_apps.py)
5. **Data Augmentation Studio** (06_Computer_Vision_NLP/06_03_streamlit_data_augmentation.py)
6. **Transfer Learning Hub** (06_Computer_Vision_NLP/06_04_streamlit_transfer_learning.py)
7. **MLOps Dashboard** (07_Deployment_Portfolio/07_01_streamlit_mlops_dashboard.py)
8. **NLP Dashboard** (07_Deployment_Portfolio/07_02_streamlit_nlp_dashboard.py)

## 📁 Repository-Struktur

```
amalea/
├── 📂 01_Python_Grundlagen/           # Python Basics & Pandas (3 Notebooks)
│   ├── 📓 00_Python_in_3_Stunden.ipynb
│   ├── 📓 01_Pandas_Grundlagen.ipynb
│   ├── 📓 02_Datenanalyse_Vertiefung.ipynb
│   └── 📁 data/
├── 📂 02_Streamlit_und_Pandas/        # Web-Apps & Datenanalyse (1 Notebook + 1 App)
│   ├── 📓 01_Streamlit_Dashboard.ipynb
│   ├── 🚀 example_app.py
│   └── 📁 data/
├── 📂 03_Machine_Learning/            # ML Grundlagen (1 Notebook)
│   ├── 📓 01_ML_in_Streamlit.ipynb
│   └── 📁 data/
├── 📂 04_Advanced_Algorithms/         # "Big 3" Algorithmen (1 Notebook)
│   ├── 📓 01_Bäume_Nachbarn_Clustering.ipynb
│   └── 📁 data/
├── 📂 05_Neural_Networks/             # Deep Learning (1 Notebook + 1 App)
│   ├── 📓 01_Neural_Networks.ipynb
│   ├── 🚀 neural_network_playground.py
│   └── 📁 data/
├── 📂 06_Computer_Vision_NLP/         # CV & NLP (4 Notebooks + 4 Apps)
│   ├── 📓 01_CNNs_und_Bildverarbeitung.ipynb
│   ├── 📓 02_Transfer_Learning.ipynb
│   ├── 📓 03_Data_Augmentation.ipynb
│   ├── 📓 04_Computer_Vision_Apps.ipynb
│   ├── 🚀 06_01_streamlit_cnn_filter.py
│   ├── 🚀 06_02_streamlit_cv_apps.py
│   ├── 🚀 06_03_streamlit_data_augmentation.py
│   ├── 🚀 06_04_streamlit_transfer_learning.py
│   └── 📁 data/
├── 📂 07_Deployment_Portfolio/        # MLOps & Production (4 Notebooks + 2 Apps)
│   ├── 📓 01_MLOps_Grundlagen.ipynb
│   ├── 📓 02_Cloud_Deployment.ipynb
│   ├── 📓 03_API_Development.ipynb
│   ├── 📓 04_NLP_Transformers.ipynb
│   ├── 🚀 07_01_streamlit_mlops_dashboard.py
│   ├── 🚀 07_02_streamlit_nlp_dashboard.py
│   └── 📁 data/
├── 📦 archive/                        # Original AMALEA Content
├── 📚 docs/                          # Dokumentation & Status
├── 🎥 Kurs-Videos/                   # 22 Original Videos
├── 🐳 docker-compose.yml
├── 📋 requirements.txt
├── 🚫 .gitignore
└── ⚙️ .gitattributes
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
pip install -r requirements.txt

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

1. **Starte mit [01_Python_Grundlagen](./01_Python_Grundlagen/) (Woche 1)**
2. **Arbeite dich chronologisch durch die Wochen**
3. **Experimentiere mit den Streamlit-Apps**
4. **Erstelle dein eigenes Portfolio-Projekt**

**Ziel**: Am Ende des Kurses hast du **8 deployed ML-Apps + 15 Notebooks** in deinem Portfolio! 🚀

> **Portfolio-Highlight**: Alle Apps sind production-ready und können direkt in Bewerbungen verwendet werden.

---

*AMALEA 2025 - Fully Modernized for Industry-Ready Data Scientists* ✨
