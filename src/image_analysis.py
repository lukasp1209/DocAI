from PIL import Image, ImageOps, ImageFilter
import numpy as np
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def analyze_features(image):
    """
    Analyze image features using Pillow and NumPy.
    
    Args:
        image: PIL.Image object
        
    Returns:
        dict: Dictionary containing image features
    """
    # Convert to grayscale
    gray_image = image.convert('L')
    gray_array = np.array(gray_image)
        
    # Calculate basic statistics
    mean_intensity = np.mean(gray_array)
    std_intensity = np.std(gray_array)
    
    # Edge detection
    edges_image = gray_image.filter(ImageFilter.FIND_EDGES)
    edges_array = np.array(edges_image)
    num_edges = np.count_nonzero(edges_array)
    edge_density = num_edges / (edges_array.shape[0] * edges_array.shape[1])
    
    # Contrast analysis using histogram equalization
    equalized_image = ImageOps.equalize(gray_image)
    equalized_array = np.array(equalized_image)
    contrast = np.mean(equalized_array)
    
    return {
        'mean_intensity': mean_intensity,
        'std_intensity': std_intensity,
        'edge_density': edge_density,
        'contrast': contrast
    }

def analyze_image(uploaded_file):
    """
    Analyze medical images (MRI/CT) using computer vision techniques.
    
    Args:
        uploaded_file: A file-like object from Streamlit's file_uploader.
    
    Returns:
        str: Analysis results with findings
    """
    try:
        # Load image from the uploaded file object
        logger.info(f"Loading image from uploaded file: {uploaded_file.name}")
        image = Image.open(uploaded_file)
            
        # Analyze features
        features = analyze_features(image)
        
        # Generate analysis report
        findings = []
        
        # Basic image quality assessment
        if features['mean_intensity'] < 30:
            findings.append("⚠️ Warnung: Bild möglicherweise unterbelichtet")
        elif features['mean_intensity'] > 225:
            findings.append("⚠️ Warnung: Bild möglicherweise überbelichtet")
            
        if features['std_intensity'] < 20:
            findings.append("⚠️ Warnung: Geringer Bildkontrast erkannt")
            
        # Structure analysis
        if features['edge_density'] > 0.1:
            findings.append("ℹ️ Erhöhte Strukturdichte erkannt")
        elif features['edge_density'] < 0.01:
            findings.append("⚠️ Warnung: Sehr geringe Strukturdichte")
            
        # Overall assessment
        if not findings:
            findings.append("✅ Keine besonderen Auffälligkeiten in der Bildqualität")
        # Add feature measurements
        findings.append(f"\nBildanalyse-Metriken:")
        findings.append(f"- Mittlere Intensität: {features['mean_intensity']:.1f}")
        findings.append(f"- Standardabweichung: {features['std_intensity']:.1f}")
        findings.append(f"- Strukturdichte: {features['edge_density']:.3f}")
        findings.append(f"- Kontrastwert: {features['contrast']:.1f}")
        
        return "\n".join(findings)
        
    except Exception as e:
        logger.error(f"Error analyzing image: {str(e)}")
        return f"Fehler bei der Bildanalyse: {str(e)}"