import cv2
from PIL import Image, ImageOps, ImageFilter
import numpy as np
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def preprocess_medical_image(image_path, target_size=(224, 224)):
    """
    Preprocess medical images for analysis.
    
    Args:
        image_path (str): Path to the medical image
        target_size (tuple): Target size for resizing
    
    Returns:
        np.array: Preprocessed image
    
    Raises:
        ValueError: If the image cannot be loaded or is invalid
    """
    # Convert path to string and normalize it
    if not isinstance(image_path, str):
        image_path = str(image_path)
    
    # Load image
    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError(f"Could not load image from path: {image_path}")
    
    # Convert to grayscale if needed
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image
        
    # Apply CLAHE for better contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)
    
    # Denoise
    denoised = cv2.fastNlMeansDenoising(enhanced)
    
    # Resize to target size
    resized = cv2.resize(denoised, target_size)
    
    # Normalize to 0-1 range
    normalized = resized.astype('float32') / 255.0
    
    # Expand dimensions for model input
    preprocessed = np.expand_dims(normalized, axis=-1)
    preprocessed = np.repeat(preprocessed, 3, axis=-1)  # Convert to 3 channels
    preprocessed = np.expand_dims(preprocessed, axis=0)
    
    return preprocessed

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

def analyze_image(image_path):
    """
    Analyze medical images (MRI/CT) using computer vision techniques.
    
    Args:
        image_path (str): Path to the medical image file
    
    Returns:
        str: Analysis results with findings
    """
    try:
        # Convert path to Path object for better handling
        image_path = Path(image_path)
        if not image_path.exists():
            raise ValueError(f"Image file not found: {image_path}")
            
        # Load image
        logger.info(f"Loading image from: {image_path}")
        image = Image.open(image_path)
            
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