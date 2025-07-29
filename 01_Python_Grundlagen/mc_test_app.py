import streamlit as st
import pandas as pd
import os
import csv
from datetime import datetime
import time
import hashlib
import random

# --- SEITENKONFIGURATION ---
st.set_page_config(
    page_title="MC-Test: Data Analytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- KONSTANTEN & FRAGENKATALOG ---
LOGFILE = "mc_test_answers.csv"
FIELDNAMES = ['user_id_hash', 'user_id_display', 'frage_nr', 'frage', 'antwort', 'richtig', 'zeit']
FRAGEN_ANZAHL = 50

# Der Fragenkatalog bleibt unverändert
fragen = [
    {"frage": "1. Was ist der Hauptvorteil von Docker für Data Science?", "optionen": ["Schnellere Datenverarbeitung durch Container", "Reproduzierbare und isolierte Umgebungen für Projekte", "Automatische Datenbereinigung", "Direkte GPU-Nutzung ohne Konfiguration"], "loesung": 1},
    {"frage": "2. Was ist ein DataFrame in pandas?", "optionen": ["Ein Python-Modul für Visualisierung", "Eine tabellarische Datenstruktur mit Zeilen und Spalten", "Ein Container für Python-Objekte", "Ein spezieller Datentyp für Zeitreihen"], "loesung": 1},
    {"frage": "3. Was beschreibt ein Dockerfile?", "optionen": ["Die Konfiguration der Docker-Registry", "Die Schritte zum Erstellen eines Docker-Images", "Die Netzwerkstruktur der Container", "Die Benutzerrechte im Container"], "loesung": 1},
    {"frage": "4. Wie kann man in Jupyter Notebooks eine Zelle in Code umwandeln?", "optionen": ["Mit der Taste 'M'", "Mit der Taste 'Y'", "Mit Shift+Enter", "Mit der Taste 'A'"], "loesung": 1},
    {"frage": "5. Was ist der Unterschied zwischen einem Docker-Image und einem Container?", "optionen": ["Ein Image ist eine laufende Instanz, ein Container ist die Vorlage", "Ein Container ist eine laufende Instanz eines Images", "Beide sind identisch, nur der Name unterscheidet sich", "Ein Image enthält nur Daten, kein Code"], "loesung": 1},
    {"frage": "6. Was ist der Zweck von 'docker-compose.yml' im amalea-Projekt?", "optionen": ["Verwaltung von Python-Paketen", "Orchestrierung mehrerer Services und Container", "Definition von DataFrames", "Automatische Code-Formatierung"], "loesung": 1},
    {"frage": "7. Was ist das Ziel der Q-Phase im QUA³CK-Modell?", "optionen": ["Datenbereinigung", "Formulierung der Fragestellung und Zieldefinition", "Auswahl des Algorithmus", "Visualisierung der Ergebnisse"], "loesung": 1},
    {"frage": "8. Wie kann man in pandas eine CSV-Datei einlesen?", "optionen": ["pd.read_table()", "pd.read_csv()", "pd.load_csv()", "pd.import_csv()"], "loesung": 1},
    {"frage": "9. Was ist ein typischer Fehler beim Arbeiten mit DataFrames?", "optionen": ["KeyError durch falschen Spaltennamen", "SyntaxError bei DataFrame-Methoden", "ValueError beim Import von pandas", "ImportError bei der Nutzung von .head()"], "loesung": 0},
    {"frage": "10. Was ist der Unterschied zwischen 'pip' und 'conda'?", "optionen": ["pip installiert nur Systempakete, conda nur Python-Pakete", "pip ist für Python-Pakete, conda kann auch Umgebungen verwalten", "Beide sind identisch, nur die Syntax unterscheidet sich", "conda ist ausschließlich für Windows verfügbar"], "loesung": 1},
    {"frage": "11. Was ist ein Vorteil von Jupyter Notebooks für Data Science?", "optionen": ["Sie unterstützen keine Visualisierungen", "Sie ermöglichen interaktives Arbeiten mit Code und Text", "Sie sind nur für Python geeignet", "Sie laufen ausschließlich in der Cloud"], "loesung": 1},
    {"frage": "12. Was ist ein typischer Anwendungsfall für Streamlit im Kurs?", "optionen": ["Entwicklung von Datenbanken", "Erstellung interaktiver Web-Apps für ML-Modelle", "Verwaltung von Docker-Containern", "Kompilierung von C++-Code"], "loesung": 1},
    {"frage": "13. Was ist der Unterschied zwischen einer Liste und einem Dictionary in Python?", "optionen": ["Listen speichern Schlüssel-Wert-Paare, Dictionaries nur Werte", "Listen sind geordnet, Dictionaries sind ungeordnet und nutzen Schlüssel", "Beide sind identisch, nur die Syntax unterscheidet sich", "Dictionaries können keine Zahlen speichern"], "loesung": 1},
    {"frage": "14. Wie kann man in Python eine Funktion definieren?", "optionen": ["function meine_funktion():", "def meine_funktion():", "func meine_funktion():", "define meine_funktion():"], "loesung": 1},
    {"frage": "15. Was ist der Zweck von 'requirements.txt'?", "optionen": ["Enthält die Docker-Konfiguration", "Listet alle Python-Abhängigkeiten für ein Projekt auf", "Speichert die Ergebnisse von DataFrames", "Definiert die Netzwerkports für Streamlit"], "loesung": 1},
    {"frage": "16. Was ist ein typischer Fehler beim Import von pandas?", "optionen": ["ModuleNotFoundError: Kein Modul namens 'pandas'", "ValueError: Falscher Datentyp", "KeyError: Spalte nicht gefunden", "IndexError: Index außerhalb des Bereichs"], "loesung": 0},
    {"frage": "17. Was ist der Unterschied zwischen 'docker ps' und 'docker images'?", "optionen": ["'docker ps' zeigt laufende Container, 'docker images' zeigt verfügbare Images", "Beide zeigen laufende Container", "'docker images' startet Container, 'docker ps' löscht sie", "Beide zeigen nur gestoppte Container"], "loesung": 0},
    {"frage": "18. Was ist ein Vorteil von Docker Compose gegenüber einzelnen Docker-Kommandos?", "optionen": ["Es kann nur einen Container gleichzeitig starten", "Es ermöglicht das Starten mehrerer Services mit einem Befehl", "Es ersetzt die Notwendigkeit von Images", "Es ist ausschließlich für Windows verfügbar"], "loesung": 1},
    {"frage": "19. Was ist der Zweck von 'st.sidebar' in Streamlit?", "optionen": ["Anzeige von Fehlermeldungen", "Platz für interaktive Filter und Navigationselemente", "Speicherung von Daten", "Definition von DataFrames"], "loesung": 1},
    {"frage": "20. Was ist ein typischer Anwendungsfall für das QUA³CK-Modell?", "optionen": ["Entwicklung von Hardware", "Strukturierung von Machine-Learning-Projekten", "Verwaltung von Python-Paketen", "Erstellung von Datenbanken"], "loesung": 1},
    {"frage": "21. Wie kann man in pandas die ersten 5 Zeilen eines DataFrames anzeigen?", "optionen": ["df.show(5)", "df.head()", "df.top(5)", "df.first(5)"], "loesung": 1},
    {"frage": "22. Was ist ein Vorteil von Funktionen in Python?", "optionen": ["Sie machen Code weniger lesbar", "Sie ermöglichen Wiederverwendbarkeit und Struktur", "Sie verhindern die Nutzung von Variablen", "Sie sind nur für mathematische Berechnungen geeignet"], "loesung": 1},
    {"frage": "23. Was ist der Unterschied zwischen 'docker stop' und 'docker rm'?", "optionen": ["'docker stop' löscht Container, 'docker rm' stoppt sie", "'docker stop' hält Container an, 'docker rm' entfernt sie", "Beide Befehle sind identisch", "'docker rm' startet Container neu"], "loesung": 1},
    {"frage": "24. Was ist ein typischer Fehler bei der Nutzung von Streamlit?", "optionen": ["StreamlitAPIException durch falsche Nutzung von Widgets", "KeyError beim Import von Streamlit", "ValueError bei der Nutzung von st.write()", "IndexError bei der Sidebar"], "loesung": 0},
    {"frage": "25. Was ist der Zweck von 'st.metric' in Streamlit?", "optionen": ["Anzeige von Metriken und Kennzahlen", "Erstellung von DataFrames", "Definition von Funktionen", "Verwaltung von Docker-Containern"], "loesung": 0},
    {"frage": "26. Was ist ein Vorteil von Markdown in Jupyter Notebooks?", "optionen": ["Es ermöglicht die Ausführung von Python-Code", "Es erlaubt strukturierte Dokumentation und Formatierung", "Es ersetzt die Notwendigkeit von Code-Zellen", "Es ist nur für Überschriften geeignet"], "loesung": 1},
    {"frage": "27. Was ist der Unterschied zwischen 'import pandas as pd' und 'from pandas import *'?", "optionen": ["Beide importieren pandas identisch", "'import pandas as pd' gibt einen Alias, 'from pandas import *' importiert alle Namen direkt", "'from pandas import *' ist schneller", "'import pandas as pd' importiert nur DataFrames"], "loesung": 1},
    {"frage": "28. Was ist ein typischer Anwendungsfall für 'st.file_uploader' in Streamlit?", "optionen": ["Hochladen und Einlesen eigener Datendateien", "Visualisierung von DataFrames", "Erstellung von Docker-Containern", "Definition von Funktionen"], "loesung": 0},
    {"frage": "29. Was ist der Zweck von 'def' in Python?", "optionen": ["Definition einer Variablen", "Definition einer Funktion", "Definition eines DataFrames", "Definition eines Containers"], "loesung": 1},
    {"frage": "30. Was ist ein Vorteil von Docker für Teamarbeit?", "optionen": ["Jeder arbeitet in einer eigenen, inkompatiblen Umgebung", "Alle nutzen die exakt gleiche, reproduzierbare Umgebung", "Docker verhindert die Nutzung von Python", "Docker ist nur für Einzelpersonen geeignet"], "loesung": 1},
    {"frage": "31. Was ist laut `00_Python_in_3_Stunden.ipynb` eine 'Best Practice', um die Performance von Filter- und Join-Operationen in Pandas zu beschleunigen?", "optionen": ["Daten immer als CSV statt Parquet speichern", "Einen sinnvollen Index mit `set_index` setzen", "Operationen in Python-For-Schleifen statt als Vektoroperationen schreiben", "Die `pipe()`-Methode für alle Transformationen verwenden"], "loesung": 1},
    {"frage": "32. Welchen Hauptvorteil bietet ein Multi-Stage-Build in einem `Dockerfile`, wie in den Notebooks beschrieben?", "optionen": ["Automatisches Erstellen einer `.dockerignore`-Datei", "Starten von dev, test und prod-Containern mit einem Befehl", "Reduzierung der finalen Image-Größe durch Trennung von Build- und Runtime-Umgebung", "Sichere Verwaltung von Umgebungsvariablen im Image"], "loesung": 2},
    {"frage": "33. Wie wird die A³-Phase des QUA³CK-Prozessmodells im Kurs `AMALEA 2025` modern interpretiert?", "optionen": ["Durch interaktive Datenexploration in einer Streamlit-App", "Durch das Deployment des finalen Modells in der Streamlit Cloud", "Durch die Erstellung eines automatisierten MLOps-Dashboards", "Durch Experiment-Tracking mit MLflow zur systematischen Verwaltung"], "loesung": 3},
    {"frage": "34. Wofür wird der Parameter `stratify` in `train_test_split` (siehe `03_QUA3CK_Prozessmodell.ipynb`) typischerweise verwendet?", "optionen": ["Um sicherzustellen, dass die Daten vor dem Splitten zufällig gemischt werden.", "Um die gleiche Verteilung der Zielklassen in Trainings- und Test-Set beizubehalten.", "Um eine exakte Aufteilung von 70% Trainings- und 30% Testdaten zu garantieren.", "Um den `random_state` für reproduzierbare Splits zu ersetzen."], "loesung": 1},
    {"frage": "35. Was ist der primäre Zweck von `@st.cache_data` in Streamlit?", "optionen": ["Das Caching von UI-Elementen wie Buttons und Slidern.", "Die Beschleunigung von Berechnungen, indem Funktionsergebnisse zwischengespeichert werden.", "Das Speichern des `session_state` über verschiedene Browser-Tabs hinweg.", "Die automatische Umwandlung von Pandas DataFrames in schnelle Apache Arrow Tabellen."], "loesung": 1},
    {"frage": "36. Welches Problem wird durch die Verwendung von Docker-Volumes, wie in `01_Docker_für_Data_Science.ipynb` empfohlen, primär gelöst?", "optionen": ["Die Größe des Docker-Images wird reduziert.", "Daten bleiben auch nach dem Löschen eines Containers persistent erhalten.", "Die Netzwerkkommunikation zwischen Containern wird ermöglicht.", "Python-Abhängigkeiten werden direkt im Container installiert."], "loesung": 1},
    {"frage": "37. In welcher Phase des QUA³CK-Modells findet die 'Conclude and Compare' Aktivität hauptsächlich statt?", "optionen": ["Phase Q (Question)", "Phase U (Understanding)", "Phase A³ (Algorithm, Adapting, Adjusting)", "Phase C (Conclude and Compare)"], "loesung": 3},
    {"frage": "38. Was ist ein wesentlicher Unterschied zwischen `st.session_state` und einer normalen Python-Variable in einem Streamlit-Skript?", "optionen": ["`st.session_state` ist schneller als eine globale Variable.", "`st.session_state` kann komplexe Objekte wie DataFrames speichern, Variablen nicht.", "`st.session_state` behält seinen Wert über Reruns der App hinweg, eine Variable nicht.", "`st.session_state` ist nur innerhalb von Funktionen sichtbar."], "loesung": 2},
    {"frage": "39. Welches Datenformat wird in `00_Python_in_3_Stunden.ipynb` als oft schneller und speichereffizienter als CSV für große Datenmengen bezeichnet?", "optionen": ["JSON", "Excel (.xlsx)", "Parquet", "SQL"], "loesung": 2},
    {"frage": "40. Was beschreibt der Begriff 'Vektorisierung' in Pandas, der als Performance-Tipp genannt wird?", "optionen": ["Das Umwandeln von Daten in grafische Vektoren für die Visualisierung.", "Das Anwenden von Operationen auf ganze Arrays statt auf einzelne Elemente in einer Schleife.", "Das Speichern von DataFrames in einem Vektor-Datenbanksystem.", "Das Erstellen von Feature-Vektoren für Machine-Learning-Modelle."], "loesung": 1},
    {"frage": "41. Welche MLOps-Praxis wird im `03_QUA3CK_Prozessmodell.ipynb` mit der K-Phase (Knowledge Transfer) in Verbindung gebracht?", "optionen": ["MLFlow Experiment Tracking", "Interaktive Streamlit Apps zur Datenexploration", "Cloud-Deployment und die Erstellung eines Portfolios", "Automatisierte Modellvergleiche in einem Dashboard"], "loesung": 2},
    {"frage": "42. Welchen Zweck erfüllt der Befehl `docker-compose down`?", "optionen": ["Er startet alle in der `docker-compose.yml` definierten Services im Hintergrund.", "Er zeigt die Logs aller laufenden Services an.", "Er stoppt und entfernt die von `docker-compose up` erstellten Container und Netzwerke.", "Er baut die Docker-Images für alle Services neu, ohne sie zu starten."], "loesung": 2},
    {"frage": "43. Was ist der Unterschied zwischen supervised und unsupervised Learning laut dem Iris-Beispiel im QUA³CK-Notebook?", "optionen": ["Supervised Learning benötigt gelabelte Daten (Features und Targets), Unsupervised nicht.", "Unsupervised Learning ist immer genauer als Supervised Learning.", "Supervised Learning wird für Clustering verwendet, Unsupervised für Klassifikation.", "Unsupervised Learning kann nur mit numerischen Daten umgehen, Supervised auch mit Text."], "loesung": 0},
    {"frage": "44. Welches Streamlit-Layout-Element wird verwendet, um Inhalte nebeneinander darzustellen?", "optionen": ["st.expander()", "st.tabs()", "st.columns()", "st.container()"], "loesung": 2},
    {"frage": "45. Warum wird im `Dockerfile`-Beispiel `COPY requirements.txt .` vor `COPY . .` ausgeführt?", "optionen": ["Um die Lesbarkeit des Dockerfiles zu verbessern.", "Weil `requirements.txt` größer ist und zuerst kopiert werden muss.", "Um den Docker-Build-Cache optimal zu nutzen und die Installation der Pakete nur bei Änderungen an der Datei erneut auszuführen.", "Um sicherzustellen, dass die Abhängigkeiten vor dem App-Code vorhanden sind."], "loesung": 2},
    {"frage": "46. Was ist eine 'Chained Assignment'-Warnung in Pandas und wie sollte man sie laut Notebook vermeiden?", "optionen": ["Eine Warnung, die auftritt, wenn zu viele Methodenaufrufe verkettet werden; man sollte sie ignorieren.", "Ein Fehler, der beim Zuweisen zu einer Kopie eines DataFrames auftritt; man sollte `.loc` für die Zuweisung verwenden.", "Eine Information, dass eine Zuweisung erfolgreich war; es ist keine Aktion erforderlich.", "Ein Hinweis, dass der DataFrame-Index neu gesetzt werden sollte, um die Performance zu verbessern."], "loesung": 1},
    {"frage": "47. Welches Tool wird im Kurs-Setup (`01_Docker_für_Data_Science.ipynb`) für das ML-Experiment-Tracking verwendet?", "optionen": ["Streamlit", "Jupyter Lab", "MLflow", "Docker Hub"], "loesung": 2},
    {"frage": "48. Was bedeutet der Jupyter-Tastaturbefehl 'M' im Command Mode?", "optionen": ["Die aktuelle Zelle nach unten verschieben (Move).", "Eine neue Zelle oberhalb einfügen (More).", "Die aktuelle Zelle in eine Markdown-Zelle umwandeln.", "Den Kernel neu starten (Master Reset)."], "loesung": 2},
    {"frage": "49. Was ist der primäre Zweck der `EXPOSE`-Anweisung in einem Dockerfile?", "optionen": ["Den Container mit dem Internet zu verbinden.", "Einen Port vom Host-System in den Container weiterzuleiten.", "Den Port zu dokumentieren, auf dem der Service im Container lauscht.", "Die Firewall des Containers zu konfigurieren."], "loesung": 2},
    {"frage": "50. Welche Metrik wird im `03_QUA3CK_Prozessmodell.ipynb` zur Bewertung des K-Means-Modells (Unsupervised) verwendet?", "optionen": ["Accuracy", "Adjusted Rand Score", "F1-Score", "Root Mean Squared Error (RMSE)"], "loesung": 1}
]

# --- FUNKTIONEN ---
@st.cache_data
def get_user_id_hash(user_id):
    """Erzeugt einen anonymisierten Hash der User-ID."""
    return hashlib.sha256(user_id.encode()).hexdigest()

def initialize_session_state():
    """Initialisiert den Session State für einen neuen Testdurchlauf."""
    st.session_state.beantwortet = [None] * len(fragen)
    st.session_state.frage_indices = list(range(len(fragen)))
    random.shuffle(st.session_state.frage_indices)
    st.session_state.start_zeit = None
    st.session_state.progress_loaded = False

def load_user_progress(user_id_hash):
    """Lädt den Fortschritt und die Startzeit eines Nutzers."""
    if not (os.path.isfile(LOGFILE) and os.path.getsize(LOGFILE) > 0):
        return

    try:
        df = pd.read_csv(LOGFILE, dtype={'user_id_hash': str})
        user_df = df[df['user_id_hash'] == user_id_hash]

        if user_df.empty:
            return

        st.session_state.start_zeit = pd.to_datetime(user_df['zeit']).min()

        for _, row in user_df.iterrows():
            frage_nr = int(row['frage_nr'])
            original_idx = next((i for i, f in enumerate(fragen) if f['frage'].startswith(f"{frage_nr}.")), None)
            if original_idx is not None:
                st.session_state.beantwortet[original_idx] = int(row['richtig'])
                st.session_state[f"frage_{original_idx}"] = row['antwort']
    except Exception as e:
        st.error(f"Fehler beim Laden des Fortschritts: {e}")

def save_answer(user_id, user_id_hash, frage_obj, antwort, punkte):
    """Speichert eine einzelne Antwort in der CSV-Datei."""
    frage_nr = int(frage_obj['frage'].split('.')[0])
    row = {
        'user_id_hash': user_id_hash, 'user_id_display': user_id, 'frage_nr': frage_nr, 
        'frage': frage_obj['frage'], 'antwort': antwort, 'richtig': punkte, 
        'zeit': datetime.now().isoformat(timespec='seconds')
    }
    try:
        file_exists_and_not_empty = os.path.isfile(LOGFILE) and os.path.getsize(LOGFILE) > 0
        with open(LOGFILE, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
            if not file_exists_and_not_empty:
                writer.writeheader()
            writer.writerow(row)
    except IOError as e:
        st.error(f"Konnte Antwort nicht speichern: {e}")

def display_question(frage_obj, frage_idx, anzeige_nummer):
    """Stellt eine einzelne Frage dar und verarbeitet die Antwort."""
    frage_text = frage_obj['frage'].split('.', 1)[1].strip()
    
    with st.container(border=True):
        st.markdown(f"### Frage {anzeige_nummer}")
        st.markdown(f"**{frage_text}**")
        
        is_disabled = st.session_state.beantwortet[frage_idx] is not None
        
        try:
            gespeicherte_antwort = st.session_state.get(f"frage_{frage_idx}")
            antwort_index = frage_obj["optionen"].index(gespeicherte_antwort) if gespeicherte_antwort else None
        except (ValueError, TypeError):
            antwort_index = None

        antwort = st.radio(
            "Antwort auswählen:", options=frage_obj["optionen"], key=f"frage_{frage_idx}",
            index=antwort_index, disabled=is_disabled, label_visibility="collapsed"
        )

        if antwort and not is_disabled:
            if st.session_state.start_zeit is None:
                st.session_state.start_zeit = datetime.now()

            richtig = (antwort == frage_obj["optionen"][frage_obj["loesung"]])
            punkte = 1 if richtig else -1
            st.session_state.beantwortet[frage_idx] = punkte
            
            save_answer(st.session_state.user_id, st.session_state.user_id_hash, frage_obj, antwort, punkte)
            
            if richtig:
                st.toast("Richtig! 🚀", icon="✅")
                st.balloons()
            else:
                st.toast("Leider falsch.", icon="❌")
            
            time.sleep(1.5)
            st.rerun()

        if is_disabled:
            if st.session_state.beantwortet[frage_idx] == 1:
                st.success("Ihre Antwort ist richtig! (+1 Punkt)")
            else:
                st.error(f"Ihre Antwort war leider falsch (-1 Punkt). Die korrekte Antwort lautet: **{frage_obj['optionen'][frage_obj['loesung']]}**")

@st.cache_data
def calculate_leaderboard():
    """Berechnet die Bestenliste aus der Log-Datei."""
    if not (os.path.isfile(LOGFILE) and os.path.getsize(LOGFILE) > 0):
        return pd.DataFrame()

    try:
        df = pd.read_csv(LOGFILE)
        df['richtig'] = pd.to_numeric(df['richtig'], errors='coerce')
        df['zeit'] = pd.to_datetime(df['zeit'])

        agg_df = df.groupby('user_id_hash').agg(
            Punkte=('richtig', 'sum'),
            Anzahl_Antworten=('frage_nr', 'count'),
            Startzeit=('zeit', 'min'),
            Endzeit=('zeit', 'max'),
            Anzeige_Name=('user_id_display', 'first')
        ).reset_index()

        completed_df = agg_df[agg_df['Anzahl_Antworten'] >= FRAGEN_ANZAHL].copy()
        
        if completed_df.empty: return pd.DataFrame()
            
        completed_df['Dauer'] = completed_df['Endzeit'] - completed_df['Startzeit']
        
        leaderboard = completed_df.sort_values(by=['Punkte', 'Dauer'], ascending=[False, True])
        
        leaderboard['Zeit'] = leaderboard['Dauer'].apply(lambda x: f"{int(x.total_seconds() // 60)}:{int(x.total_seconds() % 60):02d} min")
        leaderboard = leaderboard[['Anzeige_Name', 'Punkte', 'Zeit']].head(5)
        leaderboard.rename(columns={'Anzeige_Name': 'Name'}, inplace=True)
        leaderboard.reset_index(drop=True, inplace=True)
        leaderboard.index += 1

        return leaderboard
    except Exception:
        return pd.DataFrame()

def display_sidebar_metrics(num_answered):
    """Stellt die Seitenleiste dar."""
    st.sidebar.header("📊 Fortschritt & Score")
    st.sidebar.progress(num_answered / len(fragen))
    aktueller_punktestand = sum([p for p in st.session_state.beantwortet if p is not None])
    st.sidebar.metric("Aktueller Punktestand", f"{aktueller_punktestand} / {len(fragen)}")

    if st.session_state.start_zeit and num_answered < len(fragen):
        elapsed_time = datetime.now() - st.session_state.start_zeit
        minutes, seconds = divmod(int(elapsed_time.total_seconds()), 60)
        st.sidebar.metric("⏳ Bisherige Zeit", f"{minutes:02d}:{seconds:02d}")
    
    if num_answered == len(fragen):
        st.sidebar.success("✅ Test abgeschlossen!")

    st.sidebar.header("🏆 Bestenliste")
    leaderboard_df = calculate_leaderboard()
    if leaderboard_df.empty:
        st.sidebar.info("Noch keine abgeschlossenen Tests.")
    else:
        st.sidebar.dataframe(leaderboard_df)

def display_final_summary(num_answered):
    """Zeigt die finale Zusammenfassung am Ende des Tests."""
    if num_answered != len(fragen):
        return

    st.header("🎉 Test abgeschlossen!")
    aktueller_punktestand = sum([p for p in st.session_state.beantwortet if p is not None])
    prozent = aktueller_punktestand / len(fragen) if len(fragen) > 0 else 0
    
    emoji, quote = "", ""
    if prozent == 1.0:
        emoji, quote = "🌟🥇", "**Perfekt! Hervorragende Leistung! Alle Fragen richtig beantwortet.**"
        st.balloons(); st.snow()
    elif prozent >= 0.8:
        emoji, quote = "🎉👍", "**Sehr stark! Sie haben ein exzellentes Verständnis der Konzepte.**"
    elif prozent >= 0.5:
        emoji, quote = "🙂", "**Gut gemacht! Eine solide Grundlage ist vorhanden.**"
    else:
        emoji, quote = "🤔", "**Einige Konzepte sitzen schon. Schauen Sie sich die Erklärungen zu den falschen Antworten noch einmal an.**"
        
    st.success(f"### {emoji} Endstand: {aktueller_punktestand} von {len(fragen)} Punkten")
    st.markdown(quote)

def handle_user_session():
    """Verwaltet die Nutzer-Anmeldung und den Wechsel zwischen Nutzern."""
    st.sidebar.header("👤 Nutzerkennung")
    
    if 'user_id' in st.session_state:
        st.sidebar.success(f"Angemeldet als: **{st.session_state.user_id}**")
        if st.sidebar.button("Ausloggen & Nutzer wechseln"):
            # Speichere den aktuellen Input, damit er nach dem Reset wieder da ist
            current_input = st.session_state.get('user_id_input', '')
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.session_state.user_id_input = current_input
            st.rerun()
        return st.session_state.user_id

    user_input = st.sidebar.text_input("Bitte gib ein Pseudonym ein:", key="user_id_input")
    
    if st.sidebar.button("Test starten / Nutzer wechseln"):
        if user_input:
            # Setze den Session State komplett zurück, bevor ein neuer Nutzer startet
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.session_state['user_id'] = user_input.strip()
            st.rerun()
        else:
            st.sidebar.error("Bitte gib zuerst ein Pseudonym ein.")
    
    st.warning("Bitte gib im Seitenmenü ein Pseudonym ein und starte den Test.")
    st.stop()
        
# --- HAUPTPROGRAMM ---
def main():
    st.title("📝 MC-Test: Data Analytics & Big Data")
    
    user_id = handle_user_session()
    
    # Der user_id_hash muss im Session State gespeichert werden, um über Reruns hinweg verfügbar zu sein.
    if 'user_id_hash' not in st.session_state:
        st.session_state.user_id_hash = get_user_id_hash(user_id)
    
    # Session State initialisieren oder laden
    if 'frage_indices' not in st.session_state:
        initialize_session_state()
        load_user_progress(st.session_state.user_id_hash)
    
    st.info("**Hinweis:** Wähle die beste Antwort. Einmal beantwortete Fragen sind final. Viel Erfolg!")

    num_answered = len([p for p in st.session_state.beantwortet if p is not None])
    
    if num_answered == len(fragen):
        display_final_summary()
    else:
        # Quiz-Container
        quiz_container = st.container()
        with quiz_container:
            for i, q_idx in enumerate(st.session_state.frage_indices):
                display_question(fragen[q_idx], q_idx, i + 1)
                
    display_sidebar_metrics(num_answered)

if __name__ == "__main__":
    main()