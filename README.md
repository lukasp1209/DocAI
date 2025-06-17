# 🎓 AMALEA 2025 - Data Analytics & Big Data

**Modernisierter Kurs für IU Studierende - 5. Semester**

> 🚀 **Vollständig modernisiert**: 13 Notebooks + 8 Streamlit Apps + Docker + Portfolio-Assessment

## 📚 Kursstruktur (7 Wochen + 13 Interactive Apps)

| Woche | Thema | Notebooks | Apps | Hauptinhalte |
|-------|-------|-----------|------|--------------|
| **01** | [Python Grundlagen](./01_Python_Grundlagen/) | 3 | 0 | Python Crashkurs, Docker, Glossar |
| **02** | [Streamlit & Pandas](./02_Streamlit_und_Pandas/) | 1 | 1 | Web-Apps, Datenanalyse |
| **03** | [Machine Learning](./03_Machine_Learning/) | 1 | 0 | Iris Klassifikation, ML Pipeline |
| **04** | [Advanced Algorithms](./04_Advanced_Algorithms/) | 1 | 0 | Trees, KNN, Clustering |
| **05** | [Neural Networks](./05_Neural_Networks/) | 1 | 1 | Deep Learning, Backpropagation |
| **06** | [Computer Vision & NLP](./06_Computer_Vision_NLP/) | 4 | 4 | CNNs, Transfer Learning, CV Apps |
| **07** | [Deployment & Portfolio](./07_Deployment_Portfolio/) | 2 | 2 | MLOps, Cloud, APIs, NLP |

**📊 Gesamt: 13 Notebooks + 8 Streamlit Apps = 21 Portfolio-Komponenten**

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

| Komponente | Gewichtung | Beschreibung |
|------------|------------|--------------|
| **Fallstudie** | 80% | End-to-End ML Projekt mit Deployment (Jupyter Notebook + Streamlit-App) |
| **Präsentation** | 20% | Präsentation (15 Min) |

## 📊 Technischer Stack

### Core Technologies
- 🐍 **Python 3.11+** - Programmiersprache
- 📊 **Pandas & NumPy** - Datenverarbeitung
- 🤖 **Scikit-learn** - Machine Learning
- 🧠 **TensorFlow/Keras** - Deep Learning
- 🤗 **Hugging Face** - Modern NLP & Transformers
- 🚀 **Streamlit** - Interactive Web-Apps
- 🐳 **Docker** - Containerized Development

### Deployment & Tools
- ☁️ **Streamlit Cloud** - App Hosting
- � **FastAPI** - ML API Development
- �🐙 **GitHub** - Version Control + CI/CD
- 📈 **Plotly & Matplotlib** - Visualisierungen
- 🔧 **VS Code** - Development Environment
- 📊 **MLflow** - Experiment Tracking

## 🛠️ 8 Portfolio-Projekte (Production-Ready)

### Current Web Applications
1. **Streamlit Basics** (02_Streamlit_und_Pandas/example_app.py)
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
├── 01_Python_Grundlagen/              # Python Basics + Docker Setup
│   ├── 01_01_Python_Crashkurs.ipynb
│   ├── 01_02_Data_Types_und_Strukturen.ipynb
│   └── 2 Streamlit Apps
├── 02_Streamlit_und_Pandas/           # Web-Apps + Data Analysis
│   ├── 02_01_Pandas_Grundlagen.ipynb
│   ├── 02_02_Streamlit_Einführung.ipynb
│   └── 2 Streamlit Apps
├── 03_Machine_Learning/               # ML Fundamentals
│   ├── 03_01_Iris_Klassifikation.ipynb
│   ├── 03_02_Evaluation_und_Metriken.ipynb
│   └── 1 Streamlit App
├── 04_Advanced_Algorithms/            # Trees, KNN, Clustering
│   ├── 04_01_Decision_Trees.ipynb
│   ├── 04_02_KNN_und_Clustering.ipynb
│   ├── 04_03_Unsupervised_Learning.ipynb
│   └── 1 Streamlit App
├── 05_Neural_Networks/                # Deep Learning
│   ├── 05_01_Neural_Network_Grundlagen.ipynb
│   ├── 05_02_Backpropagation.ipynb
│   └── 1 Streamlit App
├── 06_Computer_Vision_NLP/            # CNNs + Modern CV/NLP
│   ├── 06_01_CNN_Grundlagen.ipynb
│   ├── 06_02_Computer_Vision_Anwendungen.ipynb
│   ├── 06_03_Data_Augmentation.ipynb
│   ├── 06_04_Transfer_Learning.ipynb
│   └── 4 Streamlit Apps
├── 07_Deployment_Portfolio/           # MLOps + Production
│   ├── 07_01_MLOps_und_Deployment.ipynb
│   ├── 07_02_NLP_und_Text_Generation.ipynb
│   └── 2 Streamlit Apps
├── BACKUP_Original_AMALEA_Notebooks/  # Original Content Preserved
├── requirements.txt                    # Python Dependencies
├── docker-compose.yml                 # Development Environment
└── README.md                          # This file
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

1. **Starte mit [01_Python_Grundlagen](./01_Python_Grundlagen/)**
2. **Arbeite dich chronologisch durch die Wochen**
3. **Experimentiere mit den Streamlit-Apps**
4. **Erstelle dein eigenes Portfolio-Projekt**

**Ziel**: Am Ende des Kurses hast du **8 deployed ML-Apps + 13 Notebooks** in deinem Portfolio! 🚀

> **Portfolio-Highlight**: Alle Apps sind production-ready und können direkt in Bewerbungen verwendet werden.

---

*AMALEA 2025 - Fully Modernized for Industry-Ready Data Scientists* ✨
