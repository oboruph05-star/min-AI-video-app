import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="Min AI App", page_icon="🎨")
st.title("🎨 Min Egen Gratis AI Generator")
st.write("Skriv en prompt nedenfor og se AI skabe et mesterværk helt gratis.")

user_prompt = st.text_input("Hvad skal AI generere for dig?", "En flot rød bil der kører i regnvejr, 4k")

# Henter din Write-nøgle fra Streamlit Secrets
HF_TOKEN = st.secrets["HF_TOKEN"]

if st.button("🚀 Generer nu ud fra prompt"):
    if not user_prompt:
        st.warning("Skriv venligst en tekst først.")
    else:
        with st.spinner("Forbinder til det nye AI-netværk... Vent venligst 10-15 sekunder..."):
            try:
                # Vi opsætter klienten korrekt med modellen direkte i starten
                client = InferenceClient(model="stabilityai/stable-diffusion-2-1", token=HF_TOKEN)
                
                # Den korrekte måde at kalde billedet på i det nye system
                client = InferenceClient(model="black-forest-labs/FLUX.1-schnell", token=HF_TOKEN)
                
                # Viser det færdige resultat
                st.image(image)
                st.success("Succes! Din app virker fejlfrit.")
                
            except Exception as e:
                # Viser den præcise fejlbesked, hvis noget mod forventning driller
                st.error(f"Teknisk fejl: {str(e)}")
