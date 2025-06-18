# **Handout: Der Modernisierte QUA³CK-Prozess \- Von der Idee zur Cloud-App mit MLOps, MLFlow und Streamlit**

## **Einleitung: Die Evolution der Entwicklung im Maschinellen Lernen**

Die Entwicklung von Anwendungen des Maschinellen Lernens (ML) hat sich in den letzten Jahren fundamental gewandelt. Die zentrale Herausforderung in vielen ML-Projekten liegt heute weniger in der Auswahl des perfekten Algorithmus, sondern vielmehr im umgebenden Engineering. Zahlreiche vielversprechende Prototypen, die oft in Umgebungen wie Jupyter-Notebooks entstehen, erreichen niemals den produktiven Einsatz. Dieses Phänomen, oft als "Prototyping-Falle" oder "Proof-of-Concept-Gefängnis" bezeichnet, entsteht, weil die für die explorative Analyse optimierten Werkzeuge und Prozesse nicht für die Anforderungen eines stabilen, skalierbaren und wartbaren Betriebs ausgelegt sind. Der Grund hierfür ist häufig das Fehlen von strukturierten, reproduzierbaren und wartbaren Prozessen, die für den Übergang von der Forschung in den Betrieb unerlässlich sind.

An dieser Stelle setzt das am Karlsruher Institut für Technologie (KIT) entwickelte Vorgehensmodell QUA3CK an. Es bietet einen didaktischen und praxisorientierten Rahmen für ML-Projekte und gliedert diese in klar definierte Phasen. Dieses Modell liefert eine wertvolle Struktur, insbesondere für Einsteiger und in akademischen Kontexten. Es stößt jedoch in der modernen, agilen Softwareentwicklung an Grenzen, wenn es um Skalierbarkeit, Automatisierung und kontinuierliche Verbesserung geht. Der klassische QUA3CK-Prozess behandelt die Phasen oft als sequenzielle Schritte, was in der Praxis zu langen Entwicklungszyklen und einer schwierigen Wartung führt.

Die Brücke zwischen der strukturierten Planung von QUA3CK und den Anforderungen der modernen Softwareentwicklung schlägt Machine Learning Operations (MLOps). MLOps wendet die bewährten Prinzipien von DevOps (Kollaboration, Automatisierung, iterative Verbesserung) auf den gesamten Lebenszyklus von ML-Modellen an. Es liefert damit die notwendige Engineering-Disziplin, um die in QUA3CK definierten Ziele in der Praxis umzusetzen \- und das skaliert, automatisiert und kontinuierlich. MLOps ist keine bloße Werkzeugsammlung, sondern eine Kultur und ein Methodenset, das darauf abzielt, die Lücke zwischen der experimentellen Welt der Entwicklung (Data Science) und der stabilen Welt des Betriebs (Operations) systematisch zu schließen.

Dieses Handout führt Sie durch die Modernisierung des QUA³CK-Prozessmodells mit MLOps-Praktiken. Sie lernen nicht nur die Theorie, sondern wenden diese auch praktisch an, um eine robuste ML-Anwendung zu entwickeln und als interaktive Web-App bereitzustellen. Am Ende verstehen Sie, wie aus einem starren, linearen Prozess ein dynamischer, sich selbst verbessernder Kreislauf wird.

## **Teil 1: Das Fundamentale QUA³CK-Prozessmodell**

Das QUA³CK-Modell ist ein Akronym, das die fünf Hauptphasen des Entwicklungsprozesses beschreibt. Die einzelnen Phasen werden nachfolgend anhand eines durchgehenden, klassischen Beispiels erläutert: der Klassifikation von Iris-Blüten. Es ist wichtig zu verstehen, dass diese Phasen in der Realität nicht streng getrennt sind, sondern sich oft überlappen und Iterationen erfordern.

* **Q** \- Question (Fragestellung)  
* **U** \- Understanding the data (Datenverständnis)  
* **A³** \- Algorithm selection, Adapting features, Adjusting hyperparameters (Die A-Schleife)  
* **C** \- Conclude and compare (Schlussfolgerung und Vergleich)  
* **K** \- Knowledge transfer (Wissenstransfer)

### **Phase Q \- Question (Fragestellung)**

