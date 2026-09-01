from mural_analyzer.core.pipeline import analyze_image
import streamlit as st
from PIL import UnidentifiedImageError
import pandas as pd


uploaded_file = st.file_uploader("Upload an image", "image/*")
if uploaded_file is not None:
    try:
        palette_info = analyze_image(uploaded_file)
    except UnidentifiedImageError:
        st.error("Error: The file must be an image")
    else:
        for i, palette_item in enumerate(palette_info):
            r , g, b = palette_item["rgb"]
            cmyw = palette_item["cmyw"]
            percentage = palette_item["percentage"]
            pigments = [
            ("Cian", "#00adf3", cmyw["C"]),
            ("Magenta", "#fc01ff", cmyw["M"]),
            ("Yellow", "#fef900", cmyw["Y"]),
            ("White", "#e5e5e5", cmyw["W"]),
            ]
            if i % 3 == 0:
                columns = st.columns(3)
            with columns[i % 3]:
                with st.container(border=True):
                    st.html(f'<div style="background-color: rgb({r}, {g}, {b}); height: 100px; width: 100%;"></div>')
                    st.progress((percentage / 100), text="Percentage", width="stretch")
                    for name, color, value in pigments:
                        with st.container(gap="xxsmall"):
                            st.caption(f"{name} {value}%")
                            st.html(f'<div style="background-color: #f0f2f6; width: 100%; height: 8px; border-radius: 200px; overflow: hidden"><div style="background-color: {color}; width: {value}%; height: 100%;"></div></div>')


