import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Starts Camera"):
    # Starts the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    # Create a pillow image instance 
    img = Image.open(camera_image)

    # covert the pillow image to grayscale
    gray_img = img.convert("L")
    
    # Render the grayscale image on the webpage
    st.image(gray_img)

    