Jedes Projekt beginnt mit einer klar definierten Frage oder einem Problem, das gelöst werden soll. Eine unklare Fragestellung ist einer der häufigsten Gründe für das Scheitern von ML-Projekten. In dieser initialen Phase ist es entscheidend, nicht nur die technischen, sondern auch die geschäftlichen Ziele, Anforderungen, Randbedingungen und erwarteten Ergebnisse (Key Performance Indicators, KPIs) festzulegen. Dies verhindert, dass Spezifikationen zu spät geklärt werden oder das Endprodukt die eigentlichen Bedürfnisse der Anwender verfehlt.

**Beispiel (Iris-Klassifikator):**

* **Problemstellung:** Eine Anwendung soll Iris-Pflanzen basierend auf den Merkmalen ihrer Blüten (Kelch- und Kronblattlänge sowie \-breite) automatisch einer von drei Spezies zuordnen: Setosa, Versicolor oder Virginica. Die Anwendung soll von Botanik-Studenten genutzt werden, um bei der Feldarbeit schnell eine Einschätzung zu erhalten.  
* **Anforderungen & KPIs:** Das entwickelte Modell soll eine Klassifikationsgenauigkeit (Accuracy) von über 95% auf bisher ungesehenen Daten erreichen. Die Vorhersagezeit pro Pflanze muss unter 500 Millisekunden liegen, um eine flüssige Benutzererfahrung zu gewährleisten.

### **Phase U \- Understanding the data (Datenverständnis)**

Diese Phase konzentriert sich auf die Daten selbst – das Herzstück jedes ML-Modells. Falls kein Datensatz vorhanden ist, muss dieser zunächst erhoben werden. Anschließend werden die Rohdaten mittels explorativer Datenanalyse (EDA) analysiert, um verborgene Informationen, Muster, Trends oder irrelevante Daten zu entdecken. Dies umfasst statistische Analysen (Mittelwert, Korrelation), Visualisierungen und die essenzielle Datenvorverarbeitung (Umgang mit fehlenden Werten, Ausreißern, Normalisierung, Data Augmentation). Die Qualität der Daten bestimmt maßgeblich die Obergrenze für die Leistungsfähigkeit des späteren Modells.

**Beispiel (Iris-Klassifikator):**

* **Datenanalyse:** Der bekannte Iris-Datensatz wird geladen. Mittels deskriptiver Statistik und Visualisierungen (z.B. Scatter-Plots, Box-Plots) werden die Verteilungen und Korrelationen der Merkmale (sepal\_length, sepal\_width, petal\_length, petal\_width) untersucht. Es wird festgestellt, dass petal\_length und petal\_width stark korrelieren und eine gute Trennung der Klassen ermöglichen.  
* **Datenvorverarbeitung:** Der Datensatz wird auf fehlende Werte überprüft (im Iris-Datensatz sind keine vorhanden). Es wird analysiert, ob Ausreißer existieren, die das Training beeinträchtigen könnten. Eine Skalierung der Features (z.B. Standardisierung) wird in Betracht gezogen, um sicherzustellen, dass alle Merkmale einen ähnlichen Einfluss auf das Modell haben, was besonders für abstandsbasiere Algorithmen wichtig ist.

### **Phase A³ \- Die iterative A-Schleife**

Diese drei Schritte – Algorithmusauswahl, Feature-Anpassung und Hyperparameter-Optimierung – bilden den iterativen Kernzyklus der Modellentwicklung. Es ist entscheidend zu verstehen, dass dies kein linearer Ablauf ist, sondern eine Schleife, die so oft durchlaufen wird, bis das Modell die gewünschten Ergebnisse liefert. In der Praxis ist dies oft der zeitaufwändigste Teil eines ML-Projekts.

1. **Algorithm selection and training (Algorithmusauswahl und Training):** Basierend auf der Problemstellung (Klassifikation, Regression etc.), der Datenmenge und \-art wird ein passender Algorithmus ausgewählt. Die Auswahl reicht von einfachen linearen Modellen bis hin zu komplexen tiefen neuronalen Netzen. Das Modell wird dann auf den aufbereiteten Trainingsdaten trainiert.  
2. **Adapting the features (Datenanpassung/Feature Engineering):** Der Datensatz wird an die spezifischen Anforderungen des gewählten Algorithmus angepasst. Dies kann die Umstrukturierung von Daten, das Erstellen neuer Merkmale aus bestehenden (z.B. Polynom-Features) oder die Reduktion von Merkmalen umfassen, um Überanpassung zu vermeiden.  
3. **Adjusting the hyperparameters (Hyperparameter-Anpassung):** Hyperparameter sind die "Stellschrauben" eines Modells, die nicht während des Trainings gelernt werden (z. B. Lernrate, Anzahl der Schichten in einem neuronalen Netz). Sie werden manuell oder durch automatisierte Verfahren wie Grid Search oder Bayesian Optimization optimiert, um die Modellleistung zu maximieren.

