# Installation – Los geht's mit Jupyter!

Cool, dass du dabei bist! Um die praktischen Aufgaben in diesem Kurs zu meistern, brauchst du eine laufende Jupyter Notebook Umgebung. Jupyter Notebooks sind super praktisch, weil du Code, Text, und Visualisierungen an einem Ort hast – ideal für Data Science und Machine Learning Kram. Du hast die Wahl:

1.  **Lokal auf deinem Rechner:** Volle Kontrolle, alles bei dir. Braucht etwas Setup.
2.  **Online-Dienste (Google Colab / myBinder):** Kaum Setup, direkt im Browser loslegen. Super für den schnellen Start oder wenn du unterwegs bist.

Egal, wofür du dich entscheidest, schnapp dir danach am besten direkt unser [Einführungs-Notebook](1%20Erste%20Schritte.ipynb) und spiel ein bisschen damit rum, um ein Gefühl dafür zu bekommen.

## Lokale Installation – Dein eigener Jupyter-Server

Dieser Weg ist für dich, wenn du Anaconda und die ganzen Abhängigkeiten direkt auf deiner Maschine haben willst. Das gibt dir die meiste Flexibilität.

### Anaconda installieren – Deine Python-Power-Suite

Jupyter Notebooks laufen bei uns über Anaconda. Das ist eine Distribution, die Python, einen Haufen nützlicher Data-Science-Bibliotheken und eben auch Jupyter Notebook schon mitbringt. Außerdem ist der Paketmanager `conda` echt Gold wert, um deine Python-Umgebungen sauber zu halten.

