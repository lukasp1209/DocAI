# Handout: Der Modernisierte QUA³CK-Prozess - Von der Idee zur Cloud-App mit MLOps, MLflow und Streamlit {#handout}

## AMALEA 2025 Integration – Theoretisches Fundament für Portfolio-Projekte {#amalea-integration}

## Inhaltsverzeichnis {#toc}

- [Handout (Top)](#handout)
  - [Einleitung](#einleitung)
    - [🎯 AMALEA Portfolio Context](#portfolio-context)
    - [📹 AMALEA Video Integration](#video-integration)
  - [Teil 1: QUA³CK-Prozessmodell](#teil1)
    - [Phase Q](#phase-q)
    - [Phase U](#phase-u)
    - [Phase A³](#phase-a3)
    - [Phase C](#phase-c)
    - [Phase K](#phase-k)
  - [Teil 2: MLOps Grundlagen](#teil2)
  - [Teil 3: Synthese](#teil3)
  - [Teil 4: Praxis-Projekt](#teil4)
  - [Literatur & Ressourcen](#literatur)
  - [Schlussfolgerung](#schlussfolgerung)
  - [Nächste Schritte](#next-steps)




> 🎓 **Für AMALEA-Studierende**: Dieses Handout bildet die theoretische Grundlage für eure **24 Portfolio-Komponenten**  
> 🎥 **Video-Integration**: Kombiniert mit **22 originalen AMALEA-Videos** aus 2021  
> 🚀 **Portfolio-Ready**: Direkter Bezug zu euren **8 Streamlit Cloud Apps** und **IU-Fallstudien**

## Einleitung: Die Evolution der Entwicklung im Maschinellen Lernen {#einleitung}

Die Entwicklung von Anwendungen des Maschinellen Lernens (ML) hat sich in den letzten Jahren fundamental gewandelt. Die zentrale Herausforderung in vielen ML-Projekten liegt heute weniger in der Auswahl des perfekten Algorithmus, sondern vielmehr im umgebenden Engineering. Zahlreiche vielversprechende Prototypen, die oft in Umgebungen wie Jupyter-Notebooks entstehen, erreichen niemals den produktiven Einsatz. Dieses Phänomen, oft als "Prototyping-Falle" oder "Proof-of-Concept-Gefängnis" bezeichnet, entsteht, weil die für die explorative Analyse optimierten Werkzeuge und Prozesse nicht für die Anforderungen eines stabilen, skalierbaren und wartbaren Betriebs ausgelegt sind. Der Grund hierfür ist häufig das Fehlen von strukturierten, reproduzierbaren und wartbaren Prozessen, die für den Übergang von der Forschung in den Betrieb unerlässlich sind.

An dieser Stelle setzt das am Karlsruher Institut für Technologie (KIT) entwickelte Vorgehensmodell QUA3CK an. Es bietet einen didaktischen und praxisorientierten Rahmen für ML-Projekte und gliedert diese in klar definierte Phasen. Dieses Modell liefert eine wertvolle Struktur, insbesondere für Einsteiger und in akademischen Kontexten. Es stößt jedoch in der modernen, agilen Softwareentwicklung an Grenzen, wenn es um Skalierbarkeit, Automatisierung und kontinuierliche Verbesserung geht. Der klassische QUA3CK-Prozess behandelt die Phasen oft als sequenzielle Schritte, was in der Praxis zu langen Entwicklungszyklen und einer schwierigen Wartung führt.

**AMALEA 2025** baut direkt auf diesem bewährten Fundament auf: Das **"Angewandte Machine Learning Algorithmen"** Programm des KI-Campus wird mit QUA³CK-Prinzipien und modernen MLOps-Praktiken kombiniert. So entsteht ein Kurs, der theoretische Klarheit mit industrieller Praxistauglichkeit verbindet.

### 🎯 AMALEA Portfolio Context {#portfolio-context}

Für **AMALEA-Studierende der IU** ist dieses Handout direkt **portfoliorelevant**:

- **QUA³CK als Struktur**: Jede Portfolio-Komponente folgt den 6 QUA³CK-Schritten
- **MLOps als Standard**: Model Tracking, Versioning und Deployment Best Practices
- **Streamlit als Platform**: 8 interaktive Apps für Streamlit Cloud
- **Big 3 Integration**: Decision Trees, KNN, K-Means mit MLflow Tracking
- **IU Assessment**: Erfüllung aller Bewertungskriterien durch strukturierten Ansatz

### 📹 AMALEA Video Integration {#video-integration}

Die **22 originalen AMALEA-Videos** aus **2021-2025** werden systematisch in den MLOps-Workflow integriert:

- **Videos 1-7**: QUA³CK Foundation und Python Basics
- **Videos 8-14**: Big 3 Algorithms mit MLflow Tracking  
- **Videos 15-22**: Deployment, Portfolio und Assessment

Diese Video-Roadmap sorgt dafür, dass ihr Theorie, praktische Umsetzung und Portfolio-Anwendung nicht getrennt, sondern als zusammenhängenden Lernpfad erlebt. Jede neue technische Komponente (z.B. Tracking, Registry, Deployment) wird didaktisch vorbereitet und direkt praktisch gefestigt.

Die Brücke zwischen der strukturierten Planung von QUA3CK und den Anforderungen der modernen Softwareentwicklung schlägt Machine Learning Operations (MLOps). MLOps wendet die bewährten Prinzipien von DevOps (Kollaboration, Automatisierung, iterative Verbesserung) auf den gesamten Lebenszyklus von ML-Modellen an. Es liefert damit die notwendige Engineering-Disziplin, um die in QUA3CK definierten Ziele in der Praxis umzusetzen - und das skaliert, automatisiert und kontinuierlich. MLOps ist keine bloße Werkzeugsammlung, sondern eine Kultur und ein Methodenset, das darauf abzielt, die Lücke zwischen der experimentellen Welt der Entwicklung (Data Science) und der stabilen Welt des Betriebs (Operations) systematisch zu schließen.

Dieses Handout führt euch durch die Modernisierung des QUA³CK-Prozessmodells mit MLOps-Praktiken. Ihr lernt nicht nur die Theorie, sondern wendet diese auch praktisch an, um eine robuste ML-Anwendung zu entwickeln und als interaktive Web-App bereitzustellen. Am Ende versteht ihr, wie aus einem starren, linearen Prozess ein dynamischer, sich selbst verbessernder Kreislauf wird.

**Für AMALEA-Studierende** dient dieses Handout als theoretisches Fundament für alle **24 Portfolio-Komponenten** (16 Notebooks + 8 Streamlit Apps). Die hier vorgestellten Konzepte werden in den praktischen Notebooks der Wochen 1, 4 und 7 direkt umgesetzt und bereiten optimal auf die **IU-Fallstudien** vor.

## Teil 1: Das Fundamentale QUA³CK-Prozessmodell {#teil1}

> 🎥 **AMALEA Video-Integration**: Die folgenden Konzepte werden durch **originale AMALEA-Videos** aus 2021 vertieft  
> 🚀 **Portfolio-Kontext**: Diese Phasen strukturieren eure **IU-Fallstudien** und **Streamlit Cloud Apps**

Das QUA³CK-Modell ist ein Akronym, das die fünf Hauptphasen des Entwicklungsprozesses beschreibt. Die einzelnen Phasen werden nachfolgend anhand eines durchgehenden, klassischen Beispiels erläutert: der Klassifikation von Iris-Blüten. Es ist wichtig zu verstehen, dass diese Phasen in der Realität nicht streng getrennt sind, sondern sich oft überlappen und Iterationen erfordern.

**AMALEA-Integration**: In den praktischen Notebooks werden diese Konzepte mit modernen Technologien wie **Docker**, **Streamlit** und **Hugging Face** umgesetzt.

- **Q** - Question (Fragestellung)
- **U** - Understanding the data (Datenverständnis)
- **A³** - Algorithm selection, Adapting features, Adjusting hyperparameters (Die A-Schleife)
- **C** - Conclude and compare (Schlussfolgerung und Vergleich)
- **K** - Knowledge transfer (Wissenstransfer)

### Phase Q - Question (Fragestellung) {#phase-q}

> 🎯 **AMALEA-Kontext**: Dies entspricht der **Fallstudien-Definition** im IU-Assessment!

Jedes Projekt beginnt mit einer klar definierten Frage oder einem Problem, das gelöst werden soll. Eine unklare Fragestellung ist einer der häufigsten Gründe für das Scheitern von ML-Projekten. In dieser initialen Phase ist es entscheidend, nicht nur die technischen, sondern auch die geschäftlichen Ziele, Anforderungen, Randbedingungen und erwarteten Ergebnisse (Key Performance Indicators, KPIs) festzulegen. Dies verhindert, dass Spezifikationen zu spät geklärt werden oder das Endprodukt die eigentlichen Bedürfnisse der Anwender verfehlt.

**Für AMALEA-Studierende**: Eure Fallstudien müssen eine **öffentlich zugängliche Streamlit Cloud App** und ein **GitHub Portfolio-Repository** umfassen. Die Problemstellung sollte als **Vorstudie für euer Bachelorprojekt** geeignet sein.

**Beispiel (Iris-Klassifikator):**

- **Problemstellung:** Eine Anwendung soll Iris-Pflanzen basierend auf den Merkmalen ihrer Blüten (Kelch- und Kronblattlänge sowie -breite) automatisch einer von drei Spezies zuordnen: Setosa, Versicolor oder Virginica. Die Anwendung soll von Botanik-Studenten genutzt werden, um bei der Feldarbeit schnell eine Einschätzung zu erhalten.
- **Anforderungen & KPIs:** Das entwickelte Modell soll eine Klassifikationsgenauigkeit (Accuracy) von über 95% auf bisher ungesehenen Daten erreichen. Die Vorhersagezeit pro Pflanze muss unter 500 Millisekunden liegen, um eine flüssige Benutzererfahrung zu gewährleisten.

**Warum diese Phase kritisch ist:** Unklare Ziele führen downstream zu ineffizientem Feature Engineering, zu breiten Suchräumen beim Modellieren und zu fehlgeleiteter Optimierung. Eine halbe Stunde mehr Präzision hier spart oft Tage später.

**Typische Stolpersteine:**
 
- Vage KPI ("hohe Genauigkeit") statt messbarer Schwelle
- Keine Definition von Constraints (Latenz, Speicher, Interpretierbarkeit)
- Keine frühe Abstimmung mit Stakeholdern → spätere Revisionsschleifen

**Mini-Checkliste:** Wer? Was? Warum jetzt? Erfolg wann messbar? Risiken? Abbruchkriterien?

### Phase U - Understanding the data (Datenverständnis) {#phase-u}

> 📊 **AMALEA Big Data Integration**: Nutzt [Kaggle](https://kaggle.com/datasets), [AWS Open Data](https://registry.opendata.aws/), [Google Dataset Search](https://datasetsearch.research.google.com/) für eure Projekte!

Diese Phase konzentriert sich auf die Daten selbst – das Herzstück jedes ML-Modells. Falls kein Datensatz vorhanden ist, muss dieser zunächst erhoben werden. Anschließend werden die Rohdaten mittels explorativer Datenanalyse (EDA) analysiert, um verborgene Informationen, Muster, Trends oder irrelevante Daten zu entdecken. Dies umfasst statistische Analysen (Mittelwert, Korrelation), Visualisierungen und die essenzielle Datenvorverarbeitung (Umgang mit fehlenden Werten, Ausreißern, Normalisierung, Data Augmentation). Die Qualität der Daten bestimmt maßgeblich die Obergrenze für die Leistungsfähigkeit des späteren Modells.

**AMALEA-Ressourcen**: Der Kurs stellt **diverse Big Data Quellen** bereit - von **Finanzdaten** (Yahoo Finance) über **wissenschaftliche Datasets** (NASA, UCI) bis zu **Social Media APIs** (Reddit, Spotify) für authentische Portfolio-Projekte.

**Beispiel (Iris-Klassifikator):**

- **Datenanalyse:** Der bekannte Iris-Datensatz wird geladen. Mittels deskriptiver Statistik und Visualisierungen (z.B. Scatter-Plots, Box-Plots) werden die Verteilungen und Korrelationen der Merkmale (`sepal_length`, `sepal_width`, `petal_length`, `petal_width`) untersucht. Es wird festgestellt, dass `petal_length` und `petal_width` stark korrelieren und eine gute Trennung der Klassen ermöglichen.
- **Datenvorverarbeitung:** Der Datensatz wird auf fehlende Werte überprüft (im Iris-Datensatz sind keine vorhanden). Es wird analysiert, ob Ausreißer existieren, die das Training beeinträchtigen könnten. Eine Skalierung der Features (z.B. Standardisierung) wird in Betracht gezogen, um sicherzustellen, dass alle Merkmale einen ähnlichen Einfluss auf das Modell haben, was besonders für abstandsbasierte Algorithmen wichtig ist.

**Vertiefung:** Datenverständnis ist nicht einmalig. Schon erste Modell-Runs geben Hinweise (Feature Importance, Fehlklassifikationen), die zurück in weitere Exploration fließen. Deshalb: EDA artefaktisieren (Notebooks versionieren, Abbildungen ablegen) und wichtige Kennzahlen (Verteilungen, Korrelationen) als Referenz für späteres Drift-Monitoring sichern.

**Praktische Hinweise:**
 
- Früh ein initiales Daten-Profiling (z.B. mit pandas-profiling/Great Expectations) generieren.
- Potenzielle Leaks markieren (z.B. Zielspalte in abgeleiteten Features versehentlich eingegangen?).
- Segmentierung vorbereiten (z.B. Gruppen-Attribute für Fairness später extrahieren).

### Phase A³ - Die iterative A-Schleife {#phase-a3}

> 🎯 **AMALEA "Big 3"**: In **Woche 4** lernt ihr die drei wichtigsten ML-Algorithmen: **Decision Trees**, **K-Nearest Neighbors** und **K-Means Clustering**!

Diese drei Schritte – Algorithmusauswahl, Feature-Anpassung und Hyperparameter-Optimierung – bilden den iterativen Kernzyklus der Modellentwicklung. Es ist entscheidend zu verstehen, dass dies kein linearer Ablauf ist, sondern eine Schleife, die so oft durchlaufen wird, bis das Modell die gewünschten Ergebnisse liefert. In der Praxis ist dies oft der zeitaufwändigste Teil eines ML-Projekts.

**AMALEA-Erweiterung**: Zusätzlich zu klassischen Algorithmen lernt ihr **Neural Networks** (Woche 5), **Computer Vision mit CNNs** (Woche 6) und **moderne NLP mit Transformers** (Woche 6). Alle Experimente werden mit **MLflow Tracking** dokumentiert für professionelle Portfolio-Präsentation.

1. **Algorithm selection and training (Algorithmusauswahl und Training):** Basierend auf der Problemstellung (Klassifikation, Regression etc.), der Datenmenge und -art wird ein passender Algorithmus ausgewählt. Die Auswahl reicht von einfachen linearen Modellen bis hin zu komplexen tiefen neuronalen Netzen. Das Modell wird dann auf den aufbereiteten Trainingsdaten trainiert.

2. **Adapting the features (Datenanpassung/Feature Engineering):** Der Datensatz wird an die spezifischen Anforderungen des gewählten Algorithmus angepasst. Dies kann die Umstrukturierung von Daten, das Erstellen neuer Merkmale aus bestehenden (z.B. Polynom-Features) oder die Reduktion von Merkmalen umfassen, um Überanpassung zu vermeiden.

3. **Adjusting the hyperparameters (Hyperparameter-Anpassung):** Hyperparameter sind die "Stellschrauben" eines Modells, die nicht während des Trainings gelernt werden (z. B. Lernrate, Anzahl der Schichten in einem neuronalen Netz). Optimierung erfolgt manuell oder durch automatisierte Verfahren wie Grid Search oder Bayesian Optimization, um die Modellleistung zu maximieren.

**Beispiel (Iris-Klassifikator):**

- **A1 - Algorithmusauswahl:** Ein RandomForestClassifier aus scikit-learn wird als geeigneter, robuster Algorithmus für dieses tabellarische Klassifikationsproblem ausgewählt. **AMALEA-Erweiterung**: In Woche 4 vergleichen wir systematisch die "Big 3" Algorithmen, in Woche 5 ergänzen wir Neural Networks und in Woche 6 nutzen wir CNNs für Computer Vision.
- **A2 - Datenanpassung:** Für den Random Forest sind die Daten bereits in einem passenden Format. **AMALEA-Praxis**: In den Streamlit-Apps lernt ihr interaktive Feature Engineering Tools und Data Augmentation für Computer Vision.
- **A3 - Hyperparameter-Anpassung:** Die Hyperparameter des Modells, wie die Anzahl der Bäume (`n_estimators`) und die maximale Tiefe der Bäume (`max_depth`), werden durch systematisches Ausprobieren verschiedener Werte optimiert. **MLflow Integration**: Alle Experimente werden automatisch getrackt und sind über das MLflow UI vergleichbar.

Dieser Zyklus wird wiederholt, wobei die Leistung des Modells auf einem separaten Validierungsdatensatz gemessen wird, um eine Überanpassung an die Trainingsdaten zu vermeiden.

**Strategischer Fokus:** Ziel ist nicht das theoretisch beste Modell, sondern das passendste unter realen Constraints (Interpretierbarkeit, Kosten, Update-Frequenz). Ein leicht schwächeres, aber robusteres und schneller trainierbares Modell kann produktiv überlegen sein.

**Iterative Taktik:**
 
 1. Baseline (z.B. LogReg / Simple Tree) → Metriken festhalten
 2. Feature-Ideen bewerten (Hypothese → Experiment → Logging)
 3. Hyperparameter-Suche erst ausweiten, wenn Feature-Raum stabil
 4. Komplexität nur erhöhen, wenn Gap zu Ziel-KPI sonst nicht schließbar

**Overfit-Früherkennung:** Track Trainings- vs. Validierungs-Metrik Delta. Ab Delta > 0.03: Frühzeitig Regularisierung / Datenanreicherung / Feature-Reduktion prüfen.

### Phase C - Conclude and compare (Schlussfolgerung und Vergleich) {#phase-c}

In dieser Phase wird die Generalisierungsfähigkeit des final trainierten Modells auf einem separaten Testdatensatz bewertet, den das Modell während des gesamten Entwicklungszyklus noch nie gesehen hat. Die Ergebnisse werden mit den in Phase Q definierten KPIs und eventuell mit Referenzmodellen ("Baselines") verglichen. Wenn die Leistung nicht ausreicht, muss zur A³-Schleife zurückgekehrt werden.

**Beispiel (Iris-Klassifikator):**

- Das optimierte RandomForestClassifier-Modell wird auf das Test-Set angewendet.
- Die Genauigkeit wird berechnet und eine Confusion Matrix erstellt, um die Leistung im Detail zu analysieren (z.B. welche Klassen am häufigsten verwechselt werden).
- Es wird festgestellt, dass das Modell die KPI von >95% Genauigkeit erfüllt. Die Vorhersagezeit wird ebenfalls gemessen und als zufriedenstellend bewertet.

**Bewertungssystem etablieren:** Nutzt konsistente Vergleichstabellen (Run-ID, Accuracy, F1, Latenz, Modellgröße). Ergänzt qualitative Faktoren (Erklärbarkeit, Stabilität). Ziel: Promotion-Entscheidung nachvollziehbar dokumentieren.

**Output dieser Phase:**
 
- Bestes Modell + Metrik-Snapshot
- Entscheidungsprotokoll (warum dieses Modell)
- Offene Risiken (z.B. Performance auf seltenen Segmenten)

### Phase K - Knowledge transfer (Wissenstransfer) {#phase-k}

Sobald das Modell die Anforderungen erfüllt, ist es aus Entwicklungssicht "fertig". Diese letzte, oft vernachlässigte Phase umfasst die detaillierte Dokumentation des gesamten Prozesses (Algorithmus, finale Parameter, Datensätze, Vorverarbeitungsschritte) zur Sicherstellung der Replizierbarkeit und die Bereitstellung (Deployment) des Modells auf einer Zielplattform, z.B. als API-Endpunkt in der Cloud oder integriert in eine mobile App.

**Beispiel (Iris-Klassifikator):**

- Die finalen Hyperparameter, der Trainingsprozess, die Leistungskennzahlen und die Feature-Wichtigkeiten werden in einem Report dokumentiert.
- Das trainierte Modell wird als Datei (z.B. mittels pickle oder joblib) gespeichert, um es in einer Anwendung - wie der später entwickelten Streamlit-App - wiederzuverwenden.

**Ziel dieser Phase:** Nachhaltigkeit & Skalierbarkeit sichern. Wissen raus aus Köpfen, rein in Artefakte + automatisierte Prozesse.

**Essentielle Artefakte:**
 
- Repro-Befehl (Trainingskommando + Parameter)
- Datenversion (Commit / Hash / Storage-Pfad)
- Modell-Signatur & Inputschema
- Entscheidungskriterien (Promotion Notes)

**Hand-Off Anti-Pattern:** Nur ein Notebook + gespeichertes Modell. → Besser: Skript + Tests + README mit klarer Deploy-Anleitung.

## Teil 2: MLOps - Engineering-Disziplin für Maschinelles Lernen {#teil2}

MLOps führt eine Reihe von Kernprinzipien ein, die für die Modernisierung und Skalierung des QUA³CK-Prozesses unerlässlich sind. Diese Prinzipien transformieren die traditionellen, oft manuellen Phasen in einen dynamischen, automatisierten und robusten Lebenszyklus.

### Kernprinzip 1: Versionierung (Code, Daten, Modelle)

MLOps erweitert die klassische Code-Versionierung mit Werkzeugen wie Git auf alle Artefakte des ML-Prozesses. Dies bedeutet, dass nicht nur der Code, sondern auch die verwendeten Datensätze, die Feature-Engineering-Pipelines und die trainierten Modelle selbst versioniert werden. Die Versionierung aller Komponenten ist die unabdingbare Grundlage, um eine ML-Pipeline vollständig reproduzierbar zu machen. Wenn ein Fehler auftritt oder ein Modell unerwartete Vorhersagen liefert, ermöglicht diese lückenlose Historie eine exakte Rekonstruktion des Zustands und eine schnelle Fehleranalyse. Dies ist entscheidend für Audits, das Debugging von Fehlern und die kollaborative Arbeit im Team.

**Good Practice Layering:**
 
- Code: Git + konventionelle Branch-Strategie (feat/, fix/, exp/)
- Daten: Hash-basierte Speicherung (DVC, Lake, Object Store Pfade mit Versionssuffix)
- Features: Explizite Transformationen (Pipelines) statt adhoc Notebook-Zellen
- Modelle: Registry mit Alias (staging/production/champion)

**Risiken ohne Versionierung:** Nicht reproduzierbare Fehler, inkonsistente Retrains, Audit-Blocker.

### Kernprinzip 2: Automatisierung & Continuous X (CI/CD/CT/CM)

Die Automatisierung von wiederkehrenden Aufgaben ist ein zentrales Anliegen von MLOps, um manuelle Fehler zu reduzieren, die Konsistenz zu erhöhen und den Entwicklungszyklus zu beschleunigen. Diese Automatisierung manifestiert sich in den "Continuous"-Praktiken, die einen geschlossenen Kreislauf bilden:

- **Continuous Integration (CI):** Geht über das reine Testen von Code hinaus. Bei jeder Code-Änderung werden automatisch Datenvalidierungstests, Tests der Trainingspipeline und grundlegende Modell-Qualitätsprüfungen ausgeführt.
- **Continuous Delivery (CD):** Die automatisierte Bereitstellung des gesamten Systems, einschließlich des trainierten und validierten Modells als Vorhersagedienst (Prediction Service) in einer Test- oder Produktionsumgebung.
- **Continuous Training (CT):** Das automatische Neutrainieren von Modellen, sobald neue relevante Daten verfügbar sind oder die Modellperformance in der Produktion nachlässt. Dies ist die direkte Antwort auf das Problem des "Model Decay" oder der Modellalterung und sorgt dafür, dass Modelle relevant bleiben.
- **Continuous Monitoring (CM):** Die kontinuierliche Überwachung der technischen und statistischen Performance des Modells in der Produktionsumgebung. Dies dient dazu, Probleme wie "Model Drift" (eine Veränderung in der Verteilung der Eingabedaten) oder "Concept Drift" (eine Veränderung der Beziehung zwischen Ein- und Ausgabedaten) proaktiv zu erkennen und ggf. ein Retraining (CT) auszulösen.

**Automatisierungs-Priorisierung (Start klein):**
 
 1. Tests + Lint + Simple Train Job
 2. Modell-Registrierung + Alias Promotion
 3. Container Build + Security Scan
 4. Drift / Fairness Gates
 5. Periodisches Retraining / Canary Deployments

**Anti-Pattern:** Alles manuell triggern → sporadische Qualität. Vollautomatisierung ohne Quality Gates → Risiko stiller Degradierung.

### Kernprinzip 3: Testing im ML-Kontext

Testing in ML-Projekten ist weitaus umfassender als klassische Unit- und Integrationstests, da es sich mit der inhärenten Unsicherheit von Daten und Modellen befassen muss. Es beinhaltet spezifische Tests für die verschiedenen Artefakte und Phasen des ML-Lebenszyklus:

- **Datenvalidierung:** Automatische Überprüfung von Datenschemata (sind alle Spalten vorhanden?), Verteilungen (entspricht die Verteilung der neuen Daten der der Trainingsdaten?) und statistischen Eigenschaften.
- **Modellvalidierung:** Überprüfung der Generalisierungsfähigkeit des Modells nicht nur auf dem gesamten Testset, sondern auch auf wichtigen, vordefinierten Datensegmenten (z.B. für verschiedene Benutzergruppen), um versteckte Schwächen aufzudecken.
- **Fairness- und Bias-Tests:** Sicherstellung, dass das Modell keine unterrepräsentierten Gruppen systematisch benachteiligt. Es wird geprüft, ob die Fehlerraten über verschiedene demografische Gruppen hinweg ähnlich sind.
- **Infrastruktur- und Stresstests:** Prüfung, ob die Trainings- und Serving-Infrastruktur unter Last stabil bleibt und die in Phase Q definierten Latenzanforderungen erfüllt.
- **Konsistenztests:** Ein wichtiger Test validiert, dass ein Modell für dieselbe Eingabe in der Trainingsumgebung und in der Serving-Umgebung exakt dieselbe Vorhersage liefert. Abweichungen deuten auf subtile Engineering-Fehler hin, z.B. unterschiedliche Versionen von Abhängigkeiten.

**Test-Pyramide (ML):**
 
- Basis: Daten- und Schema-Checks
- Mitte: Modell-Qualitäts- & Fairness-Tests
- Spitze: Pipeline / End-to-End (Train → Serve)

**Schlanke Einführung:** Startet mit 4 Kernfällen (Schema, Min Accuracy, Konsistenz, Negative Input). Dann iterativ erweitern.

### Kernprinzip 4: Modell-Governance & Reproduzierbarkeit

Governance umfasst die Verwaltung aller Aspekte von ML-Systemen, um Effizienz, Sicherheit und die Einhaltung von Vorschriften (Compliance) zu gewährleisten. Dies beinhaltet klare Prozesse für die Freigabe von Modellen, das Management von Zugriffsrechten und die Sicherstellung ethischer Richtlinien. Reproduzierbarkeit ist dabei kein isoliertes Prinzip, sondern das synergetische Ergebnis der konsequenten Anwendung von Versionierung, Automatisierung und Testing. Ein Governance-Framework definiert, wer ein Modell in die Produktion überführen darf und welche Qualitätskriterien dafür erfüllt sein müssen. MLOps-Werkzeuge helfen dabei, diese Regeln automatisiert durchzusetzen.

**Governance-Artefakte:**
 
- Promotion Checklist (Metriken, Drift OK, Fairness OK, Security Scan pass)
- Audit Log (Wer hat wann promoted?)
- Policy für Rückroll (Alias-Revert, Canary Abschaltung)

**Reproduzierbarkeits-Bausteine:** Seeds, klare Abhängigkeits-Pins, unveränderliche Daten-Snapshots, deklarative Pipelines.

## Teil 3: Synthese - Integration von MLOps in den QUA³CK-Prozess {#teil3}

In diesem zentralen Abschnitt wird gezeigt, wie die MLOps-Prinzipien die traditionellen QUA³CK-Phasen transformieren und anreichern. Die folgende Tabelle dient als didaktische Referenz, die den Mehrwert von MLOps in jeder Phase auf einen Blick verdeutlicht und eine Brücke zur praktischen Umsetzung schlägt.

| Phase (QUA³CK) | Traditionelle Aktivität (gemäß QUA³CK) | Modernisierte (MLOps) Aktivität | Key Tools |
|---|---|---|---|
| Q-Question & U-Understanding | Manuelle Anforderungsanalyse, statische KPIs in einem Dokument. EDA in einem Notebook, manuelle Datenbereinigung, Pre-Processing. | Kollaborative Definition in einem Wiki, KPIs als Metriken für automatisches Monitoring definieren. Automatisierte Datenvalidierungs-Pipelines, Nutzung eines Feature Stores, Daten-Versionierung. | Git, Confluence, Great Expectations, DVC, Feast |
| A³ - The A-Loop | Manuelles Experimentieren: Algorithmus wählen, Daten anpassen, Hyperparameter tunen. Lokales Training, Speichern als .pkl. | Experiment-Tracking, Code in modularer, testbarer Form, automatisierte Trainingspipeline (CI/CT). | MLflow Tracking, Pytest, Docker, Jenkins/GitHub Actions |
| C- Conclude & Compare | Manuelle Validierung auf Test-Set, Vergleich in Excel/Report. | Automatisierte Modellvalidierung in CI/CD-Pipeline, zentraler Vergleich von Metriken. | MLflow UI, CI/CD-Tools |
| K - Knowledge Transfer | Manuelle Übergabe des Modells, statische Dokumentation, manuelles Deployment. | Zentrales Modell-Management (Registry), geregelte Staging/Production-Übergänge, kontinuierliches Monitoring, automatisiertes Deployment. | MLflow Model Registry, Prometheus/Grafana, Streamlit |

### Deep Dive: Modernisierung der A³-Schleife mit MLflow Tracking

Mit MLOps ändert sich das Paradigma der A³-Schleife fundamental: Es geht nicht mehr nur darum, ein Skript zu schreiben und es auszuführen, sondern darum, ein nachvollziehbares und **reproduzierbares Experiment** durchzuführen. Das Open-Source-Framework MLflow bietet hierfür mit seiner Tracking-Komponente ein mächtiges Werkzeug, das als zentrales Laborbuch für alle Modellentwicklungsaktivitäten dient.

MLflow Tracking organisiert die Modellentwicklung um folgende Kernkonzepte:

- **Experiment:** Ein logischer Container für zusammengehörige Durchläufe, z.B. "Optimierung des Iris-Klassifikators" oder "Test verschiedener Architekturen".
- **Run:** Eine einzelne Ausführung des Trainingscodes. Jeder Run erhält eine eindeutige ID und wird mit allen zugehörigen Informationen aufgezeichnet.
- **Parameter (log_param):** Die Eingaben des Experiments werden protokolliert. Dies sind typischerweise die Hyperparameter des Modells (z.B. max_depth) oder Merkmale der Eingabedaten (z.B. feature_set_version).
- **Metriken (log_metric):** Die quantitativen Ergebnisse des Experiments werden aufgezeichnet, z.B. die accuracy oder der f1_score auf dem Test-Set. Metriken können über die Zeit protokolliert werden (z.B. der Trainingsverlust pro Epoche), um Lernkurven zu visualisieren.
- **Artefakte (log_artifact/log_model):** Beliebige Ausgabedateien können gespeichert werden. Am wichtigsten ist hier das trainierte Modell selbst, aber auch Visualisierungen (z.B. eine Confusion Matrix), Datensätze oder Log-Dateien können als Artefakte abgelegt werden.

Der unschätzbare Vorteil: Jeder Trainingslauf wird mit seinen Ein- und Ausgaben exakt und unveränderlich dokumentiert. MLflow bietet eine Web-UI, in der verschiedene Runs bequem verglichen werden können (z.B. durch Sortieren nach der besten Metrik oder durch parallele Darstellung von Graphen), um das beste Modell objektiv zu identifizieren.

### Deep Dive: Modernisierung von C & K mit der MLflow Model Registry

Auch die Phasen C (Conclude) und K (Knowledge Transfer) erfahren eine Transformation. Der manuelle Vergleich und die Übergabe eines Modells werden durch einen zentralisierten, versionierten und governance-gesteuerten Prozess ersetzt. Die **MLflow Model Registry** ist ein zentralisierter Speicher, der genau diesen Lebenszyklus verwaltet und als "Single Source of Truth" für produktionsreife Modelle dient.

Die Schlüsselkonzepte der Model Registry sind:

- **Registered Model:** Ein eindeutig benanntes Modell im Registry, z.B. iris-classifier. Es dient als Container für alle Versionen dieses spezifischen Modells.
- **Model Version:** Jedes Mal, wenn ein neues Modell unter diesem Namen registriert wird (z.B. nach einem Retraining mit neuen Daten), wird eine neue, inkrementelle Version erstellt (Version 1, Version 2,...). Dies ermöglicht eine lückenlose und nachvollziehbare Modell-Historie.
- **Model Alias (MLflow 2.x):** Ein veränderbarer "Zeiger" oder "Tag" (z.B. `@champion`, `@challenger`), der auf eine bestimmte Modellversion verweist. **Moderne Syntax**: `models:/iris-classifier@production` statt der veralteten Stage-basierten Notation. Aliase werden verwendet, um Umgebungen flexibel abzubilden (development, staging, production) und ermöglichen Blue-Green-Deployments durch einfaches Umsetzen der Aliases.

## Teil 4: Praxis-Projekt - Entwicklung und Deployment einer Iris-Klassifikator-App {#teil4}

Diese detaillierte Schritt-für-Schritt-Anleitung führt durch das gesamte Projekt und verbindet die Theorie mit der praktischen Anwendung.

### Schritt 1: Projekt-Setup (Phase Q, U)

1. **Verzeichnis anlegen und Git initialisieren:**

  Wir beginnen minimal: Ein isoliertes Projektverzeichnis plus Git-Versionierung bildet das Rückgrat für Nachvollziehbarkeit und spätere CI/CD Automatisierung.

  ```bash
  mkdir ml-app && cd ml-app
  git init
  ```
  Danach direkt ein erster Commit (README, leere `requirements.txt`) – so lässt sich jede folgende Änderung granular vergleichen.

1. **Docker-basierte Entwicklungsumgebung (Empfohlen für AMALEA):**
   
   **Profi-Tipp: Warum Docker?**
   
   Docker garantiert, dass Ihre ML-Anwendung in jeder Umgebung identisch läuft - von der lokalen Entwicklung bis zur Streamlit Community Cloud. Dies eliminiert das berüchtigte "Works on my machine"-Problem und ist essentiell für reproduzierbare ML-Experimente.

  Erstellt eine gehärtete `Dockerfile`:

  ```dockerfile
   FROM python:3.11-slim AS base
   ENV PYTHONDONTWRITEBYTECODE=1 \
     PYTHONUNBUFFERED=1 \
     PIP_NO_CACHE_DIR=1

   RUN apt-get update && apt-get install -y --no-install-recommends \
     build-essential gcc g++ curl git libgomp1 \
     && rm -rf /var/lib/apt/lists/*

   WORKDIR /app
   COPY requirements.txt ./
   RUN pip install --upgrade pip && pip install -r requirements.txt

   RUN useradd -m appuser && chown -R appuser /app
   USER appuser

   COPY --chown=appuser:appuser . .
   EXPOSE 8501
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
  ```

  Optional: .gitignore hinzufügen:

  ```gitignore
   __pycache__/
   *.pyc
   .venv/
   mlruns/
   .pytest_cache/
   .DS_Store
   .env
   ```

1. **Alternative: Virtuelle Umgebung erstellen und aktivieren:**

   **Profi-Tipp:** Warum eine virtuelle Umgebung?
   
   Eine virtuelle Umgebung (wie venv) isoliert die für dieses Projekt benötigten Python-Pakete von anderen Projekten auf Ihrem System. Das verhindert Konflikte zwischen Paketversionen (z.B. Projekt A benötigt pandas 1.5, Projekt B aber pandas 2.0) und stellt sicher, dass Ihr Projekt (und die requirements.txt-Datei) nur die wirklich notwendigen Abhängigkeiten enthält. Dieser Schritt ist fundamental für die Reproduzierbarkeit!

1. **Abhängigkeiten installieren:**

  ```bash
  # Core ML/Data Science Stack
  pip install streamlit>=1.28.0 pandas>=2.0.0 scikit-learn>=1.3.0 mlflow>=2.8.0

  # Development and Testing
  pip install pytest>=7.0.0 great-expectations>=0.17.0

  # Optional: Docker integration
  pip install docker>=6.0.0
  ```

1. **Versionierung & Constraints (empfohlen):**

  Für reproduzierbare Builds erstellt ihr eine `constraints.txt`:

  ```text
  streamlit==1.31.0
  pandas==2.0.3
  scikit-learn==1.3.2
  mlflow==2.9.0
  numpy==1.26.4
  pytest==8.0.0
  great-expectations==0.18.5
  ```

  Installation dann z.B.:

  ```bash
  pip install -r constraints.txt
  ```

1. **(Optional) Security & Supply Chain:** Signierte Pakete (`pip --require-hashes`) und Vulnerability Scan (`pip-audit`) integrieren.

### Schritt 2: Experiment-Tracking mit MLflow (Phase A³)

Aktualisierte, fehlertolerante Version von `train.py` mit klarer Signatur und robustem Logging:

Strukturüberblick vor dem Code:

- Konfiguration des Tracking Servers (lokal) + Experimentnamen
- Datensicherheits-Gates (leer / NaN) verhindern Silent Fails
- Stratified Split für faire Klassifikationsverteilung
- Parametrisierung + Logging (Param + Metrik + Artefakt Report)
- Signatur-Inferenz für späteres sicheres Laden in der App

```python
import mlflow
import logging
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

acc = None

try:
  mlflow.set_tracking_uri("http://127.0.0.1:5000")
  mlflow.set_experiment("Iris Classification Experiment")

  iris = load_iris()
  X, y = iris.data, iris.target
  if X.size == 0:
    raise ValueError("Dataset ist leer")
  if np.isnan(X).any():
    raise ValueError("Dataset enthält NaN")

  logger.info("Dataset: %d Samples, %d Features", X.shape[0], X.shape[1])
  X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
  )

  params = {"n_estimators": 100, "max_depth": 5, "random_state": 42}

  with mlflow.start_run() as run:
    mlflow.log_params(params)
    model = RandomForestClassifier(**params)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("n_train_samples", len(X_train))
    mlflow.log_metric("n_test_samples", len(X_test))

    report = classification_report(y_test, y_pred, target_names=iris.target_names)
    mlflow.log_text(report, "classification_report.txt")

    signature = mlflow.models.infer_signature(X_train, model.predict(X_train))
    mlflow.sklearn.log_model(
      model,
      "random-forest-model",
      input_example=X_test[:1],
      signature=signature,
    )

    logger.info("Run %s finished with accuracy=%.4f", run.info.run_id, acc)

except Exception as e:
  logger.exception("Training failed: %s", e)
  raise

if acc is not None:
  print(f"Accuracy: {acc:.4f}")
print("Run completed. MLflow UI: http://127.0.0.1:5000")
```

### Schritt 3: Modell-Management mit der Registry (Phase C)

Das beste Modell aus den durchgeführten Experimenten wird nun formal in der Model Registry registriert, um es für das Deployment verfügbar zu machen und seinen Lebenszyklus zu verwalten. Die Registry ersetzt chaotische Modell-Dateiablagen durch nachvollziehbare Versionierung mit Alias-Umschaltungen.

1. **Modell registrieren:** In der MLFlow-UI zum besten Run navigieren und unter "Artifacts" auf "Register Model" klicken. Dies ist der formale Akt der "Beförderung" eines experimentellen Modells zu einem Kandidaten für die Produktion.
2. **Alias zuweisen:** Auf der "Models"-Seite dem Modell einen Alias wie `production-candidate` zuweisen. Dieser Alias signalisiert anderen Systemen (z.B. einer CI/CD-Pipeline), dass dieses Modell nun für weitere Tests und ein potenzielles Deployment bereitsteht.

### Schritt 4a: Testing-Implementierung (Qualitätssicherung)

Bevor wir die Web-App erstellen, implementieren wir umfassende Tests für unser ML-System:

**Erstellt `test_model.py`:**

```python
import pytest
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


class TestIrisModel:
    @pytest.fixture()
    def sample_data(self):
        iris = load_iris()
        return iris.data, iris.target

    def test_data_validation(self, sample_data):
        X, y = sample_data
        assert X.shape[1] == 4
        assert len(np.unique(y)) == 3
        assert not np.isnan(X).any()
        assert not np.isinf(X).any()

    def test_model_min_accuracy(self, sample_data):
        X, y = sample_data
        model = RandomForestClassifier(n_estimators=30, random_state=42)
        model.fit(X, y)
        preds = model.predict(X)
        acc = accuracy_score(y, preds)
        assert acc > 0.90

    def test_model_consistency(self, sample_data):
        X, y = sample_data
        model = RandomForestClassifier(n_estimators=10, random_state=42)
        model.fit(X, y)
        p1 = model.predict(X[:1])
        p2 = model.predict(X[:1])
        assert p1[0] == p2[0]

    def test_invalid_shape(self, sample_data):
        X, y = sample_data
        model = RandomForestClassifier(n_estimators=10, random_state=42)
        model.fit(X, y)
        with pytest.raises(ValueError):
            model.predict([[0, 0, 0, 0, 0]])
```

Optionales Monitoring (Evidently-Skizze & Prometheus-Hinweis):


```python
# from evidently.report import Report
# from evidently.metrics import DataDriftPreset
# report = Report(metrics=[DataDriftPreset()])
# report.run(reference_data=df_ref, current_data=df_new)
# report.save_html("drift_report.html")

# Prometheus Integration (Konzept):
# 1. prometheus_client installieren
# 2. from prometheus_client import Gauge, start_http_server
# 3. start_http_server(9108)
# 4. accuracy_gauge = Gauge('model_accuracy', 'Last validation accuracy')
# 5. accuracy_gauge.set(acc)
```

CI/CD Beispiel (`.github/workflows/ci.yml`):

```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest
      - name: Test
        run: pytest -q
```

#### Erweiterte Pipeline (Training + Registry Promotion + Container Build + Drift Alarm)

Erweitertes Beispiel (`.github/workflows/mlops.yml`) das zeigt, wie Training, Modellregistrierung (per API), Container Build & optionale Drift-Prüfung verknüpft werden können:

```yaml
name: MLOps
on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  train-register:
    runs-on: ubuntu-latest
    env:
      MLFLOW_TRACKING_URI: http://localhost:5000
    services:
      mlflow:
        image: ghcr.io/mlflow/mlflow:latest
        ports:
          - 5000:5000
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install
        run: |
          pip install --upgrade pip
          pip install -r requirements.txt
      - name: Train Model
        run: python train.py
      - name: Select Best Run & Register
        run: |
          python scripts/register_best.py
      - name: Promote Alias
        if: github.ref == 'refs/heads/main'
        run: |
          python scripts/promote.py --from staging --to production

  build-app:
    needs: train-register
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build Image
        run: docker build -t ghcr.io/${{ github.repository }}:latest .
      - name: Push Image
        run: |
          echo ${{ secrets.GITHUB_TOKEN }} | docker login ghcr.io -u ${{ github.actor }} --password-stdin
          docker push ghcr.io/${{ github.repository }}:latest

  drift-check:
    needs: build-app
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install minimal
        run: |
          pip install pandas evidently scikit-learn
      - name: Drift Report
        run: |
          python scripts/drift_check.py
      - name: Upload Artifact
        uses: actions/upload-artifact@v4
        with:
          name: drift-report
          path: drift_report.html
      - name: Fail on Severe Drift
        run: |
          python scripts/drift_gate.py
```

Begleitende Hilfsskripte (Skizzen):

```python
# scripts/register_best.py
import mlflow, pandas as pd
client = mlflow.tracking.MlflowClient()
exp = client.get_experiment_by_name("Iris Classification Experiment")
runs = client.search_runs([exp.experiment_id], order_by=["metrics.accuracy DESC"], max_results=1)
best = runs[0]
model_uri = f"runs:/{best.info.run_id}/random-forest-model"
name = "iris-classifier"
try:
  mv = client.create_model_version(name=name, source=model_uri, run_id=best.info.run_id)
except Exception:
  # Falls bereits vorhanden, überspringen
  pass
client.set_registered_model_alias(name, "staging", mv.version)
print("Registered best run as staging")
```

```python
# scripts/promote.py
import argparse, mlflow
client = mlflow.tracking.MlflowClient()
parser = argparse.ArgumentParser()
parser.add_argument('--from', dest='src', required=True)
parser.add_argument('--to', dest='dst', required=True)
parser.add_argument('--model', default='iris-classifier')
args = parser.parse_args()
versions = client.get_model_version_download_uri # placeholder to ensure context
model = args.model
mv = client.get_model_version_by_alias(model, args.src)
client.set_registered_model_alias(model, args.dst, mv.version)
print(f"Promoted {model}@{args.src} -> {model}@{args.dst}")
```

```python
# scripts/drift_check.py (vereinfachte Drift-Heuristik)
import pandas as pd, json
from sklearn.datasets import load_iris
iris = load_iris()
ref = pd.DataFrame(iris.data, columns=iris.feature_names)
# Simulierte aktuelle Daten (leicht verschoben)
cur = ref.copy()
cur['petal length (cm)'] *= 1.08
drift = {}
for col in ref.columns:
  ref_mean = ref[col].mean()
  cur_mean = cur[col].mean()
  rel = abs(cur_mean - ref_mean)/ref_mean
  drift[col] = rel
with open('drift_metrics.json','w') as f:
  json.dump(drift, f, indent=2)
html = ["<h1>Simple Drift Report</h1>"]
for k,v in drift.items():
  html.append(f"<p>{k}: {v:.3%}</p>")
open('drift_report.html','w').write('\n'.join(html))
```

```python
# scripts/drift_gate.py
import json, sys
threshold = 0.10  # 10% relative mean shift erlaubt
with open('drift_metrics.json') as f:
  metrics = json.load(f)
violations = {k:v for k,v in metrics.items() if v > threshold}
if violations:
  print("SEVERE DRIFT:")
  for k,v in violations.items():
    print(f"  {k}: {v:.2%}")
  sys.exit(1)
print("Drift within acceptable bounds")
```

#### Fairness / Segment Tests (Beispiel)

Für reale Datensätze mit sensiblen Attributen (z.B. `gender`, `age_group`) können Segment-Metriken geprüft werden.

```python
def group_accuracy(model, X, y, sensitive):
    import numpy as np
    import pandas as pd
    df = pd.DataFrame(X).copy()
    df['y'] = y
    df['grp'] = sensitive
    res = {}
    for g, sub in df.groupby('grp'):
        preds = model.predict(sub.drop(columns=['y','grp']))
        res[g] = (preds == sub['y']).mean()
    return res

# Test-Skizze
def test_no_large_accuracy_gap(trained_model, X, y, sensitive_attr):
    accs = group_accuracy(trained_model, X, y, sensitive_attr)
    if accs:
        gap = max(accs.values()) - min(accs.values())
        assert gap < 0.15, f"Fairness Gap zu groß: {gap:.2f}"
```

Diese Beispiele liefern die Blaupause für eine skalierbare MLOps-Pipeline mit Qualitäts-, Governance- und Drift-Gates. Jede Komponente (Training, Registrierung, Promotion, Drift Gate) ist separat erweiterbar – Modularität fördert Wartbarkeit.

### Schritt 4b: Erstellung der Web-App mit Streamlit (Phase K)

Das Frontend der Anwendung wird mit Streamlit erstellt. Die App `app.py` lädt das registrierte Modell direkt aus der MLFlow Model Registry und stellt eine interaktive Benutzeroberfläche bereit.

```python
import streamlit as st
import pandas as pd
import mlflow
import numpy as np

st.title("Iris Flower Species Classifier")

alias = st.sidebar.selectbox("Model Alias", ["staging", "production"], index=1)
MODEL_URI = f"models:/iris-classifier@{alias}"

@st.cache_resource(show_spinner=True)
def load_model(uri: str):
  try:
    return mlflow.pyfunc.load_model(model_uri=uri)
  except Exception as e:
    st.error(f"Modell konnte nicht geladen werden: {e}")
    return None

model = load_model(MODEL_URI)

st.sidebar.header("Input Features")
sepal_length = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.4)
sepal_width = st.sidebar.slider("Sepal Width (cm)", 2.0, 4.5, 3.4)
petal_length = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

input_data = pd.DataFrame({
  'sepal length (cm)': [sepal_length],
  'sepal width (cm)': [sepal_width],
  'petal length (cm)': [petal_length],
  'petal width (cm)': [petal_width]
})

st.subheader("User Input Features")
st.write(input_data)

if st.button("Predict Species"):
  if model is None:
    st.warning("Kein Modell geladen")
  else:
    pred = model.predict(input_data)
    target_names = ['setosa', 'versicolor', 'virginica']
    species = target_names[int(pred[0])]
    st.success(f"Predicted: {species.capitalize()}")
    # Optional: Wahrscheinlichkeiten
    if hasattr(model, "predict_proba"):
      try:
        proba = model.predict_proba(input_data)[0]
        st.bar_chart(pd.DataFrame(proba, index=target_names, columns=["Probability"]))
      except Exception:
        pass
```

### Schritt 5: Deployment in der Streamlit Community Cloud (Phase K - Continuous Delivery)

1. **Vorbereitung:**

  ```bash
   # Requirements mit spezifischen Versionen erstellen
   pip freeze > requirements.txt
   
   # Git Repository vorbereiten
   git add .
  git commit -m "Add Iris ML App with MLflow tracking"
   git push origin main
  ```


1. **Deployment:**
   - Auf [**share.streamlit.io**](https://share.streamlit.io) (jetzt **Streamlit Community Cloud**) anmelden

- GitHub-Repository auswählen und die App deployen
- **Neu in 2025**: Unterstützung für Secrets Management und Environment Variables
- **Profi-Tipp**: Verwendet Streamlit Secrets für MLflow Tracking URI in der Production

1. **Production-Ready Konfiguration:**

  ```python
   # In streamlit_app.py - Production-Ready Setup
   import streamlit as st
   import os
   
  # MLflow URI aus Streamlit Secrets oder Environment
   MLFLOW_URI = st.secrets.get("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000")
   MODEL_URI = f"models:/iris-classifier@production"
   ```

## Literaturempfehlungen und weiterführende Ressourcen {#literatur}

Um die in diesem Handout vorgestellten Konzepte zu vertiefen, wird die folgende Sammlung von Ressourcen empfohlen. Die Liste bietet Zugang zu offiziellen Dokumentationen, praktischen Anleitungen und aktiven Communitys.

### Offizielle Projektseiten und Dokumentationen

Dies sind die primären Quellen für verlässliche Informationen und sollten stets die erste Anlaufstelle sein.

- **MLflow-Dokumentation:** [https://mlflow.org/docs/latest/index.html](https://mlflow.org/docs/latest/index.html)
  - Die offizielle und umfassendste Ressource für alle MLflow-Komponenten (Tracking, Projects, Models, Registry).
- **Streamlit-Dokumentation:** [https://docs.streamlit.io/](https://docs.streamlit.io/)
  - Enthält die API-Referenz, Anleitungen und fortgeschrittene Konzepte für die Erstellung von Streamlit-Apps.
- **Scikit-learn-Dokumentation:** [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/)
  - Die unverzichtbare Referenz für die im Beispiel verwendeten Machine-Learning-Algorithmen und -werkzeuge.

### Tutorials und "How-To"-Anleitungen

Diese Ressourcen bieten geführte Einführungen und praxisnahe Beispiele.

- **MLflow Getting Started Guide:** [https://mlflow.org/docs/latest/getting-started/index.html](https://mlflow.org/docs/latest/getting-started/index.html)
  - Ein schrittweises Tutorial, das die Kernkonzepte von MLflow praktisch demonstriert.
- **Streamlit Get Started:** [https://docs.streamlit.io/get-started](https://docs.streamlit.io/get-started)
  - Eine interaktive Anleitung, die euch in wenigen Minuten zur ersten eigenen Web-App führt.
- **GitHub Guides:** [https://guides.github.com/](https://guides.github.com/)
  - Essenzielle Anleitungen für den Einstieg in die Versionskontrolle mit Git und die Kollaboration über GitHub.

### Communitys und weiterführende Konzepte

Plattformen für den Austausch mit anderen Entwicklern und zur Inspiration.

- **MLOps Community:** [https://mlops.community/](https://mlops.community/)
  - Eine globale Community mit einem Slack-Kanal, Meetups und vielen Ressourcen rund um das Thema MLOps.
- **Streamlit Gallery:** [https://streamlit.io/gallery](https://streamlit.io/gallery)
  - Eine kuratierte Sammlung beeindruckender Streamlit-Apps, die als Inspiration für eigene Projekte dienen kann.
- **"Awesome MLOps" auf GitHub:** [https://github.com/visenger/awesome-mlops](https://github.com/visenger/awesome-mlops)
  - Eine umfassende, von der Community gepflegte Liste von MLOps-Werkzeugen, Blogs, Büchern und anderen Ressourcen.

### Moderne MLOps-Trends 2025

Aktuelle Entwicklungen, die das MLOps-Ökosystem prägen:

- **LLMOps (Large Language Model Operations):** Spezialisierte MLOps-Praktiken für Foundation Models und LLMs
  - Prompt Engineering Workflows
  - Model Fine-tuning Pipelines  
  - RAG (Retrieval Augmented Generation) Systems
- **Feature Stores:** Zentralisierte Verwaltung und Serving von ML-Features
  - Feast (Open Source): [https://feast.dev/](https://feast.dev/)
  - Tecton, Hopsworks (Enterprise Solutions)
- **Cloud-native MLOps:** Kubernetes-basierte ML-Workflows
  - Kubeflow für ML-Pipelines
  - Seldon Core für Model Serving
  - MLRun für End-to-End ML Automation
- **DataOps Integration:** Verschmelzung von Data Engineering und MLOps
  - Data Lineage Tracking
  - Data Quality Monitoring
  - Automated Data Pipeline Testing

## Schlussfolgerung: Den vollen ML-Lebenszyklus meistern {#schlussfolgerung}

Dieses Handout hat die Reise von einem traditionellen, linearen Prozessmodell wie QUA3CK hin zu einer modernen, MLOps-gesteuerten und zyklischen Entwicklungspipeline nachgezeichnet. Die Anreicherung der QUA3CK-Phasen mit den Prinzipien der Versionierung, Automatisierung, des Testings und der Governance - umgesetzt mit Werkzeugen wie MLFlow und Streamlit - transformiert den Entwicklungsprozess von einer Reihe manueller, fehleranfälliger Schritte zu einem integrierten, robusten und agilen Lebenszyklus. Es wird deutlich, dass ein erfolgreiches ML-Produkt weitaus mehr ist als nur ein genaues Modell; es ist ein zuverlässiges, wartbares und skalierbares System, das kontinuierlich überwacht und verbessert wird.

## Nächste Schritte / Ausblick {#next-steps}

**Euer Weg geht jetzt weiter:** Nutzt das Gelernte als Ausgangspunkt:

- Experimentiert mit anderen Algorithmen und modernen Foundation Models
- Fügt weitere Features zur Streamlit-App hinzu (z.B. die Anzeige der Vorhersagewahrscheinlichkeiten)
- Implementiert A/B-Testing für verschiedene Modellversionen
- Automatisiert den gesamten Prozess von Training bis Deployment mit GitHub Actions
- Untersucht fortgeschrittene Themen wie Data-Drift-Detektion oder Feature Stores
- Integriert LLM-basierte Workflows in eure MLOps-Pipeline

Viel Erfolg auf eurer Reise zum MLOps-Experten!