**Beispiel (Iris-Klassifikator):**

* **A1 \- Algorithmusauswahl:** Ein RandomForestClassifier aus scikit-learn wird als geeigneter, robuster Algorithmus für dieses tabellarische Klassifikationsproblem ausgewählt. Alternativ könnte auch ein Support Vector Machine (SVM) oder ein einfaches neuronales Netz in Betracht gezogen werden.  
* **A2 \- Datenanpassung:** Für den Random Forest sind die Daten bereits in einem passenden Format. Es sind keine weiteren Anpassungen notwendig. Wäre ein lineares Modell gewählt worden, hätte man die Features eventuell standardisieren müssen.  
* **A3 \- Hyperparameter-Anpassung:** Die Hyperparameter des Modells, wie die Anzahl der Bäume (n\_estimators) und die maximale Tiefe der Bäume (max\_depth), werden durch systematisches Ausprobieren verschiedener Werte optimiert.

Dieser Zyklus wird wiederholt, wobei die Leistung des Modells auf einem separaten Validierungsdatensatz gemessen wird, um eine Überanpassung an die Trainingsdaten zu vermeiden.

### **Phase C \- Conclude and compare (Schlussfolgerung und Vergleich)**

In dieser Phase wird die Generalisierungsfähigkeit des final trainierten Modells auf einem separaten Testdatensatz bewertet, den das Modell während des gesamten Entwicklungszyklus noch nie gesehen hat. Die Ergebnisse werden mit den in Phase Q definierten KPIs und eventuell mit Referenzmodellen ("Baselines") verglichen. Wenn die Leistung nicht ausreicht, muss zur A³-Schleife zurückgekehrt werden.

**Beispiel (Iris-Klassifikator):**

* Das optimierte RandomForestClassifier-Modell wird auf das Test-Set angewendet.  
* Die Genauigkeit wird berechnet und eine Confusion Matrix erstellt, um die Leistung im Detail zu analysieren (z.B. welche Klassen am häufigsten verwechselt werden).  
* Es wird festgestellt, dass das Modell die KPI von \>95% Genauigkeit erfüllt. Die Vorhersagezeit wird ebenfalls gemessen und als zufriedenstellend bewertet.

### **Phase K \- Knowledge transfer (Wissenstransfer)**

Sobald das Modell die Anforderungen erfüllt, ist es aus Entwicklungssicht "fertig". Diese letzte, oft vernachlässigte Phase umfasst die detaillierte Dokumentation des gesamten Prozesses (Algorithmus, finale Parameter, Datensätze, Vorverarbeitungsschritte) zur Sicherstellung der Replizierbarkeit und die Bereitstellung (Deployment) des Modells auf einer Zielplattform, z.B. als API-Endpunkt in der Cloud oder integriert in eine mobile App.

**Beispiel (Iris-Klassifikator):**

* Die finalen Hyperparameter, der Trainingsprozess, die Leistungskennzahlen und die Feature-Wichtigkeiten werden in einem Report dokumentiert.  
* Das trainierte Modell wird als Datei (z.B. mittels pickle oder joblib) gespeichert, um es in einer Anwendung \- wie der später entwickelten Streamlit-App \- wiederzuverwenden.

## **Teil 2: MLOps \- Engineering-Disziplin für Maschinelles Lernen**

MLOps führt eine Reihe von Kernprinzipien ein, die für die Modernisierung und Skalierung des QUA³CK-Prozesses unerlässlich sind. Diese Prinzipien transformieren die traditionellen, oft manuellen Phasen in einen dynamischen, automatisierten und robusten Lebenszyklus.

### **Kernprinzip 1: Versionierung (Code, Daten, Modelle)**

MLOps erweitert die klassische Code-Versionierung mit Werkzeugen wie Git auf alle Artefakte des ML-Prozesses. Dies bedeutet, dass nicht nur der Code, sondern auch die verwendeten Datensätze, die Feature-Engineering-Pipelines und die trainierten Modelle selbst versioniert werden. Die Versionierung aller Komponenten ist die unabdingbare Grundlage, um eine ML-Pipeline vollständig reproduzierbar zu machen. Wenn ein Fehler auftritt oder ein Modell unerwartete Vorhersagen liefert, ermöglicht diese lückenlose Historie eine exakte Rekonstruktion des Zustands und eine schnelle Fehleranalyse. Dies ist entscheidend für Audits, das Debugging von Fehlern und die kollaborative Arbeit im Team.

