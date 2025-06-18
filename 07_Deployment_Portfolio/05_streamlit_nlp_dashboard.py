import streamlit as st
import requests
import json
from datetime import datetime

st.set_page_config(
    page_title="Modern NLP Dashboard",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Modern NLP Dashboard")
st.markdown("**Transformer-basierte NLP Services**")

# Sidebar
st.sidebar.header("⚙️ Konfiguration")
api_url = st.sidebar.text_input("NLP API URL", "http://localhost:8000")

# Main Content
tab1, tab2, tab3 = st.tabs(["✍️ Text Generation", "😊 Sentiment", "❓ Q&A"])

with tab1:
    st.header("✍️ Text Generation")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        prompt = st.text_area("Prompt eingeben:", "Once upon a time")
        
    with col2:
        max_length = st.slider("Max Length", 50, 200, 100)
        temperature = st.slider("Temperature", 0.1, 1.0, 0.7)
        
    if st.button("🚀 Generate Text", type="primary"):
        with st.spinner("Generiere Text..."):
            try:
                response = requests.post(
                    f"{api_url}/generate",
                    json={
                        "prompt": prompt,
                        "max_length": max_length,
                        "temperature": temperature
                    }
                )
                
                if response.status_code == 200:
                    result = response.json()
                    st.success("Text erfolgreich generiert!")
                    st.write("**Generated Text:**")
                    st.write(result["generated_texts"][0])
                else:
                    st.error(f"API Fehler: {response.status_code}")
            except Exception as e:
                st.error(f"Verbindungsfehler: {str(e)}")

with tab2:
    st.header("😊 Sentiment Analysis")
    
    text_input = st.text_area("Text für Sentiment Analysis:")
    
    if st.button("🔍 Analyze Sentiment", type="primary"):
        if text_input:
            with st.spinner("Analysiere Sentiment..."):
                try:
                    response = requests.post(
                        f"{api_url}/sentiment",
                        json={"text": text_input}
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        sentiment = result["sentiment"]
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Sentiment", sentiment["label"])
                        with col2:
                            st.metric("Confidence", f"{sentiment['confidence']:.2%}")
                            
                        # Emoji basierend auf Sentiment
                        emoji = "😊" if sentiment["label"] == "POSITIVE" else "😔"
                        st.write(f"## {emoji} {sentiment['label']}")
                        
                    else:
                        st.error(f"API Fehler: {response.status_code}")
                except Exception as e:
                    st.error(f"Verbindungsfehler: {str(e)}")
        else:
            st.warning("Bitte Text eingeben")

with tab3:
    st.header("❓ Question Answering")
    
    context = st.text_area("Kontext:", height=150)
    question = st.text_input("Frage:")
    
    if st.button("💡 Answer Question", type="primary"):
        if context and question:
            with st.spinner("Beantworte Frage..."):
                try:
                    response = requests.post(
                        f"{api_url}/qa",
                        json={
                            "context": context,
                            "question": question
                        }
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        answer = result["answer"]
                        
                        st.success("Antwort gefunden!")
                        st.write(f"**Antwort:** {answer['answer']}")
                        st.write(f"**Confidence:** {answer['confidence']:.2%}")
                        
                    else:
                        st.error(f"API Fehler: {response.status_code}")
                except Exception as e:
                    st.error(f"Verbindungsfehler: {str(e)}")
        else:
            st.warning("Bitte Kontext und Frage eingeben")

# Footer
st.divider()
st.caption(f"Modern NLP Dashboard - {datetime.now().strftime('%H:%M:%S')}")
