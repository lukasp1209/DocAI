# 📦 AMALEA Archive Directory

**Zweck**: Zentrales Archiv für alle Backup-Dateien und historische Versionen des AMALEA-Projekts.

## 📁 Archiv-Struktur

### 🗂️ Original AMALEA Backup
- **`BACKUP_Original_AMALEA_Notebooks/`** - Komplettes Original AMALEA vor der Modernisierung
  - Enthält alle 6 Wochen der ursprünglichen Notebooks
  - Historische requirements (`requirements_old.txt`)
  - **Dies ist das einzige relevante Backup - alle Originalinhalte sind hier**

### 📋 Requirements & Dependencies
- **`backup_requirements/`** - Verschiedene Versionen der Python Requirements
  - `requirements-2025.txt` - Standard-Version 2025
  - `requirements-2025-backup.txt` - Version mit erweiterten Kommentaren
  - `requirements-minimal.txt` - Minimale Dependencies für Tests
- `amalea.yml` - Legacy conda environment file (ersetzt durch Docker + requirements.txt)

### 📚 Dokumentation
- **`docs_archive/`** - Archivierte Dokumentations-Dateien
  - `archive/` - Alte Archiv-Struktur
  - `deployment/` - Deployment-Dokumentation
  - `development/` - Entwickler-Dokumentation
  - `modernization/` - Modernisierungsprozess-Dokumentation

## 🎯 Warum archiviert?

Diese Dateien wurden archiviert, weil:
1. **Original-AMALEA Backup** - Vollständige Sicherung der ursprünglichen Notebooks
2. **Historischer Wert** - Dokumentation der Entwicklungsgeschichte  
3. **Backup-Sicherheit** - Keine Daten gehen verloren
4. **Saubere Struktur** - Hauptverzeichnis bleibt übersichtlich

**Redundante Backups entfernt** - Nur das Original-AMALEA Backup ist relevant.

## 💾 Wiederherstellung

Falls benötigt, können Dateien aus diesem Archiv zurück ins Hauptverzeichnis kopiert werden:

```bash
# Beispiel: Backup Requirements konsultieren (historisch)
cp archive/backup_requirements/requirements-2025.txt requirements-backup.txt

# Beispiel: Altes Notebook konsultieren
open archive/BACKUP_Original_AMALEA_Notebooks/Woche\ 1/
```

## 🗑️ Lösch-Policy

**Nicht löschen!** Diese Archiv-Dateien sind:
- ✅ Wichtige Referenz für die Projektentwicklung
- ✅ Backup für kritische Wiederherstellung
- ✅ Dokumentation der Modernisierungsschritte

---

**Archiviert am:** 16. Juni 2025  
**Grund:** Repository-Bereinigung und Strukturverbesserung  
**Status:** Vollständig organisiert ✅
