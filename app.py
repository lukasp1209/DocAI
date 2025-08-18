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
    tabs = st.tabs(["📝 Befund Übersetzen", "🖼️ Bildanalyse", "🎥 Videoanalyse"])

    # --- Tab 1: Text Translation ---
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

    # --- Tab 2: Image Analysis ---
    with tabs[1]:
        st.subheader("MRT/CT Bild hochladen")
        image_file = st.file_uploader("🖼️ Unterstützte Formate: PNG, JPG, JPEG, BMP", type=["png", "jpg", "jpeg", "bmp"])
        if image_file is not None:
            with st.spinner("🔍 Analysiere Bild..."):
                result = analyze_image(image_file)
            st.success("✅ Analyse abgeschlossen")
            st.write(result)

    # --- Tab 3: Video Analysis ---
    with tabs[2]:
        st.subheader("Video hochladen")
        video_file = st.file_uploader("🎥 Unterstützte Formate: MP4, AVI, MOV", type=["mp4", "avi", "mov"])
        if video_file is not None:
            st.video(video_file)  # zeigt das Video im Player
            with st.spinner("⏳ Analysiere Video..."):
                result = analyze_video(video_file)
            st.success("✅ Analyse abgeschlossen")
            st.write(result)


if __name__ == "__main__":
    main()
