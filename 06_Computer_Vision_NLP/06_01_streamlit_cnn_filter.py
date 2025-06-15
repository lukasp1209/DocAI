# 🎮 CNN Filter Explorer - Streamlit App
# Führen Sie aus mit: streamlit run 06_01_streamlit_cnn_filter.py

import streamlit as st
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
from scipy import signal
import io
import base64

# App Konfiguration
st.set_page_config(
    page_title="🔍 CNN Filter Explorer",
    page_icon="🎮",
    layout="wide"
)

# Header
st.title("🔍 CNN Filter Explorer")
st.markdown("**Interaktive Exploration von Computer Vision Filtern**")
st.markdown("---")

# Sidebar für Parameter
st.sidebar.header("🔧 Filter Einstellungen")

# Filter-Typ auswählen
filter_type = st.sidebar.selectbox(
    "🎯 Wählen Sie einen Filter:",
    ["Original", "Blur (Mean)", "Edge Detection (Sobel X)", "Edge Detection (Sobel Y)", 
     "Sharpen", "Laplace", "Custom Filter"]
)

# Parameter für Filter
if filter_type == "Blur (Mean)":
    kernel_size = st.sidebar.slider("Kernel Größe", 3, 15, 5, step=2)
elif filter_type == "Custom Filter":
    st.sidebar.markdown("**Custom 3x3 Filter Matrix:**")
    col1, col2, col3 = st.sidebar.columns(3)
    with col1:
        f00 = st.number_input("", value=0.0, key="f00")
        f10 = st.number_input("", value=0.0, key="f10") 
        f20 = st.number_input("", value=0.0, key="f20")
    with col2:
        f01 = st.number_input("", value=0.0, key="f01")
        f11 = st.number_input("", value=1.0, key="f11")
        f21 = st.number_input("", value=0.0, key="f21")
    with col3:
        f02 = st.number_input("", value=0.0, key="f02")
        f12 = st.number_input("", value=0.0, key="f12")
        f22 = st.number_input("", value=0.0, key="f22")

# Bild Upload
uploaded_file = st.sidebar.file_uploader(
    "📸 Eigenes Bild hochladen",
    type=['png', 'jpg', 'jpeg']
)

# Standard Filter definieren
def get_filter_kernel(filter_type, kernel_size=5):
    if filter_type == "Blur (Mean)":
        return np.ones((kernel_size, kernel_size)) / (kernel_size**2)
    elif filter_type == "Edge Detection (Sobel X)":
        return np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    elif filter_type == "Edge Detection (Sobel Y)":
        return np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    elif filter_type == "Sharpen":
        return np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    elif filter_type == "Laplace":
        return np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    elif filter_type == "Custom Filter":
        return np.array([[f00, f01, f02], [f10, f11, f12], [f20, f21, f22]])
    else:
        return None

# Bild laden
if uploaded_file is not None:
    # User Upload
    image = Image.open(uploaded_file)
    image_array = np.array(image.convert('L'))  # Graustufen
else:
    # Standard Scipy Bild
    from scipy import misc
    image_array = misc.ascent()

# Filter anwenden
if filter_type == "Original":
    filtered_image = image_array
else:
    kernel = get_filter_kernel(filter_type, kernel_size if filter_type == "Blur (Mean)" else 3)
    filtered_image = signal.convolve2d(image_array, kernel, boundary='symm', mode='same')
    
    # Für Edge Detection: Absolutwerte
    if "Edge Detection" in filter_type or filter_type == "Laplace":
        filtered_image = np.abs(filtered_image)
    
    # Werte normalisieren
    filtered_image = np.clip(filtered_image, 0, 255)

# Hauptbereich: Bilder anzeigen
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏔️ Original Bild")
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    ax1.imshow(image_array, cmap='gray', interpolation='nearest')
    ax1.set_title(f"Original ({image_array.shape[0]}x{image_array.shape[1]})")
    ax1.axis('off')
    st.pyplot(fig1)
    
    # Statistiken
    st.info(f"""
    📊 **Original Statistiken:**
    - Min: {image_array.min()}
    - Max: {image_array.max()}  
    - Mean: {image_array.mean():.1f}
    - Std: {image_array.std():.1f}
    """)

