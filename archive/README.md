# 📦 AMALEA Archive Directory

**Zweck**: Zentrales Archiv für alle Backup-Dateien und historische Versionen des AMALEA-Projekts.

## 📁 Archiv-Struktur

### 🗂️ Original Backups
- **`BACKUP_Original_AMALEA_Notebooks/`** - Ursprüngliche AMALEA Notebooks vor der Modernisierung
- **`BACKUP_vor_refactoring/`** - Backup vor dem großen Refactoring 2025
- **`DEPRECATED_alte_struktur/`** - Veraltete Ordnerstruktur (vor Reorganisation)

### 📋 Requirements & Dependencies
- **`backup_requirements/`** - Verschiedene Versionen der Python Requirements
  - `requirements-2025.txt` - Hauptversion 2025
  - `requirements-2025-backup.txt` - Backup mit Kommentaren
  - `requirements-2025-clean.txt` - Bereinigte Version
  - `requirements-minimal.txt` - Minimale Dependencies für Tests
- `amalea.yml` - Legacy conda environment file (replaced by Docker + requirements.txt)

### 📚 Dokumentation
- **`docs_archive/`** - Archivierte Dokumentations-Dateien
  - `archive/` - Alte Archiv-Struktur
  - `deployment/` - Deployment-Dokumentation
  - `development/` - Entwickler-Dokumentation
  - `modernization/` - Modernisierungsprozess-Dokumentation

## 🎯 Warum archiviert?

Diese Dateien wurden archiviert, weil:
1. **Historischer Wert** - Dokumentation der Entwicklungsgeschichte
2. **Backup-Sicherheit** - Keine Daten gehen verloren
3. **Saubere Struktur** - Hauptverzeichnis bleibt übersichtlich
4. **Referenz** - Bei Bedarf wieder zugänglich

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
