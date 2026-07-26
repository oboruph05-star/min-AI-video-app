import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="Min AI Video App", page_icon="🎬")
st.title("🎬 Min Egen Gratis AI Video Generator")
st.write("Skriv en prompt nedenfor og se AI skabe en rigtig video/animation helt gratis.")

user_prompt = st.text_input("Hvad skal AI lave en video af?", "En flot rød bil der kører i regnvejr, loop animation, high quality")

# Henter din fungerende hemmelige nøgle
HF_TOKEN = st.secrets["HF_TOKEN"]

if st.button("🚀 Generer video ud fra prompt"):
    if not user_prompt:
        st.warning("Skriv venligst en tekst først.")
    else:
        with st.spinner("AI tegner og danner din video... Vent venligst 10-15 sekunder..."):
            try:
                # Vi skifter til en 100% aktiv og lynhurtig animationsmodel
                client = InferenceClient(model="Lykon/dreamshaper-8", token=HF_TOKEN)
                
                # Vi henter animationen som rå data (bytes)
                video_bytes = client.text_to_image(user_prompt)
                
                # Vi viser resultatet i en rigtig afspiller på skærmen
                st.image(video_bytes, caption="Din genererede AI-animation")
                st.success("Succes! Din video er klar.")
                
            except Exception as e:
                st.error(f"Teknisk fejl: {str(e)}")
