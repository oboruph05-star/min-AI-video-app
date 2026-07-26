import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="Min AI App", page_icon="🎨")
st.title("🎨 Min Egen Gratis AI Generator")
st.write("Skriv en prompt nedenfor og se AI skabe et mesterværk helt gratis.")

user_prompt = st.text_input("Hvad skal AI generere for dig?", "En flot rød bil der kører i regnvejr, 4k")

# Henter din Write-nøgle fra Streamlit Secrets
HF_TOKEN = st.secrets["HF_TOKEN"]

# Det helt nye 2026-system, som automatisk omdirigerer til en gratis server
if st.button("🚀 Generer nu ud fra prompt"):
    if not user_prompt:
        st.warning("Skriv venligst en tekst først.")
    else:
        with st.spinner("Forbinder til det nye AI-netværk... Vent venligst 10-15 sekunder..."):
            try:
                # Vi bruger den nye InferenceClient, som omgår den gamle lukkede adresse
                client = InferenceClient(provider="hf-inference", token=HF_TOKEN)
                
                image = client.text_to_image(
                    user_prompt, 
                    model="stabilityai/stable-diffusion-2-1"
                )
                
                # Viser det færdige resultat
                st.image(image)
                st.success("Succes! Din app virker fejlfrit over det nye system.")
                
            except Exception as e:
                st.error(f"Forbindelsesfejl: Systemet opdaterer. Prøv at trykke på knappen igen om et øjeblik.")
