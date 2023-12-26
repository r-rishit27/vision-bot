import streamlit as st

from PIL import Image

import google.generativeai as genai



genai.configure(api_key="AIzaSyBC8QHmbUHNWDhu4dC7v5bppEySFemctTM")


## Function to load OpenAI model and get respones

def get_gemini_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(image)
    return response.text


##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Vision GPT")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

## If ask button is clicked

if submit:
    response = get_gemini_response(input, image)
    st.subheader("Response: ")
    st.write(response)