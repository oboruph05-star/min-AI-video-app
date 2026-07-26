import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="Min AI Video App", page_icon="🎬")
st.title("🎬 Min Egen Gratis AI Video Generator")
st.write("Skriv en prompt nedenfor og se AI skabe en rigtig video helt gratis.")

user_prompt = st.text_input("Hvad skal AI lave en video af?", "En flot rød bil der kører i regnvejr, 4k, animation")

# Henter din opdaterede hemmelige nøgle
HF_TOKEN = st.secrets["HF_TOKEN"]

if st.button("🚀 Generer video ud fra prompt"):
    if not user_prompt:
        st.warning("Skriv venligst en tekst først.")
    else:
        with st.spinner("AI tegner og danner din video... Vent venligst 15-30 sekunder..."):
            try:
                # Vi skifter til en helt åben og gratis videomodel
                client = InferenceClient(model="Kijai/Cosmo-1-test", token=HF_TOKEN)
                
                # Vi beder klienten om at generere en video/animation ud fra din tekst
                video_bytes = client.text_to_video(user_prompt)
                
                # Vi viser resultatet i en rigtig videoafspiller på skærmen
                st.video(video_bytes)
                st.success("Succes! Din video er klar.")
                
            except Exception as e:
                st.error(f"Teknisk fejl: {str(e)}")
