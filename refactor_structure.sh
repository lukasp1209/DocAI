#!/bin/bash

# 🧹 AMALEA Repository Refactoring Script
# Bereinigt die chaotische Ordnerstruktur und erstellt eine saubere, einheitliche Struktur

echo "🧹 AMALEA Repository Refactoring gestartet..."
echo "=================================="

# Arbeitsverzeichnis setzen
cd "/Users/kqc/Dropbox/Vorlesungen/13. IU - Data Analytics und Big Data/amalea"

# Backup erstellen
echo "📦 Erstelle Backup der aktuellen Struktur..."
if [ ! -d "BACKUP_vor_refactoring" ]; then
    mkdir "BACKUP_vor_refactoring"
    cp -r "Woche"* "BACKUP_vor_refactoring/" 2>/dev/null || true
fi

echo "✅ Backup erstellt in BACKUP_vor_refactoring/"

# 1. Erstelle neue, saubere Ordnerstruktur
echo ""
echo "🏗️ Erstelle neue Ordnerstruktur..."

# Zielordner erstellen
mkdir -p "01_Python_Grundlagen"
mkdir -p "02_Streamlit_und_Pandas" 
mkdir -p "03_Machine_Learning"
mkdir -p "04_Advanced_Algorithms"
mkdir -p "05_Neural_Networks"
mkdir -p "06_Computer_Vision_NLP"
mkdir -p "07_Deployment_Portfolio"

echo "✅ Neue Ordnerstruktur erstellt"

# 2. Modernisierte Inhalte in neue Struktur verschieben
echo ""
echo "📁 Verschiebe modernisierte Inhalte..."

