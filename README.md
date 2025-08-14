# 🎓 AMALEA 2025 - Data Analytics & Big Data

**Modernisierter Kurs für IU Studierende - 5. Semester**

> 🚀 **Vollständig modernisiert**: 16 Core Notebooks + 8 Streamlit Apps + QUA³CK Framework + MLOps Integration

---

## 📑 Inhaltsverzeichnis

<!-- markdownlint-disable MD051 MD007 MD032 MD004 -->
* [AMALEA Framework Integration](#-amalea-framework-integration)
* [Modernisierte Kursstruktur (2025)](#-modernisierte-kursstruktur-2025)
* [Quick Start](#-quick-start)
* [OS-agnostischer Setup-Guide](#-os-agnostischer-setup-guide-macos--windows--linux)
* [Technischer Stack](#-technischer-stack)
* [8 Portfolio-Projekte](#8-portfolio-projekte-production-ready)
* [Repository-Struktur](#-repository-struktur)
* [Docker Aufräumen (Cleanup)](#-docker-aufräumen-cleanup)
* [Troubleshooting](#-troubleshooting)
* [Zusätzliche Ressourcen](#-zusätzliche-ressourcen)
* [Support](#-support)
* [Los gehts](#-los-gehts)
<!-- markdownlint-enable MD051 MD007 MD032 MD004 -->




## 🎯 AMALEA Framework Integration

**AMALEA** steht für **"Angewandte Machine Learning Algorithmen"** und kombiniert:
* **📚 Theoretische Fundamente** - QUA³CK Prozessmodell als Struktur
* **🛠️ Praktische Umsetzung** - Hands-on Coding mit modernsten Tools
* **☁️ Cloud Deployment** - Production-ready Streamlit Apps

### 🔄 QUA³CK Prozessmodell (Integrated)
Jedes Portfolio-Projekt folgt dem systematischen **QUA³CK Framework**:
- **Q**uestion: Business Problem Definition
- **U**nderstand: Data Exploration & Analysis
- **A**cquire & Clean: Data Preparation & Processing
- **A**nalyze: Model Development & Evaluation
- **A**pp: Interactive Streamlit Application
- **C**onclusion & **K**ommunikation: Portfolio Documentation

## 📚 Modernisierte Kursstruktur (2025)

> 🌟 **QUA³CK Integration**: Alle Notebooks folgen dem strukturierten 6-Phasen-Prozessmodell  
> 🎥 **22 Original AMALEA Videos**: Systematisch in moderne Notebooks integriert  
> 🏆 **MLOps Standards**: Professional Model Development mit MLFlow Tracking

| Woche | Thema | Core Notebooks | Apps | QUA³CK Focus |
|-------|-------|----------------|------|--------------|
| **01** | [Python Grundlagen](./01_Python_Grundlagen/) | 4 | 0 | Foundation + QUA³CK Intro |
| **02** | [Streamlit & Pandas](./02_Streamlit_und_Pandas/) | 1 | 1 | Interactive Apps Development |
| **03** | [Machine Learning](./03_Machine_Learning/) | 1 | 0 | ML Pipeline mit QUA³CK |
| **04** | [Advanced Algorithms](./04_Advanced_Algorithms/) | 2 | 0 | Big 3 + MLOps Integration |
| **05** | [Neural Networks](./05_Neural_Networks/) | 1 | 1 | Deep Learning Foundations |
| **06** | [Computer Vision & NLP](./06_Computer_Vision_NLP/) | 4 | 4 | CV/NLP mit Transfer Learning |
| **07** | [Deployment & Portfolio](./07_Deployment_Portfolio/) | 3 | 2 | MLOps + Cloud Deployment |

**📊 Gesamt: 16 Core Notebooks + 8 Streamlit Apps + 13 Archive Notebooks = 37 Notebooks**

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

#### Leichtgewichtig starten (Slim Images)

Für schnellen Start ohne schwere Deep-Learning-Stacks (TF/Torch/OpenCV)
gibt es schlanke Images. Die Full-Services bleiben unverändert.

```bash
# Nur die schlanken Services starten
docker compose up -d jupyter-lab-slim streamlit-slim

# Oder alles starten (Full + Slim)
docker compose up -d
```

- Jupyter Slim: [http://localhost:8889](http://localhost:8889)
- Streamlit Slim: [http://localhost:8502](http://localhost:8502)

Hinweis: Der Slim-Streamlit-Service startet direkt die MC-Test-App
(`01_Python_Grundlagen/mc_test_app.py`).

Wechsle zu den Full-Services, wenn du TensorFlow, PyTorch, OpenCV oder
große NLP-Modelle brauchst.

#### Streamlit Apps richtig starten (Docker)

Nutze für zusätzliche Apps die vorhandenen Streamlit-Container – nicht den
Jupyter-Container. Beispiel (Full Image):

```bash
docker compose exec streamlit-dev streamlit run \
  /app/01_Python_Grundlagen/uebungs_app.py
```

Slim-Variante (Port 8502):

```bash
docker compose exec streamlit-slim streamlit run \
  /app/01_Python_Grundlagen/uebungs_app.py --server.port 8501
```

Parallel mehrere Apps? Nutze unterschiedliche Ports und mappe sie bei Bedarf
im compose (z. B. 8503):

```bash
docker compose exec streamlit-dev streamlit run \
  /app/02_Streamlit_und_Pandas/example_app.py --server.port 8503
```

Warum nicht im Jupyter-Container? Dort ist Port 8501 nicht exponiert; das
führt zu Meldungen wie "Did not auto detect external IP." (harmlos, aber
ohne Host-Zugriff). Wenn du es trotzdem brauchst, füge einen Port-Mapping
hinzu und starte mit `--server.address=0.0.0.0`.


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

#### Virtuelle Umgebung (lokal)

Wenn du ohne Docker lokal arbeitest, empfiehlt sich eine virtuelle Umgebung
zur sauberen Isolation der Python-Pakete.

```bash
# venv anlegen und aktivieren (macOS/Linux)
python3 -m venv .venv
source .venv/bin/activate

# Tools aktualisieren und Dependencies installieren
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# (Optional) Jupyter-Kernel registrieren
python -m ipykernel install --user --name amalea-venv \
  --display-name "Python (amalea)"

# Deaktivieren
deactivate
```

Hinweis: Wenn du Docker (compose) nutzt, ist keine lokale venv nötig –
alles läuft im Container.

## 🧭 OS-agnostischer Setup-Guide (macOS · Windows · Linux)

Diese Entwicklungsumgebung ist plattformunabhängig. Alles läuft in
Containern; keine Host-spezifischen Skripte.

- Voraussetzungen
  - macOS: Docker Desktop (File Sharing für den Projektordner erlauben)
  - Windows 10/11: Docker Desktop mit WSL2-Backend; Projektordner in einem
    WSL-Pfad ablegen (z. B. \\wsl$ oder `~/` in Ubuntu-WSL)
  - Linux: Docker Engine und Docker Compose v2 (plugin)

- Starten/Stoppen
  - Start: `docker compose up -d`
  - Logs: `docker compose logs -f --tail=100`
  - Stoppen: `docker compose down`

- Ports (frei halten)
  - Jupyter: 8888
  - Streamlit: 8501
  - MLflow: 5001 (Container-Port 5000)
  - Postgres: 5432
  - Jupyter Slim: 8889
  - Streamlit Slim: 8502

- Volumes und Mounts
  - Projektordner als Bind-Mount:
    - Streamlit: `./:/app`
    - Jupyter: `./:/workspace`
  - Benannte Volumes: `jupyter-data`, `mlflow-data`, `postgres-data`
  - Postgres-Init:
    - `./datasets` wird nach `/docker-entrypoint-initdb.d` gemountet
    - Ordner muss existieren

- Umgebungsvariablen
  - `.env` im Repo-Root wird automatisch von Compose geladen
  - Beispiel: `MC_TEST_ADMIN_KEY=Admin` (Admin-Ansicht in der MC-Test-App)
  - Vorlage: `.env.example` → kopiere zu `.env` und passe Werte an

- macOS: Docker Desktop File Sharing
  - Öffne Docker Desktop → Settings → Resources → File Sharing
  - Füge den Projektordner hinzu: `/Users/kqc/amalea`
  - Apply & Restart, danach `docker compose up -d` erneut ausführen
  - Hinweis: Wenn du Ordner außerhalb des Repos mountest, diese Pfade
    zusätzlich freigeben

- Häufige Stolpersteine
  - Portkonflikte: 8501/8888/5001/5432 müssen frei sein
  - Datei-Freigabe (macOS/Windows): Projektordner in Docker Desktop freigeben
  - Windows/WSL2: Besser in einem WSL-Dateipfad arbeiten (I/O-Performance)
  - Live-Reload: Auf macOS/Windows sind Dateievents teils verzögert;
    in Streamlit ggf. manuell neu laden
Nach dem Kurs beherrschen Sie:

### 🔬 **Technical Excellence**

- ✅ **QUA³CK Framework** für systematische Data Science Projekte
- ✅ **Python für Data Science** mit modernen Libraries (Pandas 2.2+, Scikit-learn 1.4+)
- ✅ **MLOps Best Practices** mit MLFlow Experiment Tracking
- ✅ **Neural Networks & Computer Vision** mit TensorFlow 2.15+
- ✅ **Modern NLP** mit Hugging Face Transformers
- ✅ **Big 3 Algorithmen** (Decision Trees, KNN, K-Means) professionell

### 🚀 **Portfolio Development**

- ✅ **7 Production-Ready Streamlit Apps** für Cloud Deployment
- ✅ **Interactive Web-Applications** mit Real-time Parameter Tuning
- ✅ **Professional Documentation** nach QUA³CK Standards
- ✅ **GitHub Portfolio** mit Industry-Standard Code Quality
- ✅ **Streamlit Cloud Deployment** für öffentliche App-Präsentation

### 💼 **Career Readiness**

- ✅ **Industry-Standard Tools** (MLFlow, Docker, Cloud Platforms)
- ✅ **Business Problem Solving** mit Data Science Methodologies
- ✅ **Professional Presentation** für Job Interviews

### 📋 AMALEA Portfolio-Fallstudie

Die **Fallstudie** folgt dem aktualisierten **QUA³CK Prozessmodell** und demonstriert vollständige Data Science Kompetenz:

🎯 **QUA³CK-basierte MLOps-Portfolio-Entwicklung**

- **Q**uestion: Business Problem Definition & Stakeholder Analysis
- **U**nderstand: Comprehensive Data Exploration & EDA
- **A**cquire & Clean: Professional Data Pipeline Development
- **A**nalyze: Machine Learning Model Development mit MLFlow Tracking
- **A**pp: **Production-Ready Streamlit Cloud Deployment**
- **C**&**K**: Professional Documentation & Portfolio Presentation

### 💡 AMALEA Portfolio-Beispiele (QUA³CK-strukturiert)

> 🎯 **Maximale Freiheit**: Wählen Sie ein Thema aus Ihrem Interessensbereich - ideal als **Vorstudie für das Bachelorprojekt**!

**Beispiel 1: Predictive Analytics mit QUA³CK** 📈

- **Q**: Immobilienpreis-Vorhersage für Makler-Unterstützung
- **U**: Marktdaten-Analyse mit modernen Visualisierungen
- **A**: Automated Data Pipeline mit Outlier Detection
- **A**: Random Forest + XGBoost mit MLFlow Experiment Tracking
- **A**: Interactive Dashboard → `https://deine-immobilien-app.streamlit.app`
- **C&K**: ROI-Analysis und Business Impact Documentation

**Beispiel 2: Computer Vision mit Transfer Learning** 👁️

- **Q**: Medical Image Classification für Diagnostik-Support
- **U**: DICOM Dataset Analysis mit Privacy Considerations
- **A**: Data Augmentation + Preprocessing Pipeline
- **A**: EfficientNet Transfer Learning mit Hugging Face
- **A**: Drag & Drop Interface → `https://deine-medical-cv.streamlit.app`
- **C&K**: Clinical Validation und Ethical AI Documentation

**Beispiel 3: NLP & Sentiment Analysis** 📝

- **Q**: Social Media Brand Monitoring für Marketing Teams
- **U**: Twitter/Reddit Data mit Trend Analysis
- **A**: Text Preprocessing + Multi-language Support
- **A**: BERT Fine-tuning mit Transformer Pipelines
- **A**: Real-time Dashboard → `https://deine-sentiment-app.streamlit.app`
- **C&K**: Marketing Strategy Recommendations

**Ihre eigene AMALEA-Idee?** 🚀 Entwickeln Sie ein QUA³CK-Portfolio für Ihre Karriereziele!

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

**💡 Tipp**: Wähle Daten aus einem Bereich, der dich interessiert - das macht
die Fallstudie authentischer!

Alle Apps müssen **live deployed** und **öffentlich zugänglich** sein!

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
7. **MLOps Dashboard** (07_Deployment_Portfolio/04_streamlit_mlops_dashboard.py)
8. **NLP Dashboard** (07_Deployment_Portfolio/05_streamlit_nlp_dashboard.py)

## 📁 Repository-Struktur

```text
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
├── 🐳 docker-compose.yml
├── 📋 requirements.txt
├── 🚫 .gitignore
└── ⚙️ .gitattributes
```

## 🧹 Docker aufräumen (Cleanup)

Wenn Sie Platz freigeben möchten, können Sie ungenutzte Ressourcen
entfernen. Achtung: Der zweite Befehl löscht auch unbenutzte Volumes
(Datenverlust möglich).

```bash
# Unbenutzte Container, Netzwerke und Images entfernen
docker system prune -f

# Optional: inklusive ungenutzter Volumes
docker system prune -a --volumes -f
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

**Ziel**: Am Ende des Kurses hast du **8 deployed ML-Apps + 16 Notebooks**
in deinem Portfolio! 🚀

> **Portfolio-Highlight**: Alle Apps sind production-ready und können
> direkt in Bewerbungen verwendet werden.

---

*AMALEA 2025 - Fully Modernized for Industry-Ready Data Scientists* ✨