with col2:
    st.subheader(f"🔍 {filter_type}")
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    ax2.imshow(filtered_image, cmap='gray', interpolation='nearest')
    ax2.set_title(f"{filter_type} Ergebnis")
    ax2.axis('off')
    st.pyplot(fig2)
    
    # Statistiken
    st.info(f"""
    📊 **Filter Statistiken:**
    - Min: {filtered_image.min():.1f}
    - Max: {filtered_image.max():.1f}
    - Mean: {filtered_image.mean():.1f}  
    - Std: {filtered_image.std():.1f}
    """)

# Filter Kernel anzeigen
if filter_type != "Original":
    st.subheader("🔧 Filter Kernel")
    kernel = get_filter_kernel(filter_type, kernel_size if filter_type == "Blur (Mean)" else 3)
    
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    im = ax3.imshow(kernel, cmap='RdBu', vmin=-2, vmax=2)
    ax3.set_title(f"{filter_type} Kernel")
    
    # Werte in Zellen anzeigen
    for (i, j), val in np.ndenumerate(kernel):
        ax3.text(j, i, f'{val:.2f}', ha='center', va='center', 
                color='white' if abs(val) > 1 else 'black', fontweight='bold')
    
    plt.colorbar(im, ax=ax3)
    st.pyplot(fig3)

# Erklärungen
st.markdown("---")
st.subheader("📚 Filter-Erklärungen")

explanations = {
    "Blur (Mean)": "🌫️ **Blur Filter:** Macht das Bild unscharf durch Mittelwertbildung. Größere Kernel = stärkerer Blur-Effekt.",
    "Edge Detection (Sobel X)": "⚡ **Sobel X:** Erkennt vertikale Kanten durch Gradientenberechnung in X-Richtung.",
    "Edge Detection (Sobel Y)": "⚡ **Sobel Y:** Erkennt horizontale Kanten durch Gradientenberechnung in Y-Richtung.", 
    "Sharpen": "✨ **Sharpen:** Verstärkt Details und Kanten für schärfere Bilder.",
    "Laplace": "🔍 **Laplace:** Zweite Ableitung - hebt Kanten und Details stark hervor.",
    "Custom Filter": "🎨 **Custom:** Erstellen Sie Ihren eigenen 3x3 Filter!"
}

if filter_type in explanations:
    st.info(explanations[filter_type])

# Fun Facts
st.markdown("---")
st.subheader("💡 CNN Connection")
st.success("""
**Warum ist das wichtig für CNNs?**

🧠 **Automatisches Lernen:** CNNs lernen diese Filter automatisch während des Trainings!

🔄 **Hierarchisch:** Erste Layer lernen einfache Filter (Kanten), tiefere Layer komplexere Muster.

⚡ **Effizienz:** Ein 3x3 Filter hat nur 9 Parameter - viel weniger als Fully-Connected Layer.

🎯 **Spezialisierung:** Verschiedene Filter in verschiedenen Layern erkennen verschiedene Features.
""")

# Download-Button für gefilterte Bilder
if st.button("💾 Gefiltertes Bild downloaden"):
    # PIL Image erstellen
    filtered_pil = Image.fromarray(filtered_image.astype(np.uint8))
    
    # In Bytes konvertieren
    img_buffer = io.BytesIO()
    filtered_pil.save(img_buffer, format='PNG')
    img_str = base64.b64encode(img_buffer.getvalue()).decode()
    
    # Download Link
    href = f'<a href="data:image/png;base64,{img_str}" download="{filter_type}_filtered.png">Download {filter_type} Bild</a>'
    st.markdown(href, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("*📚 IU Data Analytics & Big Data - Woche 6.1: CNN Grundlagen*")
