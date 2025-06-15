#!/usr/bin/env python3
"""
🔄 Transfer Learning Explorer - Streamlit App
=====================================

Interactive web app for exploring Transfer Learning techniques
and pre-trained model comparisons.

Author: IU Data Analytics Course
Date: 2025
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.applications import (
    ResNet50, VGG16, MobileNetV2, EfficientNetB0, 
    DenseNet121, Xception, InceptionV3
)
from tensorflow.keras.datasets import cifar10
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image
import time

# Page Configuration
st.set_page_config(
    page_title="🔄 Transfer Learning Explorer",
    page_icon="🔄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #ff7f0e;
        margin: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 0.5rem 0;
    }
    .info-box {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .strategy-box {
        border: 2px solid #4ecdc4;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        background-color: #f0fdfa;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">🔄 Transfer Learning Explorer</h1>', 
            unsafe_allow_html=True)
st.markdown("**Interaktive Exploration von Transfer Learning Strategien**")

# Sidebar Configuration
st.sidebar.header("🎛️ Transfer Learning Konfiguration")

# Available Models
AVAILABLE_MODELS = {
    'ResNet50': {
        'class': ResNet50,
        'params': 25.6,
        'top1_imagenet': 74.9,
        'description': 'Deep Residual Networks mit Skip Connections'
    },
    'EfficientNetB0': {
        'class': EfficientNetB0,
        'params': 5.3,
        'top1_imagenet': 77.1,
        'description': 'Efficient Neural Architecture Search optimiert'
    },
    'MobileNetV2': {
        'class': MobileNetV2,
        'params': 3.5,
        'top1_imagenet': 71.8,
        'description': 'Mobile-optimiert mit Depthwise Separable Convolutions'
    },
    'VGG16': {
        'class': VGG16,
        'params': 138.4,
        'top1_imagenet': 71.3,
        'description': 'Klassische CNN-Architektur, sehr tief'
    },
    'DenseNet121': {
        'class': DenseNet121,
        'params': 8.0,
        'top1_imagenet': 75.0,
        'description': 'Dense Connections zwischen allen Layern'
    }
}

# Load and Cache Data
@st.cache_data
def load_cifar10():
    """Load CIFAR-10 dataset"""
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    
    # Normalize
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    
    # Class names
    classes = [
        'Flugzeug', 'Auto', 'Vogel', 'Katze', 'Hirsch',
        'Hund', 'Frosch', 'Pferd', 'Schiff', 'LKW'
    ]
    
    return x_train, y_train, x_test, y_test, classes

# Performance Prediction Function
def predict_transfer_learning_performance(model_name, strategy, learning_rate, 
                                        unfreeze_layers, batch_size):
    """
    Predict expected performance based on Transfer Learning parameters
    """
    # Base performance from ImageNet accuracy adjusted for CIFAR-10
    base_imagenet_acc = AVAILABLE_MODELS[model_name]['top1_imagenet'] / 100
    base_cifar10_acc = min(0.95, base_imagenet_acc + 0.1)  # Rough estimation
    
    # Strategy adjustments
    if strategy == 'Feature Extraction':
        strategy_adj = 0.0
    elif strategy == 'Fine-tuning':
        strategy_adj = 0.03
    else:  # Gradual Unfreezing
        strategy_adj = 0.05
    
    # Learning rate adjustment
    if learning_rate > 0.01:
        lr_adj = -0.03
    elif learning_rate < 0.0001:
        lr_adj = -0.02
    else:
        lr_adj = 0.01
    
    # Unfreeze layers adjustment
    if strategy != 'Feature Extraction':
        if unfreeze_layers < 20:
            unfreeze_adj = -0.01
        elif unfreeze_layers > 80:
            unfreeze_adj = -0.02
        else:
            unfreeze_adj = 0.01
    else:
        unfreeze_adj = 0
    
    # Model-specific adjustments
    if model_name == 'EfficientNetB0':
        model_adj = 0.02
    elif model_name == 'MobileNetV2':
        model_adj = -0.02
    else:
        model_adj = 0
    
    final_acc = base_cifar10_acc + strategy_adj + lr_adj + unfreeze_adj + model_adj
    return max(0.6, min(0.98, final_acc))

# Load data
x_train, y_train, x_test, y_test, classes = load_cifar10()

# Sidebar Controls
st.sidebar.subheader("🏗️ Model Auswahl")
selected_model = st.sidebar.selectbox(
    "Pre-trained Model",
    list(AVAILABLE_MODELS.keys()),
    help="Wählen Sie ein pre-trained Model aus"
)

st.sidebar.subheader("🔧 Transfer Learning Strategie")
strategy = st.sidebar.selectbox(
    "Strategie",
    ["Feature Extraction", "Fine-tuning", "Gradual Unfreezing"],
    help="Feature Extraction: Base frozen, Fine-tuning: Base trainable"
)

st.sidebar.subheader("⚙️ Hyperparameter")
learning_rate = st.sidebar.select_slider(
    "Learning Rate",
    options=[0.1, 0.01, 0.001, 0.0001, 0.00001],
    value=0.001,
    format_func=lambda x: f"{x:.0e}"
)

if strategy != "Feature Extraction":
    unfreeze_layers = st.sidebar.slider(
        "Layers to Unfreeze", 0, 100, 50,
        help="Anzahl der zu trainierenden Layer vom Ende"
    )
else:
    unfreeze_layers = 0

batch_size = st.sidebar.selectbox("Batch Size", [16, 32, 64], index=1)

# Main Content
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<h2 class="sub-header">🏗️ Model Information</h2>', 
                unsafe_allow_html=True)
    
    model_info = AVAILABLE_MODELS[selected_model]
    
    st.markdown(f"""
    <div class="info-box">
        <strong>📊 {selected_model}</strong><br>
        <strong>Parameter:</strong> {model_info['params']} Million<br>
        <strong>ImageNet Top-1:</strong> {model_info['top1_imagenet']}%<br>
        <strong>Beschreibung:</strong> {model_info['description']}
    </div>
    """, unsafe_allow_html=True)
    
    # Predict performance
    predicted_acc = predict_transfer_learning_performance(
        selected_model, strategy, learning_rate, unfreeze_layers, batch_size
    )
    
    st.markdown(f"""
    <div class="metric-card">
        <strong>🎯 Predicted CIFAR-10 Accuracy</strong><br>
        <h2>{predicted_acc:.1%}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<h2 class="sub-header">📊 Performance Analysis</h2>', 
                unsafe_allow_html=True)
    
    # Create comparison with different strategies
    strategies = ["Feature Extraction", "Fine-tuning", "Gradual Unfreezing"]
    strategy_performances = []
    
    for strat in strategies:
        perf = predict_transfer_learning_performance(
            selected_model, strat, learning_rate, unfreeze_layers, batch_size
        )
        strategy_performances.append(perf)
    
    # Create plotly chart
    fig = go.Figure(data=[
        go.Bar(
            x=strategies,
            y=strategy_performances,
            marker_color=['#FF6B6B', '#4ECDC4', '#45B7D1'],
            text=[f'{p:.1%}' for p in strategy_performances],
            textposition='auto',
        )
    ])
    
    # Highlight selected strategy
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    selected_color = colors[strategies.index(strategy)]
    
    fig.update_traces(
        marker_color=[selected_color if s == strategy else '#E0E0E0' 
                     for s in strategies]
    )
    
    fig.update_layout(
        title=f"🔄 {selected_model} Strategy Comparison",
        yaxis_title="Predicted Accuracy",
        showlegend=False,
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

# Model Architecture Comparison
st.markdown('<h2 class="sub-header">🏗️ Model Architecture Comparison</h2>', 
            unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    # Parameters comparison
    model_names = list(AVAILABLE_MODELS.keys())
    params = [AVAILABLE_MODELS[name]['params'] for name in model_names]
    
    fig_params = px.bar(
        x=model_names,
        y=params,
        title="📊 Model Size (Million Parameters)",
        labels={'x': 'Model', 'y': 'Parameters (M)'},
        color=params,
        color_continuous_scale='viridis'
    )
    
    # Highlight selected model
    fig_params.update_traces(
        marker_color=[
            'red' if name == selected_model else 'lightgray' 
            for name in model_names
        ]
    )
    
    st.plotly_chart(fig_params, use_container_width=True)

with col2:
    # ImageNet performance vs Parameters
    imagenet_accs = [AVAILABLE_MODELS[name]['top1_imagenet'] for name in model_names]
    
    fig_scatter = px.scatter(
        x=params,
        y=imagenet_accs,
        text=model_names,
        title="🎯 ImageNet Accuracy vs Model Size",
        labels={'x': 'Parameters (M)', 'y': 'ImageNet Top-1 Accuracy (%)'},
        size=[10 if name == selected_model else 5 for name in model_names],
        color=[1 if name == selected_model else 0 for name in model_names],
        color_discrete_map={0: 'lightgray', 1: 'red'}
    )
    
    fig_scatter.update_traces(textposition="top center")
    st.plotly_chart(fig_scatter, use_container_width=True)

# Transfer Learning Strategy Guide
st.markdown('<h2 class="sub-header">💡 Transfer Learning Strategy Guide</h2>', 
            unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="strategy-box">
        <h4>🔒 Feature Extraction</h4>
        <strong>Wann nutzen:</strong><br>
        • Kleiner Datensatz<br>
        • Ähnlich zu ImageNet<br>
        • Schnelle Prototypen<br><br>
        <strong>Vorteile:</strong><br>
        • Sehr schnell<br>
        • Wenig GPU-Speicher<br>
        • Stabil<br><br>
        <strong>Nachteile:</strong><br>
        • Begrenzte Anpassung
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="strategy-box">
        <h4>🔄 Fine-tuning</h4>
        <strong>Wann nutzen:</strong><br>
        • Mittlerer Datensatz<br>
        • Unterschiedlich zu ImageNet<br>
        • Production-Ready<br><br>
        <strong>Vorteile:</strong><br>
        • Beste Performance<br>
        • Gute Anpassung<br>
        • Flexibel<br><br>
        <strong>Nachteile:</strong><br>
        • Längere Training<br>
        • Overfitting-Risiko
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="strategy-box">
        <h4>🚀 Gradual Unfreezing</h4>
        <strong>Wann nutzen:</strong><br>
        • Großer Datensatz<br>
        • Maximum Performance<br>
        • Research/Competition<br><br>
        <strong>Vorteile:</strong><br>
        • Höchste Accuracy<br>
        • Stabiles Training<br>
        • State-of-the-art<br><br>
        <strong>Nachteile:</strong><br>
        • Sehr zeitaufwändig<br>
        • Komplex zu implementieren
    </div>
    """, unsafe_allow_html=True)

# Interactive Hyperparameter Impact
st.markdown('<h2 class="sub-header">🎛️ Hyperparameter Impact Analysis</h2>', 
            unsafe_allow_html=True)

if st.button("📊 Analyze Hyperparameter Impact"):
    # Create analysis for different learning rates
    lr_values = [0.1, 0.01, 0.001, 0.0001, 0.00001]
    lr_performances = []
    
    for lr in lr_values:
        perf = predict_transfer_learning_performance(
            selected_model, strategy, lr, unfreeze_layers, batch_size
        )
        lr_performances.append(perf)
    
    # Create interactive plot
    fig_lr = go.Figure()
    
    fig_lr.add_trace(go.Scatter(
        x=[f"{lr:.0e}" for lr in lr_values],
        y=lr_performances,
        mode='lines+markers',
        name='Predicted Accuracy',
        line=dict(color='#4ECDC4', width=3),
        marker=dict(size=10)
    ))
    
    # Highlight current learning rate
    current_idx = lr_values.index(learning_rate)
    fig_lr.add_trace(go.Scatter(
        x=[f"{learning_rate:.0e}"],
        y=[lr_performances[current_idx]],
        mode='markers',
        name='Current Setting',
        marker=dict(size=15, color='red', symbol='star')
    ))
    
    fig_lr.update_layout(
        title="📈 Learning Rate Impact on Performance",
        xaxis_title="Learning Rate",
        yaxis_title="Predicted Accuracy",
        height=400
    )
    
    st.plotly_chart(fig_lr, use_container_width=True)

# Model Training Simulation
st.markdown('<h2 class="sub-header">⏱️ Training Time Estimation</h2>', 
            unsafe_allow_html=True)

# Estimate training time based on model and strategy
base_time = AVAILABLE_MODELS[selected_model]['params'] / 10  # Base time in minutes

if strategy == "Feature Extraction":
    time_multiplier = 0.2
elif strategy == "Fine-tuning":
    time_multiplier = 1.0
else:  # Gradual Unfreezing
    time_multiplier = 2.0

estimated_time = base_time * time_multiplier

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Estimated Training Time", f"{estimated_time:.1f} min")

with col2:
    st.metric("Memory Usage", f"{AVAILABLE_MODELS[selected_model]['params'] * 4:.1f} MB")

with col3:
    st.metric("Model Parameters", f"{AVAILABLE_MODELS[selected_model]['params']} M")

with col4:
    st.metric("ImageNet Baseline", f"{AVAILABLE_MODELS[selected_model]['top1_imagenet']}%")

# Best Practices
st.markdown('<h2 class="sub-header">🎯 Best Practices</h2>', 
            unsafe_allow_html=True)

st.markdown("""
### 📋 Transfer Learning Checklist:

1. **🔍 Model Selection:**
   - EfficientNet für beste Accuracy/Parameter Ratio
   - MobileNet für Mobile/Edge Deployment
   - ResNet für allgemeine Anwendungen

2. **⚙️ Hyperparameter Tuning:**
   - Learning Rate 10-100x niedriger für Fine-tuning
   - Kleinere Batch Sizes für Fine-tuning
   - Early Stopping zur Overfitting-Vermeidung

3. **📊 Training Strategy:**
   - Starte immer mit Feature Extraction
   - Graduelles Unfreezing für beste Ergebnisse
   - Monitor Validation Metrics kontinuierlich

4. **🚀 Production Deployment:**
   - Model Compression für mobile Anwendungen
   - A/B Testing verschiedener Architecturen
   - Continuous Learning mit neuen Daten
""")

st.markdown("---")
st.markdown("**🎓 IU Data Analytics & Big Data Course - Week 6.4: Transfer Learning**")
st.markdown("Experimentieren Sie mit verschiedenen Models und Strategien!")
