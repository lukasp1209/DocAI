# ✅ TODO: Nächste Schritte - AMALEA 2025

**Datum**: 15. Juni 2025  
**Status**: Phase 1 - Notebooks komplettieren

---

## 🔥 **HEUTE (15. Juni) - Priorität 1**

### ✅ Abgeschlossen:
- [x] Repository bereinigt und AMALEA-Inhalte integriert
- [x] Woche 0-4 Notebooks erstellt und getestet
- [x] Docker-Environment aufgesetzt
- [x] Ordnerstruktur modernisiert
- [x] Dokumentation vollständig

### 🚧 **Heute noch zu erledigen:**

#### 1. Woche 5 Notebook starten (CNN & Computer Vision)
```bash
# Arbeitsschritte:
cd "/Users/kqc/Dropbox/Vorlesungen/13. IU - Data Analytics und Big Data/amalea"
cd Woche_5_Advanced_Topics/

# Notebook erstellen basierend auf:
# - BACKUP_Original_AMALEA_Notebooks/Woche 5/*
# - "1 Falten, Ausschneiden und fertig ist das CNN.ipynb"
# - "2 Inhaltsstoffe Kann Spuren von Intelligenz enthalten.ipynb"
```

#### 2. Docker-Environment validieren
```bash
# Alle Services testen:
docker-compose up -d
# Prüfen: http://localhost:8888 (Jupyter)
# Prüfen: http://localhost:8501 (Streamlit)  
# Prüfen: http://localhost:5000 (MLflow)
```

#### 3. Requirements-2025.txt optimieren
```bash
# Für Computer Vision erweitern:
# - opencv-python
# - pillow
# - torchvision
# - timm (für pretrained models)
```

---

## 📅 **DIESE WOCHE (16.-21. Juni)**

### **Montag (16. Juni):**
- [ ] 🖼️ **Woche 5 CNN Notebook** komplett fertigstellen
  - Convolutional Layer Erklärung (aus ursprünglichem AMALEA)
  - Transfer Learning Demo
  - Streamlit Image Upload Interface
  - Real-time Prediction
- [ ] 🧪 **Erste Streamlit CV-App** prototypen
- [ ] 🔧 **Docker Memory Limits** für studentische Hardware optimieren

### **Dienstag (17. Juni):**
- [ ] 📝 **Woche 5 NLP Notebook** erstellen
  - Text Preprocessing
  - Sentiment Analysis mit BERT
  - Streamlit Text Input & Analysis
  - Hugging Face Integration
- [ ] 🤗 **Hugging Face Models** in Requirements integrieren
- [ ] 🔍 **Cross-Platform Testing** (Windows/Mac/Linux)

### **Mittwoch (18. Juni):**
- [ ] ☁️ **Woche 6 Deployment Notebook** erstellen
  - Streamlit Cloud Setup
  - GitHub Integration
  - Secrets Management
  - Performance Monitoring
- [ ] 🚀 **GitHub Actions Pipeline** konfigurieren
- [ ] 📖 **Deployment Guide** für Studierende

### **Donnerstag (19. Juni):**
- [ ] 🎤 **Woche 6 Portfolio Notebook** erstellen
  - Präsentationstechniken
  - Storytelling mit Daten
  - Live-Demo Best Practices
  - Assessment Template
- [ ] 📊 **Bewertungsrubrik** finalisieren
- [ ] ✅ **Integration Testing** aller Notebooks

### **Freitag (20. Juni):**
- [ ] 🐳 **Docker-Compose finalisieren** und optimieren
- [ ] 📚 **Dokumentation vervollständigen**
- [ ] 🎯 **README.md** mit finaler Anleitung
- [ ] 📋 **Kurs-Ready Checklist** abarbeiten

---

## 🎯 **NÄCHSTE WOCHE (23.-28. Juni)**

### **Phase 2: Streamlit-Apps & Deployment**

#### Montag-Mittwoch: Standalone Apps
```
📱 Streamlit Apps erstellen:
├── app_woche1_data_exploration.py
├── app_woche2_ml_classification.py  
├── app_woche3_algorithm_comparison.py
├── app_woche4_neural_networks.py
├── app_woche5_computer_vision.py
└── app_woche6_portfolio_showcase.py
```

#### Donnerstag-Freitag: Cloud Deployment
- Streamlit Cloud Setup für alle Apps
- GitHub Repository strukturieren
- CI/CD Pipeline testen
- Student-friendly Deployment Guide

---

## 🛠️ **KONKRETE ARBEITSSCHRITTE**

### **Woche 5 - Computer Vision (heute starten):**

