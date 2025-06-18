# Handout: Der Modernisierte QUA³CK-Prozess - Von der Idee zur Cloud-App mit MLOps, MLFlow und Streamlit

## Einleitung: Die Evolution der Entwicklung im Maschinellen Lernen

Die Entwicklung von Anwendungen des Maschinellen Lernens (ML) hat sich in den letzten Jahren fundamental gewandelt. Die zentrale Herausforderung in vielen ML-Projekten liegt heute weniger in der Auswahl des perfekten Algorithmus, sondern vielmehr im umgebenden **Engineering**. Zahlreiche vielversprechende Prototypen, die oft in Umgebungen wie Jupyter-Notebooks entstehen, erreichen niemals den produktiven Einsatz. Dieses Phänomen, oft als "Prototyping-Falle" oder "Proof-of-Concept-Gefängnis" bezeichnet, entsteht, weil die für die explorative Analyse optimierten Werkzeuge und Prozesse nicht für die Anforderungen eines stabilen, skalierbaren und wartbaren Betriebs ausgelegt sind. Der Grund hierfür ist häufig das Fehlen von strukturierten, reproduzierbaren und wartbaren Prozessen, die für den Übergang von der Forschung in den Betrieb unerlässlich sind.

An dieser Stelle setzt das am Karlsruher Institut für Technologie (KIT) entwickelte Vorgehensmodell $QUA^{3}CK$ an. Es bietet einen didaktischen und praxisorientierten Rahmen für ML-Projekte und gliedert diese in klar definierte Phasen. Dieses Modell liefert eine wertvolle Struktur, insbesondere für Einsteiger und in akademischen Kontexten. Es stößt jedoch in der modernen, agilen Softwareentwicklung an Grenzen, wenn es um Skalierbarkeit, Automatisierung und kontinuierliche Verbesserung geht. Der klassische $QUA^{3}CK}$-Prozess behandelt die Phasen oft als sequenzielle Schritte, was in der Praxis zu langen Entwicklungszyklen und einer schwierigen Wartung führt.

Die Brücke zwischen der strukturierten Planung von $QUA^{3}CK$ und den Anforderungen der modernen Softwareentwicklung schlägt **Machine Learning Operations (MLOps)**. MLOps wendet die bewährten Prinzipien von DevOps (Kollaboration, Automatisierung, iterative Verbesserung) auf den gesamten Lebenszyklus von ML-Modellen an. Es liefert damit die notwendige Engineering-Disziplin, um die in $QUA^{3}CK$ definierten Ziele in der Praxis umzusetzen - und das skaliert, automatisiert und kontinuierlich. MLOps ist keine bloße Werkzeugsammlung, sondern eine Kultur und ein Methodenset, das darauf abzielt, die Lücke zwischen der experimentellen Welt der Entwicklung (Data Science) und der stabilen Welt des Betriebs (Operations) systematisch zu schließen.

Dieses Handout führt Sie durch die Modernisierung des QUA³CK-Prozessmodells mit MLOps-Praktiken. Sie lernen nicht nur die Theorie, sondern wenden diese auch praktisch an, um eine robuste ML-Anwendung zu entwickeln und als interaktive Web-App bereitzustellen. Am Ende verstehen Sie, wie aus einem starren, linearen Prozess ein dynamischer, sich selbst verbessernder Kreislauf wird.

---

## Teil 1: Das Fundamentale QUA³CK-Prozessmodell

Das QUA³CK-Modell ist ein Akronym, das die fünf Hauptphasen des Entwicklungsprozesses beschreibt. Die einzelnen Phasen werden nachfolgend anhand eines durchgehenden, klassischen Beispiels erläutert: der Klassifikation von Iris-Blüten. Es ist wichtig zu verstehen, dass diese Phasen in der Realität nicht streng getrennt sind, sondern sich oft überlappen und Iterationen erfordern.

