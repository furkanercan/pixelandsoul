import streamlit as st

# Set page configuration
st.set_page_config(page_title="Pixel & Soul Photography", page_icon=":camera:")

# Main container - center everything
container = st.container()

with container:
    st.markdown(
        """
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh;">
            <h1 style="font-family: 'Arial', sans-serif; font-weight: bold;">Pixel & Soul Photography</h1>
            <img src="Pixel_Soul_Logo_HighRes.png" alt="Pixel & Soul Logo" style="max-width: 300px; width: 100%; height: auto; margin: 20px 0;">
            <h2>Website Coming Soon!</h2>
            <p style="font-size: 16px;">Follow us on Instagram <strong>@pixelandsoulphoto</strong></p>
        </div>
        """,
        unsafe_allow_html=True
    )
