import streamlit as st
from src.translation import translate_finding
from src.image_analysis import analyze_image
from src.video_analysis import analyze_video

# --- Page Config ---
st.set_page_config(
    page_title="DocAI - KI Arzt",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # --- Sidebar ---
    st.sidebar.title("⚙️ Einstellungen")
    st.sidebar.info("Willkommen bei **DocAI - KI Arzt**.\n\n"
                    "Hier können Sie medizinische Befunde vereinfachen "
                    "sowie Bilder und Videos analysieren lassen.")

    st.sidebar.markdown("👤 **Benutzer:** Arzt / Patient")

    # --- Header ---
    st.title("🩺 DocAI - Dein KI-Arzt-Assistent")
    st.markdown("Nutze KI, um Befunde besser zu verstehen und medizinische Medien auszuwerten.")

    # --- Tabs ---
    tabs = st.tabs(["📝 Befund", "🩺 Diagnose", "🖼️ Bildgebende Verfahren"])

    # --- Tab 1: Befund ---
    with tabs[0]:
        st.subheader("Befund in einfache Sprache übersetzen")
        with st.container():
            finding_text = st.text_area("👉 Befund hier eingeben:", height=150, placeholder="Schreibe oder füge einen medizinischen Befund ein...")
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button("🔄 Übersetzen"):
                    if finding_text:
                        result = translate_finding(finding_text)
                        st.success(result)
                    else:
                        st.warning("⚠️ Bitte einen Befund eingeben.")
            with col2:
                st.info("💡 Tipp: Die Übersetzung ist für Patienten gedacht und verwendet vereinfachte Sprache.")

    # --- Tab 2: Diagnose ---
    with tabs[1]:
        st.subheader("Diagnose erstellen (Platzhalter)")
        symptoms = st.text_area("Symptome und Patientendaten eingeben:", height=150, placeholder="Geben Sie hier die Symptome ein...")
        
        uploaded_files = st.file_uploader(
            "Bilder oder Videos für die Diagnose hochladen",
            type=["png", "jpg", "jpeg", "bmp", "mp4", "mov", "avi"],
            accept_multiple_files=True,
            key="diagnose_uploader"
        )

        if uploaded_files:
            st.write("Vorschau der hochgeladenen Dateien:")
            for uploaded_file in uploaded_files:
                if uploaded_file.type.startswith('image/'):
                    st.image(uploaded_file, caption=uploaded_file.name, use_column_width=True)
                elif uploaded_file.type.startswith('video/'):
                    st.video(uploaded_file)

        if st.button("Diagnose erstellen"):
            if symptoms or uploaded_files:
                st.info("Diese Funktion ist noch in Entwicklung.")
                # Hier könnte die Logik für die Diagnose stehen
                if uploaded_files:
                    st.write(f"{len(uploaded_files)} Datei(en) wurden für die Analyse vorgemerkt.")
            else:
                st.warning("⚠️ Bitte geben Sie Symptome ein oder laden Sie eine Datei hoch.")

    # --- Tab 3: Bildgebende Verfahren ---
    with tabs[2]:
        st.subheader("Analyse von MRT, CT, Röntgen & weiteren Bilddaten")
        image_file = st.file_uploader("🖼️ Unterstützte Formate: PNG, JPG, JPEG, BMP, DCM", type=["png", "jpg", "jpeg", "bmp", "dcm"])
        if image_file is not None:
            # Hinweis: Die Analyse von DICOM (.dcm) erfordert möglicherweise eine spezielle Bibliothek wie pydicom.
            with st.spinner("🔍 Analysiere Bild..."):
                result = analyze_image(image_file)
            st.success("✅ Analyse abgeschlossen")
            st.write(result)


if __name__ == "__main__":
    main()