- **Q** - Question (Fragestellung)
- **U** - Understanding the data (Datenverständnis)
- **A³** - Algorithm selection, Adapting features, Adjusting hyperparameters (Die A-Schleife)
- **C** - Conclude and compare (Schlussfolgerung und Vergleich)
- **K** - Knowledge transfer (Wissenstransfer)

### Phase Q - Question (Fragestellung)

Jedes Projekt beginnt mit einer klar definierten Frage. Eine unklare Fragestellung ist einer der häufigsten Gründe für das Scheitern von ML-Projekten. Hier werden technische und geschäftliche Ziele, Anforderungen und Key Performance Indicators (KPIs) festgelegt.

**Beispiel (Iris-Klassifikator):**
- **Problemstellung:** Eine Anwendung soll Iris-Pflanzen basierend auf ihren Blütenmerkmalen automatisch einer von drei Spezies zuordnen.
- **Anforderungen & KPIs:** Klassifikationsgenauigkeit > 95%; Vorhersagezeit < 500 ms.

### Phase U - Understanding the data (Datenverständnis)

Diese Phase konzentriert sich auf die Daten. Mittels explorativer Datenanalyse (EDA) werden Muster, Trends und Anomalien aufgedeckt. Die Datenqualität bestimmt die Obergrenze der Modellleistung.

**Beispiel (Iris-Klassifikator):**
- **Datenanalyse:** Untersuchung der Verteilungen und Korrelationen der Merkmale (`sepal_length`, `petal_length`, etc.).
- **Datenvorverarbeitung:** Prüfung auf fehlende Werte und Ausreißer; Skalierung der Features in Betracht ziehen.

### Phase A³ - Die iterative A-Schleife

Dies ist der iterative Kernzyklus der Modellentwicklung.
1.  **Algorithm selection and training:** Ein passender Algorithmus wird ausgewählt und auf den Trainingsdaten trainiert.
2.  **Adapting the features (Feature Engineering):** Merkmale werden erstellt, transformiert oder reduziert, um die Modellleistung zu verbessern.
3.  **Adjusting the hyperparameters:** Modellparameter (z.B. Lernrate), die nicht gelernt werden, werden optimiert.

**Beispiel (Iris-Klassifikator):**
- **A1 - Algorithmusauswahl:** Ein `RandomForestClassifier` wird gewählt.
- **A2 - Datenanpassung:** Für dieses Modell sind keine weiteren Anpassungen nötig.
- **A3 - Hyperparameter-Anpassung:** Optimierung von `n_estimators` und `max_depth`.

### Phase C - Conclude and compare (Schlussfolgerung und Vergleich)

Das finale Modell wird auf einem ungesehenen Testdatensatz bewertet. Die Ergebnisse werden mit den KPIs verglichen.

**Beispiel (Iris-Klassifikator):**
- Das Modell wird auf das Test-Set angewendet. Die Genauigkeit und eine Confusion Matrix werden berechnet. Die KPIs werden als erfüllt bewertet.

### Phase K - Knowledge transfer (Wissenstransfer)

Diese letzte Phase umfasst die Dokumentation des Prozesses und die Bereitstellung (Deployment) des Modells auf einer Zielplattform.

**Beispiel (Iris-Klassifikator):**
- Der Prozess wird dokumentiert und das trainierte Modell als Datei gespeichert, um es in einer Anwendung wiederzuverwenden.

---

## Teil 2: MLOps - Engineering-Disziplin für Maschinelles Lernen

MLOps transformiert die traditionellen Phasen in einen dynamischen, automatisierten und robusten Lebenszyklus.

### Kernprinzipien von MLOps:
1.  **Versionierung:** Code, Daten und Modelle werden versioniert (z.B. mit Git, DVC), um vollständige Reproduzierbarkeit zu gewährleisten.
2.  **Automatisierung & Continuous X (CI/CD/CT/CM):**
    - **CI (Continuous Integration):** Automatisches Testen von Code, Daten und Modellen.
    - **CD (Continuous Delivery):** Automatisierte Bereitstellung des gesamten Systems.
    - **CT (Continuous Training):** Automatisches Neutrainieren von Modellen bei neuen Daten oder Performanceverlust.
    - **CM (Continuous Monitoring):** Kontinuierliche Überwachung der Modellperformance in der Produktion.
