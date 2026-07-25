import streamlit as st
import requests
import time

# Enkel opsætning af siden
st.title("🎬 Min Gratis AI-Video Generator")
st.write("Skriv en prompt og lad AI lave en video til dig.")

# Tekstfeltet hvor du skriver din prompt
user_prompt = st.text_input("Hvad skal videoen handle om?", "En rød bil der kører i regnvejr")

# Hent den hemmelige nøgle sikkert
HF_TOKEN = st.secrets["HF_TOKEN"]

# Link til AI-videomodellen
API_URL = "https://huggingface.co"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# Knap til at starte
if st.button("Generer Video"):
    if not user_prompt:
        st.warning("Skriv venligst en tekst først.")
    else:
        with st.spinner("AI tænker... Vent venligst 1-2 minutter..."):
            payload = {"inputs": user_prompt}
            response = requests.post(API_URL, headers=headers, json=payload)
            
            if response.status_code == 503:
                st.info("AI-modellen starter op. Vent 20 sekunder...")
                time.sleep(20)
                response = requests.post(API_URL, headers=headers, json=payload)

            if response.status_code == 200:
                st.video(response.content)
                st.success("Din video er klar!")
            else:
                st.error(f"Fejl fra AI-serveren: {response.status_code}. Prøv igen om lidt.")
