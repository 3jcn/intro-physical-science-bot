import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import string
import random
import datetime
import wikipedia
import pyttsx3
import speech_recognition as sr
import numpy as np
import pywhatkit
import warnings
warnings.filterwarnings('ignore')


header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
modelTraining = st.beta_container()

st.markdown("""
	<style>
	.main{
	background-color: #f5f5f5;
	}
	</style>
	""",
	unsafe_allow_html=True
)

@st.cache
def get_data(filename):
	data = pd.read_csv(filename)
	return data
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

with header:
	st.text('@Author: Thomas Nguyen Date: 28 Feb 2021')
	st.title('AI Project:')
	#st.header('Physics Assistant Bot for Introductory of Physical Science')
	html_temp = """
	<div style="background-color:tomato; padding:10px">
	<h2 style="color:white; text-align:center;">Predicting House Price in La Jolla, San Diego, CA</h2>
	</div>
	"""
	st.markdown(html_temp,unsafe_allow_html=True)
	st.text('Physical Science is a major division of Natural Science. There are five major branches: physics, chemistry, astronomy, geology, and meteorology.')
	#html = f"<a href='{link}'><img src='data:image/png;base64,{image_base64}'></a>"
	#st.markdown(html, unsafe_allow_html=True)
	image = Image.open('lajolla.jpg')
	st.image(image,use_column_width=True)

with dataset:
	st.header('La Jolla house price dataset Feb 2021')
	st.text('Data from online sites like Zillow, Redfin, Realtor, etc.')
	data = get_data('LaJolla-02-2021.csv')
	
	
with features:
	st.header('The ML models:')
	st.markdown('* **Multivariate Linear Regression** ')
	st.markdown('* **Extreme Gradient Boosting XGBClassifier** ')

with modelTraining:
	st.header('Estimate the price for a house with the following selected features:')
	para_col,disp_col = st.beta_columns(2)
	n_area = para_col.slider('Area of the house (sq ft):',min_value=600,max_value=19000, value=2000)
	n_beds = para_col.selectbox('Number of bedrooms:',options=[1,2,3,4,5,6,7,8],index=2)
	n_baths = para_col.selectbox('Number of full bathrooms:',options=[1,2,3,4,5,6,7,8],index=2)
	n_half = para_col.selectbox('Number of 1.5-bathrooms:',options=[0,1,2,3,4],index=0)


	disp_col.subheader('The price of the house:')
	disp_col.write(abs(lr.predict([[n_area,n_beds,n_baths,n_half]])))
	disp_col.subheader('R squared score of the MLR model:')
	disp_col.write(score)

	disp_col.subheader('R squared score of XGBRegressor model:')
	disp_col.write(score2)