```python
# Notebook Struktur:
# 1. CNN Grundlagen (aus ursprünglichem AMALEA)
#    - Convolutional Layer verstehen
#    - Pooling & Stride Konzepte  
#    - Feature Maps visualisieren

# 2. Transfer Learning (modern erweitert)
#    - ResNet/VGG/EfficientNet
#    - Fine-tuning vs. Feature extraction
#    - Domain Adaptation

# 3. Streamlit Integration (neu)
#    - st.file_uploader für Bilder
#    - PIL/OpenCV Processing
#    - Real-time Prediction
#    - Results Visualization

# 4. Practical Examples
#    - Bildklassifikation (Cats vs Dogs)
#    - Object Detection Demo
#    - Medical Imaging (wenn verfügbar)
```

### **Requirements Update für CV/NLP:**

```python
# requirements-2025.txt ergänzen:
opencv-python>=4.8.0
pillow>=10.0.0
torchvision>=0.15.0
timm>=0.9.0              # für pretrained models
transformers>=4.30.0     # bereits drin, aber prüfen
datasets>=2.14.0         # für Hugging Face datasets
gradio>=3.35.0          # Alternative zu Streamlit für ML demos
```

### **Docker Optimierungen:**

```yaml
# docker-compose.yml - Performance Updates:
jupyter-lab:
  mem_limit: 3g      # von 2g erhöhen für CV/NLP
  shm_size: 1g       # für PyTorch DataLoader
  
streamlit-dev:
  environment:
    - STREAMLIT_SERVER_MAXUPLOADSIZE=200  # für große Bilder
    - STREAMLIT_SERVER_ENABLECORS=false   # Security
```

---

## 📊 **FORTSCHRITT TRACKING**

### **Vollständigkeits-Checklist:**

#### Notebooks (6/6):
- [x] Woche 0: Python + Docker Grundlagen  
- [x] Woche 1: Streamlit Basics + AMALEA Jupyter-Integration
- [x] Woche 2: ML Integration + AMALEA ML-Konzepte
- [x] Woche 3: Algorithmen + AMALEA Decision Trees/KNN
- [x] Woche 4: Neural Networks + AMALEA Deep Learning
- [ ] Woche 5: Computer Vision + NLP (🚧 heute starten)
- [ ] Woche 6: Deployment + Portfolio (🚧 Mittwoch)

#### Infrastruktur:
- [x] Docker-Compose Setup
- [x] Requirements-2025.txt
- [ ] Streamlit Cloud Integration (🚧 nächste Woche)
- [ ] GitHub Actions Pipeline (🚧 nächste Woche)

#### Dokumentation:
- [x] README.md modernisiert
- [x] AMALEA-Integration dokumentiert
- [x] Migration Log erstellt
- [ ] Student Setup Guide (🚧 Freitag)
- [ ] Instructor Manual (🚧 nächste Woche)

### **Qualitätskontrolle:**

#### Testing Checklist:
- [ ] Alle Notebooks ausführbar
- [ ] Docker-Services starten korrekt
- [ ] Cross-Platform kompatibel
- [ ] Resource-effizient für Student-Hardware
- [ ] Cloud-Deployment funktional

---

## 🎯 **ERFOLGS-KRITERIEN**

### **Ende dieser Woche:**
- ✅ Alle 6 Wochen-Notebooks komplett und funktional
- ✅ Docker-Environment stabil und optimiert  
- ✅ Vollständige Dokumentation
- ✅ Student-ready Repository

### **Ende nächster Woche:**
- ✅ 6 deploybare Streamlit-Apps
- ✅ Cloud-Deployment Pipeline  
- ✅ Assessment Framework
- ✅ Instructor Resources

### **Kurs-Start Ready:**
- ✅ Student Onboarding Materials
- ✅ Technical Support Infrastructure
- ✅ Video/Quiz Integration Plan
- ✅ Portfolio Assessment Rubric

---

## 🚨 **RISIKEN & MITIGATION**

### **Potentielle Probleme:**

#### Technical:
- **Docker Memory Issues** → Resource Limits konfigurieren
- **Package Conflicts** → requirements.txt Testing
- **Cross-Platform Bugs** → Multiple OS Testing

#### Didactic:
- **Complexity Overload** → Schrittweise Progression
- **AMALEA Video Mismatch** → Content Mapping erstellen
- **Assessment Clarity** → Rubric Beta Testing

#### Organizational:
- **Timeline Pressure** → Prioritäten klar definiert
- **Resource Constraints** → Minimum Viable Product Focus
- **Stakeholder Alignment** → Regular Check-ins

---

**🎯 FOKUS HEUTE: Woche 5 CNN Notebook starten und Docker-Environment final testen!**

*Next Milestone: Woche 5 & 6 Notebooks bis Donnerstag* 🚀
