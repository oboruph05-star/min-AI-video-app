import streamlit as st
import requests
import time

# Flot opsætning af siden
st.set_page_config(page_title="Min AI App", page_icon="🎨", layout="centered")
st.title("🎨 Min Egen Gratis AI Generator")
st.write("Skriv en prompt nedenfor og se AI skabe et mesterværk helt gratis.")

# Tekstfeltet hvor du skriver din prompt
user_prompt = st.text_input("Hvad skal AI generere for dig?", "En flot rød bil der kører i regnvejr, 4k, cinematic")

# Hent din hemmelige Write-nøgle sikkert
HF_TOKEN = st.secrets["HF_TOKEN"]

# Vi skifter til den stabile model, som altid tillader gratis adgang:
API_URL = "https://huggingface.co"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# Knap til at starte genereringen
if st.button("🚀 Generer nu ud fra prompt"):
    if not user_prompt:
        st.warning("Skriv venligst en tekst først.")
    else:
        with st.spinner("AI arbejder i skyen... Vent venligst 10-15 sekunder..."):
            payload = {"inputs": user_prompt}
            response = requests.post(API_URL, headers=headers, json=payload)
            
            # Hvis AI-modellen lige skal startes op på serveren
            if response.status_code == 503:
                st.info("AI-serveren vågner i skyen. Vi prøver igen om 15 sekunder...")
                time.sleep(15)
                response = requests.post(API_URL, headers=headers, json=payload)

            if response.status_code == 200:
                # Viser det færdige resultat direkte på din app-skærm
                st.image(response.content)
                st.success("Det lykkedes! Din app virker fuldstændig fejlfrit.")
            else:
                st.error(f"Fejl fra AI-serveren: {response.status_code}. Serveren har travlt, prøv igen om et øjeblik.")