# Woche 0 → 01_Python_Grundlagen
if [ -d "Woche 0 - Python Quickstart" ]; then
    echo "   📦 Woche 0 → 01_Python_Grundlagen"
    cp -r "Woche 0 - Python Quickstart"/* "01_Python_Grundlagen/"
    
    # README für den neuen Ordner
    cat > "01_Python_Grundlagen/README.md" << 'EOF'
# 🐍 01 Python Grundlagen

**Einstieg in Python für Data Science - Kein Vorwissen erforderlich**

## 📚 Inhalt

- `00_Python_in_3_Stunden.ipynb` - Python Crashkurs für Anfänger
- `01_Docker_für_Data_Science.ipynb` - Entwicklungsumgebung setup
- `02_Glossar_Alle_Begriffe_erklärt.ipynb` - Alle wichtigen Begriffe

## 🎯 Lernziele

Nach dieser Woche kannst du:
- ✅ Python Grundlagen (Variablen, Listen, Funktionen)
- ✅ Jupyter Notebooks effektiv nutzen
- ✅ Docker für reproduzierbare Umgebungen
- ✅ Alle Data Science Begriffe verstehen

## 🚀 Start

```bash
# Docker starten
docker-compose up

# Oder lokal mit Jupyter
jupyter notebook
```
EOF
fi

# Woche 1 → 02_Streamlit_und_Pandas  
if [ -d "Woche 1 - Neu" ]; then
    echo "   📦 Woche 1 → 02_Streamlit_und_Pandas"
    cp -r "Woche 1 - Neu"/* "02_Streamlit_und_Pandas/"
    
    # Zusätzlich prüfen ob es bessere Inhalte in anderen Woche 1 Ordnern gibt
    if [ -d "Woche_1_Streamlit_Basics" ]; then
        cp -r "Woche_1_Streamlit_Basics"/* "02_Streamlit_und_Pandas/" 2>/dev/null || true
    fi
    
    cat > "02_Streamlit_und_Pandas/README.md" << 'EOF'
# 🚀 02 Streamlit und Pandas

**Interaktive Web-Apps und Datenanalyse**

## 📚 Inhalt

- `01_Erste_Streamlit_App_fixed.ipynb` - Streamlit Grundlagen
- Pandas Datenmanipulation
- Interaktive Visualisierungen

## 🎯 Lernziele

- ✅ Streamlit Apps erstellen
- ✅ Pandas für Datenanalyse
- ✅ Interaktive Dashboards
- ✅ CSV Daten verarbeiten

## 🚀 Start

```bash
streamlit run app.py
```
EOF
fi

# Woche 2 → 03_Machine_Learning
if [ -d "Woche 2 - Neu" ]; then
    echo "   📦 Woche 2 → 03_Machine_Learning"
    cp -r "Woche 2 - Neu"/* "03_Machine_Learning/"
    
    if [ -d "Woche_2_ML_Integration" ]; then
        cp -r "Woche_2_ML_Integration"/* "03_Machine_Learning/" 2>/dev/null || true
    fi
    
    cat > "03_Machine_Learning/README.md" << 'EOF'
# 🤖 03 Machine Learning

**Erste ML-Modelle in Streamlit**

## 📚 Inhalt

- `02_ML_in_Streamlit_fixed.ipynb` - ML Grundlagen
- Iris Klassifikation
- Model Evaluation
- Performance Metriken

## 🎯 Lernziele

- ✅ Supervised Learning verstehen
- ✅ Klassifikation vs. Regression
- ✅ Model Training und Evaluation
- ✅ ML-Pipelines in Streamlit

## 🚀 Start

```bash
jupyter notebook
streamlit run ml_app.py
```
EOF
fi

# Woche 3 → 04_Advanced_Algorithms
if [ -d "Woche 3 - Neu" ]; then
    echo "   📦 Woche 3 → 04_Advanced_Algorithms"
    cp -r "Woche 3 - Neu"/* "04_Advanced_Algorithms/"
    
    if [ -d "Woche_3_Algorithmen" ]; then
        cp -r "Woche_3_Algorithmen"/* "04_Advanced_Algorithms/" 2>/dev/null || true
    fi
    
    cat > "04_Advanced_Algorithms/README.md" << 'EOF'
# 🌳 04 Advanced Algorithms

**Decision Trees, KNN, Clustering**

## 📚 Inhalt

- `03_Bäume_Nachbarn_und_Clustering.ipynb` - Algorithm Deep Dive
- Decision Trees verstehen
- K-Nearest Neighbors
- K-Means Clustering

## 🎯 Lernziele

- ✅ Tree-based Algorithms
- ✅ Distance-based Methods
- ✅ Unsupervised Learning
- ✅ Algorithm Selection

## 🚀 Start

```bash
jupyter notebook 03_Bäume_Nachbarn_und_Clustering.ipynb
```
EOF
fi

# Woche 4 → 05_Neural_Networks (bereits gut strukturiert)
if [ -d "Woche_4_Deep_Learning" ]; then
    echo "   📦 Woche 4 → 05_Neural_Networks"
    cp -r "Woche_4_Deep_Learning"/* "05_Neural_Networks/"
fi

# Woche 5 → 06_Computer_Vision_NLP
if [ -d "Woche_5_Advanced_Topics" ]; then
    echo "   📦 Woche 5 → 06_Computer_Vision_NLP"
    cp -r "Woche_5_Advanced_Topics"/* "06_Computer_Vision_NLP/" 2>/dev/null || true
fi

if [ -d "Woche 5" ]; then
    cp -r "Woche 5"/* "06_Computer_Vision_NLP/" 2>/dev/null || true
fi

cat > "06_Computer_Vision_NLP/README.md" << 'EOF'
# 👁️ 06 Computer Vision & NLP

**CNNs, Bildverarbeitung und Text Analysis**

## 📚 Inhalt

- Convolutional Neural Networks
- Image Classification
- Transfer Learning
- Natural Language Processing

## 🎯 Lernziele

- ✅ CNNs verstehen und anwenden
- ✅ Computer Vision Projekte
- ✅ Text Mining Grundlagen
- ✅ Pre-trained Models nutzen

## 🚀 Coming Soon

Wird in Kürze mit modernisierten AMALEA-Inhalten gefüllt.
EOF

# Woche 6 → 07_Deployment_Portfolio
if [ -d "Woche_6_Deployment" ]; then
    echo "   📦 Woche 6 → 07_Deployment_Portfolio"
    cp -r "Woche_6_Deployment"/* "07_Deployment_Portfolio/" 2>/dev/null || true
fi

if [ -d "Woche 6" ]; then
    cp -r "Woche 6"/* "07_Deployment_Portfolio/" 2>/dev/null || true
fi

cat > "07_Deployment_Portfolio/README.md" << 'EOF'
# 🚀 07 Deployment & Portfolio

**Cloud Deployment und Portfolio-Projekte**

## 📚 Inhalt

- Streamlit Cloud Deployment
- Docker Production Setup
- Portfolio-Projekte finalisieren
- GitHub Pages / Heroku

## 🎯 Lernziele

- ✅ Apps in die Cloud deployen
- ✅ Professional Portfolio erstellen
- ✅ CI/CD Grundlagen
- ✅ Präsentationsfähigkeiten

## 🚀 Coming Soon

Wird in Kürze mit modernisierten AMALEA-Inhalten gefüllt.
EOF

echo "✅ Inhalte erfolgreich verschoben"

# 3. Alte, verwirrende Ordner markieren (aber nicht löschen für Sicherheit)
echo ""
echo "🏷️ Markiere alte Ordner als deprecated..."

# Erstelle Deprecated Ordner
mkdir -p "DEPRECATED_alte_struktur"

# Verschiebe alte Ordner (außer Backups und neuen)
for dir in "Woche 1" "Woche 2" "Woche 3" "Woche 4" "Woche 5" "Woche 6" \
           "Woche_0_Grundlagen" "Woche_1_Streamlit_Basics" "Woche_2_ML_Integration" \
           "Woche_3_Algorithmen" "Woche_5_Advanced_Topics" "Woche_6_Deployment"; do
    if [ -d "$dir" ]; then
        echo "   🗂️ $dir → DEPRECATED_alte_struktur/"
        mv "$dir" "DEPRECATED_alte_struktur/" 2>/dev/null || true
    fi
done

# Auch die bereits verwendeten verschieben (nach dem Kopieren)
for dir in "Woche 0 - Python Quickstart" "Woche 1 - Neu" "Woche 2 - Neu" \
           "Woche 3 - Neu" "Woche_4_Deep_Learning"; do
    if [ -d "$dir" ]; then
        echo "   🗂️ $dir → DEPRECATED_alte_struktur/"
        mv "$dir" "DEPRECATED_alte_struktur/" 2>/dev/null || true
    fi
done

echo "✅ Alte Ordner in DEPRECATED_alte_struktur/ verschoben"

# 4. Hauptverzeichnis README aktualisieren
echo ""
echo "📝 Aktualisiere Haupt-README..."

cat > "README.md" << 'EOF'
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
| **06** | [Computer Vision & NLP](./06_Computer_Vision_NLP/) | 🚧 | CNNs, Transfer Learning |
| **07** | [Deployment & Portfolio](./07_Deployment_Portfolio/) | 🚧 | Cloud, CI/CD, Präsentation |

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
EOF

echo "✅ Haupt-README aktualisiert"

# 5. Übersicht der neuen Struktur anzeigen
echo ""
echo "🎉 Refactoring abgeschlossen!"
echo "=================================="
echo ""
echo "📁 Neue, saubere Ordnerstruktur:"
echo ""

# Zeige die neue Struktur
ls -la | grep "^d" | grep -E "0[1-7]_" | awk '{print "   📂 " $NF}'

echo ""
echo "🗂️ Alte Inhalte gesichert in:"
echo "   📦 BACKUP_vor_refactoring/ (komplett)"
echo "   📦 DEPRECATED_alte_struktur/ (alte Ordner)"
echo "   📦 BACKUP_Original_AMALEA_Notebooks/ (ursprüngliche Notebooks)"

echo ""
echo "✅ Repository ist jetzt sauber strukturiert und bereit für Studenten!"
echo ""
echo "🚀 Nächste Schritte:"
echo "   1. git add . && git commit -m 'Refactor: Clean repository structure'"
echo "   2. Teste die neuen Pfade in Docker"
echo "   3. Aktualisiere Links in der Dokumentation"

echo ""
echo "📊 Struktur-Übersicht:"
echo "   01_Python_Grundlagen      → Python Basics (fertig)"
echo "   02_Streamlit_und_Pandas   → Web-Apps (fertig)"  
echo "   03_Machine_Learning       → ML Basics (fertig)"
echo "   04_Advanced_Algorithms    → Trees/KNN/Clustering (fertig)"
echo "   05_Neural_Networks        → Deep Learning (fertig)"
echo "   06_Computer_Vision_NLP    → CNNs/NLP (todo)"
echo "   07_Deployment_Portfolio   → Cloud/Presentation (todo)"
EOF
