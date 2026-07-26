import streamlit as st
import requests
import time

# Enkel opsætning af siden
st.title("🎬 Min Gratis AI-Video Generator")
st.write("Skriv en prompt og lad AI lave en rigtig video til dig helt gratis.")

# Tekstfeltet hvor du skriver din prompt
user_prompt = st.text_input("Hvad skal videoen handle om?", "En rød bil der kører i regnvejr, 4k, cinematic")

# Hent din hemmelige Write-nøgle sikkert
HF_TOKEN = st.secrets["HF_TOKEN"]

# VI SKIFTER TIL EN HELT ÅBEN OG GRATIS VIDEOMODEL HER:
API_URL = "https://huggingface.co"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# Knap til at starte videogenereringen
if st.button("🚀 Generer Video ud fra prompt"):
    if not user_prompt:
        st.warning("Skriv venligst en tekst først.")
    else:
        with st.spinner("AI danner din video... Det tager normalt under 1 minut..."):
            payload = {"inputs": user_prompt}
            response = requests.post(API_URL, headers=headers, json=payload)
            
            # Hvis AI-modellen lige skal startes op på serveren
            if response.status_code == 503:
                st.info("AI-serveren starter op. Vent lige 20 sekunder...")
                time.sleep(20)
                response = requests.post(API_URL, headers=headers, json=payload)

            if response.status_code == 200:
                # Viser den færdige video på skærmen
                st.video(response.content)
                st.success("Din video er klar!")
            else:
                st.error(f"Fejl fra AI-serveren: {response.status_code}. Prøv igen om et øjeblik.")
