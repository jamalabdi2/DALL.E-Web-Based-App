import openai
from PIL import Image
import urllib.request
import matplotlib.pyplot as plt
import streamlit as st
import time


def generate_images(api_key_file, image_description):
    # Read OpenAI API key from file
    with open(api_key_file, 'r') as f:
        api_key = f.read().strip()

    # Set OpenAI API key
    openai.api_key = api_key
    
    # Generate images using OpenAI API
    #img_response = openai.Image.create(n_images, image_size,prompt=image_description)
    img_response = openai.Image.create(prompt=image_description,n =1,size='512x512' )
    img_url = img_response['data'][0]['url']
    urllib.request.urlretrieve(img_url,'image.png')
    img = Image.open('image.png')
    return img

api_key_file = 'api_key.txt'

# streamlit
st.title('DALLE.E Image Generation')
image_description  = st.text_input('Image Description')
#number_of_images = st.radio('How many images do you want to generate?:',(1,2,3))
#image_size = st.radio('What size do you want the image(s) to be?: ',('256x256', '512x512', '1024x1024'))
print('Image description: ',image_description)
if st.button('Generate Image'):
    generated_image = generate_images(api_key_file,image_description)
    st.image(generated_image)
    st.success('Finally done')
    st.balloons()
    
