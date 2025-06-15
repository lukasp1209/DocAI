# 🎓 AMALEA 2025 - Data Analytics & Big Data

**Modernisierter Kurs für IU Studierende - 5. Semester**

> 🚀 **Vollständig modernisiert**: 15 Notebooks + 13 Streamlit Apps + Docker + Portfolio-Assessment

## 📚 Kursstruktur (7 Wochen + 13 Interactive Apps)

| Woche | Thema | Notebooks | Apps | Hauptinhalte |
|-------|-------|-----------|------|--------------|
| **01** | [Python Grundlagen](./01_Python_Grundlagen/) | 2 | 2 | Python Crashkurs, Docker, Glossar |
| **02** | [Streamlit & Pandas](./02_Streamlit_und_Pandas/) | 2 | 2 | Web-Apps, Datenanalyse |
| **03** | [Machine Learning](./03_Machine_Learning/) | 2 | 1 | Iris Klassifikation, ML Pipeline |
| **04** | [Advanced Algorithms](./04_Advanced_Algorithms/) | 3 | 1 | Trees, KNN, Clustering |
| **05** | [Neural Networks](./05_Neural_Networks/) | 2 | 1 | Deep Learning, Backpropagation |
| **06** | [Computer Vision & NLP](./06_Computer_Vision_NLP/) | 4 | 4 | CNNs, Transfer Learning, CV Apps |
| **07** | [Deployment & Portfolio](./07_Deployment_Portfolio/) | 2 | 2 | MLOps, Cloud, APIs, NLP |

**📊 Gesamt: 15 Notebooks + 13 Streamlit Apps = 28 Portfolio-Komponenten**

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
- ✅ **13 Interactive Web-Apps** mit Streamlit entwickeln  
- ✅ **Machine Learning Pipelines** erstellen und deployen
- ✅ **Neural Networks & Computer Vision** implementieren
- ✅ **Modern NLP** mit Transformers und Hugging Face
- ✅ **MLOps Pipelines** für Production-Deployment
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

## 🛠️ 13 Portfolio-Projekte (Production-Ready)

### Fundamentals (Wochen 1-3)
1. **Python Basics Explorer** - Interactive Python Learning
2. **Data Types Playground** - Hands-on Python Fundamentals  
3. **Pandas Data Explorer** - CSV Upload + Advanced Analytics
4. **Streamlit Portfolio Builder** - Personal Portfolio Creator
5. **ML Model Playground** - Iris Classification + Feature Engineering

### Advanced ML (Wochen 4-5)
6. **Advanced ML Algorithms** - Trees, KNN, Clustering Dashboard
7. **Neural Network Builder** - Interactive Deep Learning Demo

### Computer Vision & NLP (Woche 6)
8. **CNN Filter Explorer** - Convolutional Neural Network Visualization
9. **Computer Vision Apps** - Image Processing + Object Detection
10. **Data Augmentation Studio** - Image Enhancement Pipeline
11. **Transfer Learning Hub** - Pre-trained Model Fine-tuning

### Production Deployment (Woche 7)
12. **MLOps Dashboard** - End-to-End ML Pipeline Monitoring
13. **NLP Dashboard** - Modern Text Analysis with Transformers

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
├── requirements-2025.txt              # Python Dependencies
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

**Ziel**: Am Ende des Kurses hast du **13 deployed ML-Apps** in deinem Portfolio! 🚀

> **Portfolio-Highlight**: Alle Apps sind production-ready und können direkt in Bewerbungen verwendet werden.

---

*AMALEA 2025 - Fully Modernized for Industry-Ready Data Scientists* ✨
