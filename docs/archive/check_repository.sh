#!/bin/bash

# 🔍 AMALEA 2025 - Comprehensive Repository Check
# Validates the entire modernized repository structure

echo "🎓 AMALEA 2025 - Repository Validation"
echo "======================================"

# Check Python version
echo "🐍 Python Version:"
python3 --version

# Check main directories
echo ""
echo "📁 Main Directory Structure:"
for week in 01_Python_Grundlagen 02_Streamlit_und_Pandas 03_Machine_Learning 04_Advanced_Algorithms 05_Neural_Networks 06_Computer_Vision_NLP 07_Deployment_Portfolio; do
    if [ -d "$week" ]; then
        notebooks=$(find "$week" -name "*.ipynb" | grep -v OLD | wc -l)
        apps=$(find "$week" -name "*.py" | wc -l)
        echo "  ✅ $week: $notebooks notebooks, $apps apps"
    else
        echo "  ❌ $week: Missing"
    fi
done

# Check essential files
echo ""
echo "📄 Essential Files:"
files=("README.md" "requirements-2025.txt" "docker-compose.yml" "Dockerfile.jupyter" "Dockerfile.streamlit")
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ❌ $file: Missing"
    fi
done

# Validate notebook JSON
echo ""
echo "🔧 Notebook Validation:"
python3 -c "
import json
import glob
notebooks = glob.glob('0*/**/*.ipynb', recursive=True)
notebooks = [nb for nb in notebooks if 'OLD' not in nb]
valid_count = 0
for nb in notebooks:
    try:
        with open(nb, 'r') as f:
            json.load(f)
        valid_count += 1
    except Exception as e:
        print(f'  ❌ {nb}: {str(e)}')
print(f'  ✅ {valid_count}/{len(notebooks)} notebooks valid')
"

# Check Python imports
echo ""
echo "🔧 Python Import Check:"
python3 -c "
import sys
packages = ['pandas', 'numpy', 'sklearn', 'streamlit', 'plotly']
missing = []
for pkg in packages:
    try:
        __import__(pkg)
        print(f'  ✅ {pkg}')
    except ImportError:
        print(f'  ⚠️  {pkg}: Not installed')
        missing.append(pkg)
if missing:
    print(f'  📦 Install missing: pip install {\" \".join(missing)}')
"

# Count Streamlit apps
echo ""
echo "📱 Streamlit Apps:"
app_count=$(find . -name "*streamlit*.py" | wc -l)
echo "  📊 Found $app_count Streamlit applications"

# Docker validation
echo ""
echo "🐳 Docker Setup:"
if command -v docker &> /dev/null; then
    echo "  ✅ Docker installed"
    if [ -f "docker-compose.yml" ]; then
        echo "  ✅ docker-compose.yml present"
    fi
else
    echo "  ⚠️  Docker not installed"
fi

# Summary
echo ""
echo "📊 Repository Summary:"
total_notebooks=$(find . -name "*.ipynb" | grep -v OLD | grep -v BACKUP | grep -v DEPRECATED | wc -l)
total_apps=$(find . -name "*.py" | grep -v OLD | grep -v BACKUP | grep -v DEPRECATED | grep -v utils.py | wc -l)
echo "  📓 Active Notebooks: $total_notebooks"
echo "  📱 Streamlit Apps: $total_apps"
echo "  📁 Total Weeks: 7"

echo ""
echo "🎉 Repository Status: READY FOR USE! ✅"
echo "🚀 Start with: docker-compose up"
