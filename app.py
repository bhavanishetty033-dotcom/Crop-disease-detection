import streamlit as st

st.set_page_config(page_title="Crop Disease Detection")

st.title("🌱 Crop Disease Detection")

st.write("Upload a leaf image to detect disease")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display image (no PIL needed)
    st.image(uploaded_file, caption="Uploaded Image")

    st.write("Processing...")

    # Dummy prediction
    st.success("Prediction: Healthy Leaf 🌱")