3.  **Testing im ML-Kontext:** Umfassende Tests für Daten (Validierung), Modelle (Validierung, Fairness, Bias) und Infrastruktur (Stresstests).
4.  **Modell-Governance & Reproduzierbarkeit:** Klare Prozesse für Modellfreigabe, Zugriffsmanagement und die Einhaltung von Vorschriften.

---

## Teil 3: Synthese - Integration von MLOps in den QUA³CK-Prozess

Die folgende Tabelle verdeutlicht, wie MLOps die QUA³CK-Phasen anreichert.

| Phase (QUA³CK)      | Traditionelle Aktivität                                     | Modernisierte (MLOps) Aktivität                                                              | Key Tools                                         |
| ------------------- | ----------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| **Q** & **U** | Manuelle Analyse, statische KPIs, EDA in Notebooks.         | Kollaborative Definition, KPIs als Monitoring-Metriken, automatisierte Datenvalidierung.     | Git, Confluence, Great Expectations, DVC          |
| **A³** | Manuelles Experimentieren, lokales Training.                | Experiment-Tracking, modularer Code, automatisierte Trainingspipelines (CI/CT).              | MLFlow Tracking, Pytest, Docker, GitHub Actions   |
| **C** | Manuelle Validierung, Vergleich in Excel.                   | Automatisierte Modellvalidierung in CI/CD-Pipeline, zentraler Metrikvergleich.               | MLFlow UI, CI/CD-Tools                            |
| **K** | Manuelle Übergabe, statische Doku, manuelles Deployment.    | Zentrales Modell-Management (Registry), geregelte Übergänge, automatisiertes Deployment.     | MLFlow Model Registry, Streamlit                  |

### Deep Dive: Modernisierung der A³-Schleife mit MLFlow Tracking

Mit MLOps wird die A³-Schleife zu einem **reproduzierbaren Experiment**. MLFlow Tracking dient als zentrales Laborbuch, das jeden **Run** (Ausführung des Trainingscodes) mit **Parametern**, **Metriken** und **Artefakten** (z.B. das Modell selbst) protokolliert. Dies ermöglicht einen objektiven Vergleich verschiedener Experimente über die MLFlow UI.

### Deep Dive: Modernisierung von C & K mit der MLFlow Model Registry

Die MLFlow Model Registry ersetzt die manuelle Modellübergabe. Sie ist ein zentraler Speicher, der den Lebenszyklus von Modellen verwaltet.
- **Registered Model:** Ein Container für alle Versionen eines Modells (z.B. `iris-classifier`).
- **Model Version:** Jedes neu registrierte Modell erhält eine neue Version.
- **Model Alias:** Ein veränderbarer Zeiger (z.B. `production`), der auf eine bestimmte Version verweist und den Deployment-Prozess steuert.

---

## Teil 4: Praxis-Projekt - Entwicklung einer Iris-Klassifikator-App

### Schritt 1: Projekt-Setup (Phase Q, U)

1.  **Verzeichnis anlegen und Git initialisieren:**
    ```bash
    mkdir ml-app && cd ml-app
    git init
    ```
2.  **Virtuelle Umgebung erstellen und aktivieren.**
    > **Profi-Tipp: Warum eine virtuelle Umgebung?**
    > Eine virtuelle Umgebung (z.B. mit `venv`) isoliert die Python-Pakete eines Projekts. Das verhindert Konflikte zwischen Paketversionen und garantiert Reproduzierbarkeit.
3.  **Abhängigkeiten installieren:**
    ```bash
    pip install streamlit pandas scikit-learn mlflow
    ```

### Schritt 2: Experiment-Tracking mit MLFlow (Phase A³)