### **Kernprinzip 2: Automatisierung & Continuous X (CI/CD/CT/CM)**

Die Automatisierung von wiederkehrenden Aufgaben ist ein zentrales Anliegen von MLOps, um manuelle Fehler zu reduzieren, die Konsistenz zu erhöhen und den Entwicklungszyklus zu beschleunigen. Diese Automatisierung manifestiert sich in den "Continuous"-Praktiken, die einen geschlossenen Kreislauf bilden:

* **Continuous Integration (CI):** Geht über das reine Testen von Code hinaus. Bei jeder Code-Änderung werden automatisch Datenvalidierungstests, Tests der Trainingspipeline und grundlegende Modell-Qualitätsprüfungen ausgeführt.  
* **Continuous Delivery (CD):** Die automatisierte Bereitstellung des gesamten Systems, einschließlich des trainierten und validierten Modells als Vorhersagedienst (Prediction Service) in einer Test- oder Produktionsumgebung.  
* **Continuous Training (CT):** Das automatische Neutrainieren von Modellen, sobald neue relevante Daten verfügbar sind oder die Modellperformance in der Produktion nachlässt. Dies ist die direkte Antwort auf das Problem des "Model Decay" oder der Modellalterung und sorgt dafür, dass Modelle relevant bleiben.  
* **Continuous Monitoring (CM):** Die kontinuierliche Überwachung der technischen und statistischen Performance des Modells in der Produktionsumgebung. Dies dient dazu, Probleme wie "Model Drift" (eine Veränderung in der Verteilung der Eingabedaten) oder "Concept Drift" (eine Veränderung der Beziehung zwischen Ein- und Ausgabedaten) proaktiv zu erkennen und ggf. ein Retraining (CT) auszulösen.

### **Kernprinzip 3: Testing im ML-Kontext**

Testing in ML-Projekten ist weitaus umfassender als klassische Unit- und Integrationstests, da es sich mit der inhärenten Unsicherheit von Daten und Modellen befassen muss. Es beinhaltet spezifische Tests für die verschiedenen Artefakte und Phasen des ML-Lebenszyklus:

* **Datenvalidierung:** Automatische Überprüfung von Datenschemata (sind alle Spalten vorhanden?), Verteilungen (entspricht die Verteilung der neuen Daten der der Trainingsdaten?) und statistischen Eigenschaften.  
* **Modellvalidierung:** Überprüfung der Generalisierungsfähigkeit des Modells nicht nur auf dem gesamten Testset, sondern auch auf wichtigen, vordefinierten Datensegmenten (z.B. für verschiedene Benutzergruppen), um versteckte Schwächen aufzudecken.  
* **Fairness- und Bias-Tests:** Sicherstellung, dass das Modell keine unterrepräsentierten Gruppen systematisch benachteiligt. Es wird geprüft, ob die Fehlerraten über verschiedene demografische Gruppen hinweg ähnlich sind.  
* **Infrastruktur- und Stresstests:** Prüfung, ob die Trainings- und Serving-Infrastruktur unter Last stabil bleibt und die in Phase Q definierten Latenzanforderungen erfüllt.  
* **Konsistenztests:** Ein wichtiger Test validiert, dass ein Modell für dieselbe Eingabe in der Trainingsumgebung und in der Serving-Umgebung exakt dieselbe Vorhersage liefert. Abweichungen deuten auf subtile Engineering-Fehler hin, z.B. unterschiedliche Versionen von Abhängigkeiten.

### **Kernprinzip 4: Modell-Governance & Reproduzierbarkeit**

Governance umfasst die Verwaltung aller Aspekte von ML-Systemen, um Effizienz, Sicherheit und die Einhaltung von Vorschriften (Compliance) zu gewährleisten. Dies beinhaltet klare Prozesse für die Freigabe von Modellen, das Management von Zugriffsrechten und die Sicherstellung ethischer Richtlinien. Reproduzierbarkeit ist dabei kein isoliertes Prinzip, sondern das synergetische Ergebnis der konsequenten Anwendung von Versionierung, Automatisierung und Testing. Ein Governance-Framework definiert, wer ein Modell in die Produktion überführen darf und welche Qualitätskriterien dafür erfüllt sein müssen. MLOps-Werkzeuge helfen dabei, diese Regeln automatisiert durchzusetzen.

