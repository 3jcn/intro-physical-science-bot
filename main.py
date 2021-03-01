import streamlit as st
from PIL import Image
import string
import random
import speech_recognition as sr
from run_query import run_query, talk
import warnings
warnings.filterwarnings('ignore')

r = sr.Recognizer()

def wakeWord(text):
    wake_list = ['max', 'hi max', 'hey max', 'hello max', 'hola max']
    text = text.lower()
    for phrase in wake_list:
        if phrase in text:
            return True
    return False


def start_function():
    talk("Hi, my name is Max. I am professor Nguyen's assistant.")
    talk("How may I help you with physical science 110?")
    with sr.Microphone() as source:                
        while True:
            r.adjust_for_ambient_noise(source)
            r.pause_threshold = 0.5
            audio = r.listen(source)
            try:
                command = r.recognize_google(audio)
                #command = command.lower()
                #disp.write("You said: " + command) 

                if 'bye' in command:   
                    talk('On behalf of professor Nguyen, thank you for studying.')
                    break
                else:
                    #if(wakeWord(command)==True):
                    run_query(command)
            except LookupError:
                #print("Please, speak more clearly")
                pass
	
#################################################################################
header = st.beta_container()

st.markdown("""
	<style>
	.main{
	background-color: #f5f5f5;
	}
        .stButton>button {
        background-color: #0000ff;
        color: #ffffff;
        }
	</style>
	""",
	unsafe_allow_html=True
)

with header:
    st.text('@Author: Thomas Nguyen Date: 28 Feb 2021')
    st.title('Virtual Assistant for Introductory of Physical Science')
    st.text('Physical Science is a branch of Natural Science that studies non-living systems.')
    st.text('It has five major divisions: physics, chemistry, astronomy, geology, and meteorology.')

    html_temp = """
	<div style="background-color:tomato; padding:10px">
	<h2 style="color:white; text-align:center;">My name is Max. I am professor Nguyen's assistant.</h2>
	</div>
	"""
    st.markdown(html_temp,unsafe_allow_html=True)

    
    st.text('Hi Students, click the button below to ask me some questions about physical science!')
    st.text("For example, 'what is velociy', 'what is entropy', 'Newton's second law',... ") 
    st.text("If you are tired, you can ask me to play music by saying: play 'song name or artist name'")
    st.text("or 'who is ..?', 'what time is it?', 'what date is it?', 'from wikipedia, what...'.")
    button_start = st.button('Start Conversation')
    if button_start:
    	start_function()
    st.text("Say 'bye Max' to stop the conversation or click 'Stop' button on the top right corner of the page.")
    image = Image.open('max.png')
    st.image(image,use_column_width=True)

############################################################################       
# Unintelligible Speech: When Python cannot match some audio to text, it raises an UnknownValueError exception.