Skript `train.py` zum Trainieren und Protokollieren des Modells:
```python
import mlflow
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

# MLFlow Tracking Server für Teamarbeit
mlflow.set_tracking_uri("[http://127.0.0.1:5000](http://127.0.0.1:5000)")
mlflow.set_experiment("Iris Classification Experiment")

# Daten laden und aufteilen
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Startet einen MLFlow Run
with mlflow.start_run():
    params = {"n_estimators": 100, "max_depth": 5, "random_state": 42}
    mlflow.log_params(params)

    # Modell trainieren
    rf = RandomForestClassifier(**params)
    rf.fit(X_train, y_train)

    # Metriken protokollieren
    acc = accuracy_score(y_test, rf.predict(X_test))
    mlflow.log_metric("accuracy", acc)

    # Modell protokollieren
    mlflow.sklearn.log_model(rf, "random-forest-model")

print(f"Accuracy: {acc}")
```

### Schritt 3: Modell-Management mit der Registry (Phase C)

1.  **Modell registrieren:** In der MLFlow-UI zum besten Run navigieren und auf "Register Model" klicken.
2.  **Alias zuweisen:** Dem Modell auf der "Models"-Seite einen Alias wie `production-candidate` zuweisen.

### Schritt 4: Erstellung der Web-App mit Streamlit (Phase K)

Die App `app.py` lädt das Modell aus der Registry und stellt eine UI bereit.
```python
import streamlit as st
import pandas as pd
import mlflow

MODEL_URI = "models:/iris-classifier@production-candidate"

st.title("Iris Flower Species Classifier")

# Lädt das Modell und cacht es
@st.cache_resource
def load_model():
    return mlflow.pyfunc.load_model(model_uri=MODEL_URI)

model = load_model()

# UI-Elemente für die Eingabe
st.sidebar.header("Input Features")
sepal_length = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.4)
sepal_width = st.sidebar.slider("Sepal Width (cm)", 2.0, 4.5, 3.4)
petal_length = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# Vorhersage
if st.button("Predict Species"):
    input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                              columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])
    prediction = model.predict(input_data)
    target_names = ['setosa', 'versicolor', 'virginica']
    predicted_species = target_names[prediction[0]]
    st.success(f"The predicted species is: **{predicted_species.capitalize()}**")
```

### Schritt 5: Deployment (Phase K)

1.  **Vorbereitung:** `requirements.txt` erstellen (`pip freeze > requirements.txt`) und Code auf GitHub pushen.
2.  **Deployment:** Auf `share.streamlit.io` das GitHub-Repository auswählen und die App deployen.

---

## Literaturempfehlungen und weiterführende Ressourcen

- **Offizielle Dokumentationen:**
  - [MLFlow](https://mlflow.org/docs/latest/index.html)
  - [Streamlit](https://docs.streamlit.io/)
  - [Scikit-learn](https://scikit-learn.org/stable/)
- **Communitys & Listen:**
  - [MLOps Community](https://mlops.community/)
  - [Streamlit Gallery](https://streamlit.io/gallery)
  - ["Awesome MLOps" auf GitHub](https://github.com/visenger/awesome-mlops)

## Schlussfolgerung: Den Vollen ML-Lebenszyklus Meistern

Dieses Handout hat gezeigt, wie die Anreicherung des $QUA^{3}CK$-Modells mit MLOps-Prinzipien und -Werkzeugen den Entwicklungsprozess von einer Reihe manueller Schritte zu einem integrierten, robusten und agilen Lebenszyklus transformiert. Ein erfolgreiches ML-Produkt ist mehr als nur ein genaues Modell; es ist ein zuverlässiges, wartbares und skalierbares System.

**Ihr Weg geht jetzt weiter:** Nutzen Sie das Gelernte als Ausgangspunkt und experimentieren Sie weiter. Viel Erfolg auf Ihrer Reise zum MLOps-Experten!
