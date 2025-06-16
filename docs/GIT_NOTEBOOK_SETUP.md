# 🔧 Git Configuration für Jupyter Notebooks

Diese Datei erklärt die Git-Konfiguration für das AMALEA-Projekt, um Probleme mit Jupyter Notebook Metadaten zu vermeiden.

## 🎯 Problem gelöst

**Vorher**: Beim Öffnen von Notebooks änderten sich automatisch Metadaten (execution_count, timestamps), was zu unnötigen Git-Änderungen führte.

**Nachher**: Nur relevante Code- und Markdown-Änderungen werden getrackt.

## 📁 Neue Dateien

### `.gitignore`
Ignoriert automatisch:
- `.ipynb_checkpoints/` (Jupyter Backup-Dateien)
- `__pycache__/` (Python Cache)
- Virtuelle Umgebungen (`venv/`, `.venv/`)
- IDE-Dateien (`.vscode/`, `.idea/`)
- OS-Dateien (`.DS_Store`, `Thumbs.db`)
- MLflow Artifacts (`mlruns/`, `.mlflow/`)
- Docker Volumes und `.env` Dateien

### `.gitattributes`
Konfiguriert:
- Automatische Notebook-Bereinigung (`*.ipynb filter=nbstrip`)
- Korrekte Line-Endings für Text-Dateien
- Binär-Erkennung für Bilder und Daten

## ⚙️ Git Filter

Der `nbstrip` Filter entfernt automatisch beim Commit:
- `execution_count` Felder
- Timestamps
- Output-Daten
- Überflüssige Metadaten

## 🚀 Für neue Teammitglieder

Nach dem Klonen des Repositories:

```bash
# Git Filter konfigurieren (einmalig)
git config filter.nbstrip.clean 'jupyter nbconvert --ClearOutputPreprocessor.enabled=True --ClearMetadataPreprocessor.enabled=True --to=notebook --stdin --stdout'
git config filter.nbstrip.smudge cat
git config filter.nbstrip.required true
```

## ✅ Testen

1. Öffne ein Notebook in Jupyter Lab
2. Führe eine Zelle aus oder ändere etwas
3. Speichere das Notebook
4. Prüfe: `git status` sollte nur bei echten Code-Änderungen etwas anzeigen

## 📋 Best Practices

- **Notebooks immer speichern** bevor du committest
- **Outputs löschen** bei großen Visualisierungen vor Commit
- **Kernel restarten** bei wichtigen Commits für saubere Ausführung

## 🔍 Problembehandlung

Falls Git trotzdem Notebook-Änderungen anzeigt:

```bash
# Einzelnes Notebook zurücksetzen
git checkout -- pfad/zum/notebook.ipynb

# Alle Notebooks zurücksetzen  
git checkout -- **/*.ipynb

# Filter neu anwenden
git add *.ipynb
git reset --hard
```

---

*Diese Konfiguration macht die Zusammenarbeit mit Jupyter Notebooks in Git deutlich angenehmer! 🎉*