## **Teil 3: Synthese \- Integration von MLOps in den QUA³CK-Prozess**

In diesem zentralen Abschnitt wird gezeigt, wie die MLOps-Prinzipien die traditionellen QUA³CK-Phasen transformieren und anreichern. Die folgende Tabelle dient als didaktische Referenz, die den Mehrwert von MLOps in jeder Phase auf einen Blick verdeutlicht und eine Brücke zur praktischen Umsetzung schlägt.

| Phase (QUA³CK) | Traditionelle Aktivität (gemäß QUA³CK) | Modernisierte (MLOps) Aktivität | Key Tools |  
| Q-Question & U-Understanding | Manuelle Anforderungsanalyse, statische KPIs in einem Dokument. EDA in einem Notebook, manuelle Datenbereinigung, Pre-Processing. | Kollaborative Definition in einem Wiki, KPIs als Metriken für automatisches Monitoring definieren. Automatisierte Datenvalidierungs-Pipelines, Nutzung eines Feature Stores, Daten-Versionierung. | Git, Confluence, Great Expectations, DVC, Feast |  
| A³ \- The A-Loop | Manuelles Experimentieren: Algorithmus wählen, Daten anpassen, Hyperparameter tunen. Lokales Training, Speichern als .pkl. | Experiment-Tracking, Code in modularer, testbarer Form, automatisierte Trainingspipeline (CI/CT). | MLFlow Tracking, Pytest, Docker, Jenkins/GitHub Actions |  
| C- Conclude & Compare | Manuelle Validierung auf Test-Set, Vergleich in Excel/Report. | Automatisierte Modellvalidierung in CI/CD-Pipeline, zentraler Vergleich von Metriken. | MLFlow UI, CI/CD-Tools |  
| K \- Knowledge Transfer | Manuelle Übergabe des Modells, statische Dokumentation, manuelles Deployment. | Zentrales Modell-Management (Registry), geregelte Staging/Production-Übergänge, kontinuierliches Monitoring, automatisiertes Deployment. | MLFlow Model Registry, Prometheus/Grafana, Streamlit |

### **Deep Dive: Modernisierung der A³-Schleife mit MLFlow Tracking**

Mit MLOps ändert sich das Paradigma der A³-Schleife fundamental: Es geht nicht mehr nur darum, ein Skript zu schreiben und es auszuführen, sondern darum, ein nachvollziehbares und **reproduzierbares Experiment** durchzuführen. Das Open-Source-Framework MLFlow bietet hierfür mit seiner Tracking-Komponente ein mächtiges Werkzeug, das als zentrales Laborbuch für alle Modellentwicklungsaktivitäten dient.

MLFlow Tracking organisiert die Modellentwicklung um folgende Kernkonzepte:

* **Experiment:** Ein logischer Container für zusammengehörige Durchläufe, z.B. "Optimierung des Iris-Klassifikators" oder "Test verschiedener Architekturen".  
* **Run:** Eine einzelne Ausführung des Trainingscodes. Jeder Run erhält eine eindeutige ID und wird mit allen zugehörigen Informationen aufgezeichnet.  
* **Parameter (log\_param):** Die Eingaben des Experiments werden protokolliert. Dies sind typischerweise die Hyperparameter des Modells (z.B. max\_depth) oder Merkmale der Eingabedaten (z.B. feature\_set\_version).  
* **Metriken (log\_metric):** Die quantitativen Ergebnisse des Experiments werden aufgezeichnet, z.B. die accuracy oder der f1\_score auf dem Test-Set. Metriken können über die Zeit protokolliert werden (z.B. der Trainingsverlust pro Epoche), um Lernkurven zu visualisieren.  
* **Artefakte (log\_artifact/log\_model):** Beliebige Ausgabedateien können gespeichert werden. Am wichtigsten ist hier das trainierte Modell selbst, aber auch Visualisierungen (z.B. eine Confusion Matrix), Datensätze oder Log-Dateien können als Artefakte abgelegt werden.

Der unschätzbare Vorteil: Jeder Trainingslauf wird mit seinen Ein- und Ausgaben exakt und unveränderlich dokumentiert. MLFlow bietet eine Web-UI, in der verschiedene Runs bequem verglichen werden können (z.B. durch Sortieren nach der besten Metrik oder durch parallele Darstellung von Graphen), um das beste Modell objektiv zu identifizieren.

