import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Pixel & Soul Photography", page_icon=":camera:")

# Load the image
logo = Image.open("images/Pixel_Soul_Logo_HighRes.png")

# Main container
with st.container():
    st.markdown("<h1 style='text-align: center;'>Pixel & Soul Photography</h1>", unsafe_allow_html=True)
    st.image(logo, use_column_width=False, width=300)
    st.markdown("<h2 style='text-align: center;'>Website Coming Soon!</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Follow us on Instagram <strong>@pixelandsoulphoto</strong></p>", unsafe_allow_html=True)
