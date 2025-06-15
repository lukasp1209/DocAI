# 🖼️ Computer Vision Applications - Streamlit App
# Führen Sie aus mit: streamlit run 06_02_streamlit_cv_apps.py

import streamlit as st
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt
from scipy import signal
import io
import base64
from typing import Dict, List, Tuple

# App Konfiguration
st.set_page_config(
    page_title="🖼️ CV Applications",
    page_icon="🔍",
    layout="wide"
)

# Header
st.title("🖼️ Computer Vision Applications")
st.markdown("**Praktische Bildverarbeitung mit verschiedenen Algorithmen**")
st.markdown("---")

# Sidebar
st.sidebar.header("🎛️ Einstellungen")

# App-Modus auswählen
app_mode = st.sidebar.selectbox(
    "🎯 Wählen Sie eine Anwendung:",
    ["Edge Detection", "Object Detection", "Image Segmentation", "Feature Detection", "Filter Comparison"]
)

# Bild Upload
uploaded_file = st.sidebar.file_uploader(
    "📸 Eigenes Bild hochladen",
    type=['png', 'jpg', 'jpeg']
)

# Helper Functions
@st.cache_data
def load_image(uploaded_file):
    """Lädt und konvertiert Bild"""
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        return np.array(image)
    else:
        # Beispielbild erstellen
        img = np.zeros((400, 400, 3), dtype=np.uint8)
        cv2.rectangle(img, (50, 50), (200, 200), (255, 255, 255), -1)
        cv2.circle(img, (300, 300), 75, (128, 128, 128), -1)
        cv2.line(img, (0, 200), (400, 200), (64, 64, 64), 5)
        return img

def apply_edge_detection(image, method):
    """Verschiedene Edge Detection Methoden"""
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) if len(image.shape) == 3 else image
    
    if method == "Canny":
        edges = cv2.Canny(gray, 50, 150)
    elif method == "Sobel X":
        edges = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        edges = np.absolute(edges)
    elif method == "Sobel Y":
        edges = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        edges = np.absolute(edges)
    elif method == "Laplacian":
        edges = cv2.Laplacian(gray, cv2.CV_64F)
        edges = np.absolute(edges)
    elif method == "Scharr X":
        edges = cv2.Scharr(gray, cv2.CV_64F, 1, 0)
        edges = np.absolute(edges)
    elif method == "Scharr Y":
        edges = cv2.Scharr(gray, cv2.CV_64F, 0, 1)
        edges = np.absolute(edges)
    
    return edges.astype(np.uint8)

def detect_contours(image):
    """Konturen erkennen"""
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    result = image.copy()
    cv2.drawContours(result, contours, -1, (0, 255, 0), 2)
    return result, len(contours)

def segment_image(image, method):
    """Bildsegmentierung"""
    if method == "K-Means":
        data = image.reshape((-1, 3))
        data = np.float32(data)
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
        k = 4
        _, labels, centers = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        centers = np.uint8(centers)
        segmented = centers[labels.flatten()]
        segmented = segmented.reshape(image.shape)
        return segmented
    
    elif method == "Watershed":
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        
        # Noise removal
        kernel = np.ones((3,3), np.uint8)
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
        
        # Sure background area
        sure_bg = cv2.dilate(opening, kernel, iterations=3)
        
        # Distance transform
        dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
        _, sure_fg = cv2.threshold(dist_transform, 0.7*dist_transform.max(), 255, 0)
        
        # Unknown region
        sure_fg = np.uint8(sure_fg)
        unknown = cv2.subtract(sure_bg, sure_fg)
        
        # Marker labelling
        _, markers = cv2.connectedComponents(sure_fg)
        markers = markers + 1
        markers[unknown == 255] = 0
        
        markers = cv2.watershed(image, markers)
        result = image.copy()
        result[markers == -1] = [255, 0, 0]
        return result

def detect_features(image, method):
    """Feature Detection"""
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    if method == "SIFT":
        sift = cv2.SIFT_create()
        keypoints, descriptors = sift.detectAndCompute(gray, None)
        result = cv2.drawKeypoints(image, keypoints, None)
        return result, len(keypoints)
    
    elif method == "ORB":
        orb = cv2.ORB_create()
        keypoints, descriptors = orb.detectAndCompute(gray, None)
        result = cv2.drawKeypoints(image, keypoints, None)
        return result, len(keypoints)
    
    elif method == "Harris Corners":
        corners = cv2.cornerHarris(gray, 2, 3, 0.04)
        corners = cv2.dilate(corners, None)
        result = image.copy()
        result[corners > 0.01 * corners.max()] = [255, 0, 0]
        corner_count = np.sum(corners > 0.01 * corners.max())
        return result, corner_count

# Hauptbereich
image = load_image(uploaded_file)

