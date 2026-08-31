from mural_analyzer.core.pipeline import analyze_image
import streamlit as st
from PIL import UnidentifiedImageError


uploaded_file = st.file_uploader("Upload an image", "image/*")
if uploaded_file is not None:
    try:
        palette_info = analyze_image(uploaded_file)
    except UnidentifiedImageError:
        st.error("Error: The file must be an image")
    else:
        st.write(palette_info)