### **Deep Dive: Modernisierung von C & K mit der MLFlow Model Registry**

Auch die Phasen C (Conclude) und K (Knowledge Transfer) erfahren eine Transformation. Der manuelle Vergleich und die Übergabe eines Modells werden durch einen zentralisierten, versionierten und governance-gesteuerten Prozess ersetzt. Die **MLFlow Model Registry** ist ein zentralisierter Speicher, der genau diesen Lebenszyklus verwaltet und als "Single Source of Truth" für produktionsreife Modelle dient.

Die Schlüsselkonzepte der Model Registry sind:

* **Registered Model:** Ein eindeutig benanntes Modell im Registry, z.B. iris-classifier. Es dient als Container für alle Versionen dieses spezifischen Modells.  
* **Model Version:** Jedes Mal, wenn ein neues Modell unter diesem Namen registriert wird (z.B. nach einem Retraining mit neuen Daten), wird eine neue, inkrementelle Version erstellt (Version 1, Version 2,...). Dies ermöglicht eine lückenlose und nachvollziehbare Modell-Historie.  
* **Model Alias:** Ein veränderbarer "Zeiger" oder "Tag" (z.B. champion, challenger), der auf eine bestimmte Modellversion verweist. Aliase werden oft verwendet, um Umgebungen abzubilden, z.B. staging und production. Dieser Mechanismus steuert den Lebenszyklus eines Modells von der Entwicklung (staging) über das Testen bis hin zum produktiven Einsatz (production). So kann ein neues Modell erst als staging-Kandidat markiert, automatisiert getestet und bei Erfolg auf production hochgestuft werden, wobei das alte Produktionsmodell automatisch archiviert wird.

## **Teil 4: Praxis-Projekt \- Entwicklung und Deployment einer Iris-Klassifikator-App**

Diese detaillierte Schritt-für-Schritt-Anleitung führt durch das gesamte Projekt und verbindet die Theorie mit der praktischen Anwendung.

### **Schritt 1: Projekt-Setup (Phase Q, U)**

1. **Verzeichnis anlegen und Git initialisieren:**  
   mkdir ml-app && cd ml-app  
   git init

2. **Virtuelle Umgebung erstellen und aktivieren.**

Profi-Tipp: Warum eine virtuelle Umgebung?  
Eine virtuelle Umgebung (wie venv) isoliert die für dieses Projekt benötigten Python-Pakete von anderen Projekten auf Ihrem System. Das verhindert Konflikte zwischen Paketversionen (z.B. Projekt A benötigt pandas 1.5, Projekt B aber pandas 2.0) und stellt sicher, dass Ihr Projekt (und die requirements.txt-Datei) nur die wirklich notwendigen Abhängigkeiten enthält. Dieser Schritt ist fundamental für die Reproduzierbarkeit\!

3. **Abhängigkeiten installieren:**  
   pip install streamlit pandas scikit-learn mlflow

### **Schritt 2: Experiment-Tracking mit MLFlow (Phase A³)**

Erstellen Sie ein Skript train.py, das ein Modell trainiert und den gesamten Prozess als reproduzierbares Experiment mit MLFlow protokolliert.

import mlflow  
from sklearn.model\_selection import train\_test\_split  
from sklearn.ensemble import RandomForestClassifier  
from sklearn.datasets import load\_iris  
from sklearn.metrics import accuracy\_score

\# Legt die Adresse des MLFlow Tracking Servers fest.  
\# Ohne diese Zeile würde MLFlow die Ergebnisse lokal in einem Ordner namens \`mlruns\` speichern.  
\# Die Verwendung eines zentralen Servers ist entscheidend für die Zusammenarbeit im Team.  
mlflow.set\_tracking\_uri("http://127.0.0.1:5000")

\# Erstellt ein neues Experiment, falls es nicht existiert, oder verwendet das bestehende.  
mlflow.set\_experiment("Iris Classification Experiment")

\# Daten laden  
iris \= load\_iris()  
X, y \= iris.data, iris.target  
X\_train, X\_test, y\_train, y\_test \= train\_test\_split(X, y, test\_size=0.2, random\_state=42)

\# Hyperparameter definieren  
params \= {  
    "n\_estimators": 100,  
    "max\_depth": 5,  
    "random\_state": 42  
}