*   **Download:** Anaconda ist kostenlos. Hol es dir [hier](https://www.anaconda.com/products/individual).
*   **Installation:** Achte bei der Installation unbedingt darauf, dass du eine **Python 3.x Version** (z.B. 3.9, 3.10 oder neuer) auswählst. Python 2.x ist veraltet und wird hier nicht funktionieren.
*   **PATH-Variable (Optional, aber empfohlen für Terminal-Nutzer):** Überleg dir, ob du Anaconda zu deiner PATH-Umgebungsvariable hinzufügen lässt. Das macht es einfacher, `conda` und `python` direkt aus deinem Standard-Terminal aufzurufen. Wenn du dir unsicher bist, lass es erstmal weg, die Anaconda Prompt funktioniert auch so.

### Daten und Notebooks schnappen

Klar, ohne die Kursmaterialien geht nix. Für die lokale Installation lädst du am besten direkt das komplette Paket für alle Wochen runter.

*   **ZIP-Download:** Über [diesen Direkt-Link](https://github.com/KI-Campus/AMALEA/archive/refs/heads/master.zip) oder auf der GitHub-Seite des Repositories unter `Code` --> `Download ZIP` kriegst du ein ZIP-Archiv mit allem, was du brauchst.
*   **Git-Clone (Für die Profis):** Wenn du schon mit Git vertraut bist (was im 5. Semester ja durchaus der Fall sein sollte 😉), clone dir das Repository einfach: `git clone https://github.com/KI-Campus/AMALEA.git`. Der Vorteil: Du kannst Updates leichter ziehen und deine eigenen Änderungen versionieren. Falls du Git noch nicht so draufhast, aber neugierig bist, gibt's z.B. [hier eine gute Einführung](https://open.hpi.de/courses/git2020).

### Virtuelle Umgebung einrichten (Einmalige Sache, aber super wichtig!)

Bevor du jetzt wild Code ausführst: **Virtuelle Umgebungen sind dein Freund!** Ernsthaft. Damit stellst du sicher, dass die Pakete und Versionen für dieses Projekt isoliert bleiben und sich nicht mit anderen Python-Projekten auf deinem System in die Quere kommen (Stichwort: "Dependency Hell").

Wir haben dir das einfach gemacht und eine `amalea.yml` Datei beigelegt. Das ist eine Umgebungsdatei für `conda`, die alle Pakete mit den richtigen Versionen auflistet, die du für den Kurs brauchst.

1.  **Terminal öffnen:**
    *   **Windows:** Starte die "Anaconda Prompt" (findest du im Startmenü nach der Anaconda-Installation).
    *   **macOS/Linux:** Öffne dein normales Terminal. Wenn du Anaconda zum PATH hinzugefügt hast, kannst du `conda` direkt nutzen.
2.  **Umgebung erstellen:** Navigiere im Terminal in das Verzeichnis, in das du die Kursmaterialien (also auch die `amalea.yml`) heruntergeladen/geclont hast. Dann feuer diesen Befehl ab:

    ```bash
    conda env create --file amalea.yml
    ```

    Das kann jetzt ein paar Minuten dauern, weil `conda` alle Pakete runterlädt und installiert. Hol dir 'nen Kaffee.

3.  **Umgebung aktivieren:** Sobald die Installation durch ist, aktivierst du die Umgebung mit:

    ```bash
    conda activate amalea
    ```
    Dein Terminal-Prompt sollte sich jetzt ändern und `(amalea)` am Anfang anzeigen. Das zeigt dir, dass du in der virtuellen Umgebung bist.

4.  **Jupyter Notebook starten:** Wenn die Umgebung aktiv ist, startest du den Jupyter Notebook Server direkt aus dem AMALEA-Hauptverzeichnis mit:

    ```bash
    jupyter notebook .
    ```
    Der Punkt `.` sagt Jupyter, dass es im aktuellen Verzeichnis starten soll.

### Jupyter Notebook Server starten (Wenn die Umgebung schon existiert)

Wenn du die virtuelle Umgebung schon erstellt hast (siehe oben), sind die Schritte zum Starten einfacher:

1.  **Terminal öffnen:** Wie oben, Anaconda Prompt (Windows) oder dein Standard-Terminal (macOS/Linux).
2.  **Zum Projektordner navigieren:** `cd PFAD_ZU_DEINEM_AMALEA_ORDNER`
    *   Beispiel Windows: `cd C:\Users\DeinName\Downloads\AMALEA`
    *   Beispiel macOS/Linux: `cd ~/Downloads/AMALEA`
3.  **Virtuelle Umgebung aktivieren:**
    ```bash
    conda activate amalea
    ```
4.  **Jupyter Notebook starten:**
    ```bash
    jupyter notebook .
    ```

Dein Browser sollte sich automatisch öffnen und dir das Jupyter Dashboard mit den Kursordnern anzeigen. Wenn nicht, siehst du im Terminal eine URL (meist sowas wie `http://localhost:8888/...`), die du manuell in den Browser kopieren kannst.

**Beenden:** Um Jupyter zu stoppen, geh zurück ins Terminal, wo der Server läuft, und drück `Strg+C` (oder `Ctrl+C`). Manchmal musst du das mit `y` (für yes) und Enter bestätigen.

## Google Colab – Jupyter in der Cloud von Google

Google Colab ([colab.research.google.com](https://colab.research.google.com/)) ist 'ne feine Sache, wenn du schnell loslegen willst oder keinen eigenen Rechner für die Installation hast. Du brauchst nur ein Google-Konto.

*   **Direktlinks nutzen:** In der `README.md` findest du für viele Notebooks "Open in Colab"-Badges. Klick drauf, und das Notebook öffnet sich direkt in Colab – meist schon mit den richtigen Daten verbunden.
*   **Manuell hochladen:**
    1.  Geh zu Colab.
    2.  Wähl `Datei` -> `Notebook hochladen`.
    3.  Zieh deine `.ipynb`-Datei rein oder wähl sie aus.
*   **Wichtig bei Colab:**
    *   **Daten:** Wenn ein Notebook externe Datendateien (z.B. `.csv`) braucht, musst du die oft separat hochladen. Im Notebook-Menü links gibt's einen Reiter für "Dateien". Dort kannst du Ordner erstellen und Dateien hochladen, damit die Pfade im Code stimmen.
    *   **Code-Zellen für Daten-Download:** Manche Notebooks haben am Anfang eine Code-Zelle, die Daten automatisch von GitHub oder einer anderen Quelle herunterlädt (z.B. mit `!wget` oder `!git clone`). **Diese Zelle musst du als Erstes ausführen!**
    *   **Rechenzeit & GPUs:** Colab stellt dir kostenlos Rechenressourcen zur Verfügung, inklusive GPUs (gut für Deep Learning ab Woche 4/5). Aber die Nutzung ist limitiert und nicht garantiert. Für längere Trainings oder sehr rechenintensive Sachen ist eine lokale Installation oft zuverlässiger.

## myBinder – Die Community-Lösung

[MyBinder](https://mybinder.org/) ist eine weitere coole Plattform, die dir interaktive Notebook-Umgebungen direkt aus Git-Repositories erstellt – kostenlos und ohne Anmeldung.

*   **Direktlinks:** Auch hier gibt's in der `README.md` "Launch Binder"-Badges. Die starten eine komplette Umgebung mit allen Dateien und den in `requirements.txt` oder `environment.yml` (ähnlich unserer `amalea.yml`) spezifizierten Paketen.
*   **Startzeit:** Das Bauen der Umgebung auf myBinder kann manchmal ein paar Minuten dauern, besonders wenn der Dienst gerade stark ausgelastet ist. Also Geduld!
*   **Keine GPUs:** Soweit ich weiß, stehen auf myBinder standardmäßig keine GPUs zur Verfügung. Das Training von neuronalen Netzen (Woche 4/5) wird also deutlich länger dauern als lokal mit GPU oder auf Colab mit GPU-Runtime.
*   **Temporär:** Deine Sitzung auf myBinder ist temporär. Wenn du Änderungen an Notebooks machst, lade sie runter, sonst sind sie weg, wenn die Sitzung beendet wird.

# FAQ – Wenn's mal klemmt

Keine Panik, wenn was nicht sofort klappt. Hier ein paar typische Stolpersteine und wie du sie aus dem Weg räumst:

1.  **Kernel neu starten:** Der "Kernel" ist quasi das Gehirn deines Notebooks – die Python-Engine, die deinen Code ausführt. Wenn sich was aufhängt, komische Fehler kommen oder du gerade ein Paket installiert hast, ist ein Kernel-Neustart oft die Lösung. In Jupyter oben im Menü: `Kernel` -> `Restart`.
2.  **Abhängigkeiten checken:** Hast du alle Pakete installiert (`conda env create -f amalea.yml` sollte das erledigt haben)? Sind die Datendateien da, wo das Notebook sie erwartet (Pfade!)?
3.  **Google ist dein Freund:** Diese FAQ ist nicht allumfassend. Wenn du eine Fehlermeldung nicht verstehst, kopier sie und wirf sie in eine Suchmaschine. Die Chance ist hoch, dass schon jemand dasselbe Problem hatte.

### "Hilfe, mein Kernel will nicht!" – Neustart-Tricks

Manchmal zickt der Kernel. Ein Neustart (Menü: `Kernel` -> `Restart`) löst 90% der Probleme. Wenn du Änderungen am Code gemacht hast, die du behalten willst, wähle `Kernel` -> `Restart & Clear Output` (setzt alles zurück, aber Code bleibt) oder `Kernel` -> `Restart & Run All` (startet neu und führt alle Zellen von oben nach unten aus).

### `ModuleNotFoundError: No module named 'dingsbums'`

Diese Meldung schreit: "Hey, ich kann das Python-Paket `dingsbums` nicht finden!"

*   **Bist du in der richtigen `conda` Umgebung?** Tippe `conda activate amalea` ins Terminal, bevor du `jupyter notebook .` startest.
*   **Paket wirklich installiert?** Die `amalea.yml` sollte alles Nötige enthalten. Wenn du aber mal ein Paket brauchst, das nicht drin ist, und du in deiner `amalea`-Umgebung bist, kannst du es mit `conda install paketname` oder `pip install paketname` nachinstallieren. Für Pakete aus speziellen Channels (wie `conda-forge`) ist der Befehl oft `conda install -c conda-forge paketname`.
    *   Beispiel aus Woche 1 für `matplotlib` (obwohl es in der `amalea.yml` sein sollte):
        ```bash
        conda install -c conda-forge matplotlib
        ```
        Nach der Installation musst du den Kernel im Jupyter Notebook neu starten!

### `FileNotFoundError: [Errno 2] No such file or directory: 'data/meine_datei.csv'`

Klassiker! Python findet die Datei nicht, die du laden willst.

*   **Pfad korrekt?** Überprüfe, ob der Pfad im Code (`'data/meine_datei.csv'`) wirklich zu deiner Dateistruktur passt. Relative Pfade (`data/...`) beziehen sich auf das Verzeichnis, aus dem Jupyter Notebook gestartet wurde (also dein AMALEA-Hauptverzeichnis, wenn du `jupyter notebook .` dort ausgeführt hast).
*   **Datei vorhanden?** Ist die Datei `meine_datei.csv` wirklich im Unterordner `data`?
*   **Groß-/Kleinschreibung:** Besonders auf Linux und macOS ist das wichtig! `Data` ist nicht dasselbe wie `data`.
*   **Google Colab:** Hier musst du die Daten oft erst hochladen. Schau in den linken Reiter "Dateien" und stell sicher, dass deine Ordnerstruktur (`data/`) und die Dateien da sind.

So, jetzt solltest du startklar sein. Viel Spaß beim Coden und Experimentieren! Wenn was ist, frag einfach.