if app_mode == "Edge Detection":
    st.subheader("⚡ Edge Detection")
    
    col1, col2 = st.columns(2)
    
    edge_method = st.sidebar.selectbox(
        "Edge Detection Methode:",
        ["Canny", "Sobel X", "Sobel Y", "Laplacian", "Scharr X", "Scharr Y"]
    )
    
    with col1:
        st.write("📸 **Original**")
        st.image(image, use_column_width=True)
    
    with col2:
        st.write(f"⚡ **{edge_method} Edge Detection**")
        edges = apply_edge_detection(image, edge_method)
        st.image(edges, use_column_width=True, clamp=True)
    
    # Statistiken
    st.info(f"""
    📊 **Edge Detection Statistiken:**
    - Methode: {edge_method}
    - Erkannte Edges: {np.sum(edges > 0):,} Pixel
    - Edge Density: {(np.sum(edges > 0) / edges.size * 100):.2f}%
    """)

elif app_mode == "Object Detection":
    st.subheader("🎯 Object Detection (Contours)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("📸 **Original**")
        st.image(image, use_column_width=True)
    
    with col2:
        st.write("🎯 **Detected Objects**")
        result, contour_count = detect_contours(image)
        st.image(result, use_column_width=True)
    
    st.success(f"🎯 **{contour_count} Objekte erkannt**")

elif app_mode == "Image Segmentation":
    st.subheader("🧩 Image Segmentation")
    
    seg_method = st.sidebar.selectbox(
        "Segmentierung Methode:",
        ["K-Means", "Watershed"]
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("📸 **Original**")
        st.image(image, use_column_width=True)
    
    with col2:
        st.write(f"🧩 **{seg_method} Segmentation**")
        segmented = segment_image(image, seg_method)
        st.image(segmented, use_column_width=True)

elif app_mode == "Feature Detection":
    st.subheader("🔍 Feature Detection")
    
    feature_method = st.sidebar.selectbox(
        "Feature Detection Methode:",
        ["SIFT", "ORB", "Harris Corners"]
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("📸 **Original**")
        st.image(image, use_column_width=True)
    
    with col2:
        st.write(f"🔍 **{feature_method} Features**")
        try:
            result, feature_count = detect_features(image, feature_method)
            st.image(result, use_column_width=True)
            st.success(f"🔍 **{feature_count} Features erkannt**")
        except Exception as e:
            st.error(f"Fehler bei Feature Detection: {e}")

elif app_mode == "Filter Comparison":
    st.subheader("🔧 Filter Comparison")
    
    filters = {
        "Blur": cv2.GaussianBlur,
        "Sharpen": lambda img, *args: cv2.filter2D(img, -1, np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])),
        "Emboss": lambda img, *args: cv2.filter2D(img, -1, np.array([[-2,-1,0],[-1,1,1],[0,1,2]])),
    }
    
    st.write("📸 **Original**")
    st.image(image, use_column_width=True)
    
    cols = st.columns(len(filters))
    
    for i, (filter_name, filter_func) in enumerate(filters.items()):
        with cols[i]:
            st.write(f"🔧 **{filter_name}**")
            if filter_name == "Blur":
                filtered = filter_func(image, (15, 15), 0)
            else:
                filtered = filter_func(image)
            st.image(filtered, use_column_width=True)

# Erklärungen
st.markdown("---")
st.subheader("📚 Computer Vision Konzepte")

explanations = {
    "Edge Detection": """
    ⚡ **Edge Detection** findet Bereiche mit starken Intensitätsänderungen:
    - **Canny:** Beste Allzweck-Edge Detection
    - **Sobel:** Gradient-basiert, gut für Richtungs-Info
    - **Laplacian:** Zweite Ableitung, findet alle Edges
    """,
    "Object Detection": """
    🎯 **Object Detection** erkennt und lokalisiert Objekte:
    - **Contours:** Umrisse von Objekten finden
    - **Bounding Boxes:** Rechteckige Bereiche um Objekte
    - **Deep Learning:** YOLO, R-CNN für komplexe Objekte
    """,
    "Image Segmentation": """
    🧩 **Image Segmentation** teilt Bilder in Regionen:
    - **K-Means:** Pixel-Clustering nach Farben
    - **Watershed:** Topologie-basierte Segmentierung
    - **Semantic:** Deep Learning für Objektklassen
    """,
    "Feature Detection": """
    🔍 **Feature Detection** findet charakteristische Punkte:
    - **SIFT:** Scale-Invariant Feature Transform
    - **ORB:** Oriented FAST and Rotated BRIEF
    - **Harris:** Corner Detection Algorithmus
    """
}

if app_mode in explanations:
    st.info(explanations[app_mode])

# Footer
st.markdown("---")
st.markdown("*📚 IU Data Analytics & Big Data - Woche 6.2: Computer Vision Applications*")