\# Startet einen neuen MLFlow Run. Alle Protokollierungen innerhalb dieses Blocks  
\# werden diesem spezifischen Run zugeordnet.  
with mlflow.start\_run():  
    \# Parameter protokollieren  
    mlflow.log\_params(params)

    \# Modell trainieren  
    rf \= RandomForestClassifier(\*\*params)  
    rf.fit(X\_train, y\_train)

    \# Vorhersagen und Metriken berechnen  
    y\_pred \= rf.predict(X\_test)  
    acc \= accuracy\_score(y\_test, y\_pred)

    \# Metriken protokollieren  
    mlflow.log\_metric("accuracy", acc)

    \# Modell als Artefakt protokollieren, inklusive Signatur und Beispieldaten  
    \# für eine bessere Nachvollziehbarkeit der Ein- und Ausgabeformate.  
    mlflow.sklearn.log\_model(rf, "random-forest-model")

print(f"Accuracy: {acc}")  
print("Run completed. Check the MLflow UI at http://127.0.0.1:5000")

### **Schritt 3: Modell-Management mit der Registry (Phase C)**

Das beste Modell aus den durchgeführten Experimenten wird nun formal in der Model Registry registriert, um es für das Deployment verfügbar zu machen und seinen Lebenszyklus zu verwalten.

1. **Modell registrieren:** In der MLFlow-UI zum besten Run navigieren und unter "Artifacts" auf "Register Model" klicken. Dies ist der formale Akt der "Beförderung" eines experimentellen Modells zu einem Kandidaten für die Produktion.  
2. **Alias zuweisen:** Auf der "Models"-Seite dem Modell einen Alias wie production-candidate zuweisen. Dieser Alias signalisiert anderen Systemen (z.B. einer CI/CD-Pipeline), dass dieses Modell nun für weitere Tests und ein potenzielles Deployment bereitsteht.

### **Schritt 4: Erstellung der Web-App mit Streamlit (Phase K)**

Das Frontend der Anwendung wird mit Streamlit erstellt. Die App app.py lädt das registrierte Modell direkt aus der MLFlow Model Registry und stellt eine interaktive Benutzeroberfläche bereit.

import streamlit as st  
import pandas as pd  
import mlflow

\# Die Modell-URI verweist auf ein Modell in der Registry anhand seines Namens und eines Alias.  
\# Dies entkoppelt die App von spezifischen Modellversionen.  
MODEL\_URI \= "models:/iris-classifier@production-candidate"

st.title("Iris Flower Species Classifier")

\# Der @st.cache\_resource-Decorator sorgt dafür, dass das Modell nur einmal geladen  
\# und im Speicher gehalten wird, auch wenn der Nutzer mit der App interagiert.  
\# Dies verhindert langsame Ladezeiten bei jeder Aktion.  
@st.cache\_resource  
def load\_model():  
    return mlflow.pyfunc.load\_model(model\_uri=MODEL\_URI)

model \= load\_model()

\# Eingabefelder in der Seitenleiste  
st.sidebar.header("Input Features")  
sepal\_length \= st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.4)  
sepal\_width \= st.sidebar.slider("Sepal Width (cm)", 2.0, 4.5, 3.4)  
petal\_length \= st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 1.4)  
petal\_width \= st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

\# Eingabedaten als DataFrame erstellen, da scikit-learn-Modelle dies erwarten.  
input\_data \= pd.DataFrame({  
    'sepal length (cm)': \[sepal\_length\],  
    'sepal width (cm)': \[sepal\_width\],  
    'petal length (cm)': \[petal\_length\],  
    'petal width (cm)': \[petal\_width\]  
})

st.subheader("User Input Features")  
st.write(input\_data)

\# Button für die Vorhersage  
if st.button("Predict Species"):  
    prediction \= model.predict(input\_data)  
    target\_names \= \['setosa', 'versicolor', 'virginica'\]  
    \# model.predict() gibt ein Array zurück (z.B. \[2\]). Wir benötigen den ersten Wert für den Index.  
    predicted\_species \= target\_names\[prediction\[0\]\]  
    st.success(f"The predicted species is: \*\*{predicted\_species.capitalize()}\*\*")

### **Schritt 5: Deployment in der Streamlit Cloud (Phase K \- Continuous Delivery)**

1. **Vorbereitung:** requirements.txt erstellen (pip freeze \> requirements.txt) und den Code auf GitHub pushen.  
2. **Deployment:** Auf share.streamlit.io anmelden, das GitHub-Repository auswählen und die App deployen.

## **Literaturempfehlungen und weiterführende Ressourcen**

