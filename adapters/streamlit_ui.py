from mural_analyzer.core.pipeline import analyze_image
from mural_analyzer.core.circle_packing import pack_circles
import streamlit as st
from PIL import UnidentifiedImageError
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches


uploaded_file = st.file_uploader("Upload an image", "image/*")
col1, col2 = st.columns(2)
n_colors = col1.slider("How many colors?", 2, 255, 16, help="The number of colors to quantize the image to")
merge_threshold = col2.slider("Distance of the colors to blend?", 0, 255, 20, help="The threshold for merging similar colors")
if uploaded_file is not None:
    try:
        palette_info = analyze_image(uploaded_file, n_colors=n_colors, merge_threshold=merge_threshold)
        
    except UnidentifiedImageError:
        st.error("Error: The file must be an image")
    else:

        #Circulos

        fig, ax = plt.subplots()
        palette_circles_info = pack_circles(palette_info)

        for circle_item in palette_circles_info:
            circle = circle_item["circle"]
            r, g, b = circle_item["rgb"]
            color = (r/255, g/255, b/255)
            circle_patch = patches.Circle((circle["x"], circle["y"]), radius=circle["r"], color=color)
            ax.add_patch(circle_patch)

        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)
        ax.set_aspect("equal")
        ax.axis('off')

        st.pyplot(fig)


        #Tarjetas
        _, _, right = st.columns(3)
        if right.toggle("Sort by percentage"):
            palette_info = sorted(palette_info,key=lambda item: item["percentage"], reverse=True)
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


