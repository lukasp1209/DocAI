
import streamlit as st
import pandas as pd
import plotly.express as px


# -----------------------------
# Data Analytics & Big Data Übungs-App
# -----------------------------

# App-Titel und Einleitung
st.title("📊 Meine Data Analytics & Big Data App")
st.write("Autor: [Dein Name hier]")
st.info("Interaktive Übungs-App: Analysiere, filtere und visualisiere Produktdaten. Passe die App nach deinen Ideen an!")

# Beispieldaten erstellen (kann durch eigenen Upload ersetzt werden)
daten = {
    'Produkt': ['Laptop', 'Handy', 'Tablet', 'Kopfhörer', 'Maus'],
    'Preis': [800, 600, 400, 100, 25],
    'Kategorie': ['Computer', 'Telefon', 'Computer', 'Audio', 'Computer'],
    'Bewertung': [4.5, 4.2, 4.0, 4.8, 3.9]
}
df = pd.DataFrame(daten)


# Sidebar für Filter
st.sidebar.header("🔍 Filter")
kategorie_filter = st.sidebar.selectbox(
    "Kategorie wählen:",
    ["Alle"] + list(df['Kategorie'].unique())
)


# Daten filtern
if kategorie_filter != "Alle":
    gefilterte_daten = df[df['Kategorie'] == kategorie_filter]
else:
    gefilterte_daten = df


# Hauptbereich
st.subheader("🛍️ Produktdaten")
if gefilterte_daten.empty:
    st.warning("Keine Produkte gefunden. Bitte wähle eine andere Kategorie.")
else:
    st.dataframe(gefilterte_daten)


# Visualisierungen (nur anzeigen, wenn Daten vorhanden)
if not gefilterte_daten.empty:
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.bar(gefilterte_daten, x='Produkt', y='Preis', 
                      title="Preise nach Produkt")
        st.plotly_chart(fig1, use_container_width=True)
    with col2:
        fig2 = px.scatter(gefilterte_daten, x='Preis', y='Bewertung',
                         color='Kategorie', title="Preis vs. Bewertung")
        st.plotly_chart(fig2, use_container_width=True)


# Statistiken (nur anzeigen, wenn Daten vorhanden)
if not gefilterte_daten.empty:
    st.subheader("📈 Zusammenfassung")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Anzahl Produkte", len(gefilterte_daten))
    with col2:
        st.metric("Durchschnittspreis", f"{gefilterte_daten['Preis'].mean():.0f}€")
    with col3:
        st.metric("Beste Bewertung", f"{gefilterte_daten['Bewertung'].max()}")


# Erweiterungsideen für Studierende
st.info(
    "💡 Ideen zum Erweitern: "
    "Eigene CSV-Daten hochladen (st.file_uploader), "
    "weitere Filter (z. B. Preisbereich), "
    "Sortieroptionen, "
    "weitere Diagrammtypen, "
    "oder ein Export der gefilterten Daten."
)
