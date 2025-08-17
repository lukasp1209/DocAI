import streamlit as st
from src.translation import translate_finding
from src.image_analysis import analyze_image
from src.video_analysis import analyze_video


def main():
    st.title("DocAI - KI Arzt")

    # Text translation
    st.header("Befund eingeben:")
    finding_text = st.text_area("Befund:")
    if st.button("In einfache Sprache übersetzen"):
        if finding_text:
            result = translate_finding(finding_text)
            st.success(result)
        else:
            st.warning("Bitte einen Befund eingeben.")

    # Image analysis
    st.header("MRT/CT Bild auswählen:")
    image_file = st.file_uploader("Bild hochladen", type=["png", "jpg", "jpeg", "bmp"])
    if image_file is not None:
        result = analyze_image(image_file)
        st.success(result)

    # Video analysis
    st.header("Video auswählen:")
    video_file = st.file_uploader("Video hochladen", type=["mp4", "avi", "mov"])
    if video_file is not None:
        result = analyze_video(video_file)
        st.success(result)

if __name__ == "__main__":
    main()