Um die in diesem Handout vorgestellten Konzepte zu vertiefen, wird die folgende Sammlung von Ressourcen empfohlen. Sie bietet Zugang zu offiziellen Dokumentationen, praktischen Anleitungen und aktiven Communitys.

### **Offizielle Projektseiten und Dokumentationen**

Dies sind die primären Quellen für verlässliche Informationen und sollten stets die erste Anlaufstelle sein.

* **MLFlow-Dokumentation:** [https://mlflow.org/docs/latest/index.html](https://mlflow.org/docs/latest/index.html)  
  * Die offizielle und umfassendste Ressource für alle MLFlow-Komponenten (Tracking, Projects, Models, Registry).  
* **Streamlit-Dokumentation:** [https://docs.streamlit.io/](https://docs.streamlit.io/)  
  * Enthält die API-Referenz, Anleitungen und fortgeschrittene Konzepte für die Erstellung von Streamlit-Apps.  
* **Scikit-learn-Dokumentation:** [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)  
  * Die unverzichtbare Referenz für die im Beispiel verwendeten Machine-Learning-Algorithmen und \-werkzeuge.

### **Tutorials und "How-To"-Anleitungen**

Diese Ressourcen bieten geführte Einführungen und praxisnahe Beispiele.

* **MLFlow Getting Started Guide:** [https://mlflow.org/docs/latest/getting-started/index.html](https://mlflow.org/docs/latest/getting-started/index.html)  
  * Ein schrittweises Tutorial, das die Kernkonzepte von MLFlow praktisch demonstriert.  
* **Streamlit Get Started:** [https://docs.streamlit.io/get-started](https://docs.streamlit.io/get-started)  
  * Eine interaktive Anleitung, die Sie in wenigen Minuten zur ersten eigenen Web-App führt.  
* **GitHub Guides:** [https://guides.github.com/](https://guides.github.com/)  
  * Essenzielle Anleitungen für den Einstieg in die Versionskontrolle mit Git und die Kollaboration über GitHub.

### **Communitys und weiterführende Konzepte**

Plattformen für den Austausch mit anderen Entwicklern und zur Inspiration.

* **MLOps Community:** [https://mlops.community/](https://mlops.community/)  
  * Eine globale Community mit einem Slack-Kanal, Meetups und vielen Ressourcen rund um das Thema MLOps.  
* **Streamlit Gallery:** [https://streamlit.io/gallery](https://streamlit.io/gallery)  
  * Eine kuratierte Sammlung beeindruckender Streamlit-Apps, die als Inspiration für eigene Projekte dienen kann.  
* **"Awesome MLOps" auf GitHub:** [https://github.com/visenger/awesome-mlops](https://github.com/visenger/awesome-mlops)  
  * Eine umfassende, von der Community gepflegte Liste von MLOps-Werkzeugen, Blogs, Büchern und anderen Ressourcen.

## **Schlussfolgerung: Den Vollen ML-Lebenszyklus Meistern**

Dieses Handout hat die Reise von einem traditionellen, linearen Prozessmodell wie QUA3CK hin zu einer modernen, MLOps-gesteuerten und zyklischen Entwicklungspipeline nachgezeichnet. Die Anreicherung der QUA3CK-Phasen mit den Prinzipien der Versionierung, Automatisierung, des Testings und der Governance \- umgesetzt mit Werkzeugen wie MLFlow und Streamlit \- transformiert den Entwicklungsprozess von einer Reihe manueller, fehleranfälliger Schritte zu einem integrierten, robusten und agilen Lebenszyklus. Es wird deutlich, dass ein erfolgreiches ML-Produkt weitaus mehr ist als nur ein genaues Modell; es ist ein zuverlässiges, wartbares und skalierbares System, das kontinuierlich überwacht und verbessert wird.

**Ihr Weg geht jetzt weiter:** Nutzen Sie das Gelernte als Ausgangspunkt:

* Experimentieren Sie mit anderen Algorithmen.  
* Fügen Sie weitere Features zur Streamlit-App hinzu (z.B. die Anzeige der Vorhersagewahrscheinlichkeiten).  
* Versuchen Sie, den gesamten Prozess von Training bis Deployment mit GitHub Actions zu automatisieren.  
* Untersuchen Sie fortgeschrittene Themen wie Data-Drift-Detektion oder A/B-Tests für Modelle.

Viel Erfolg auf Ihrer Reise zum MLOps-Experten\!