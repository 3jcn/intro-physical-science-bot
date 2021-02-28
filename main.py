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

# set man's voice:
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
listener = sr.Recognizer()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def run_query(input):
    #input = take_command()
    #print(input)
    if 'play' in input:
        song = input.replace('play','')
        talk('playing...'+ song)
        pywhatkit.playonyt(song)
    elif 'who is' in input:
        person = input.replace('who is','')
        info = wikipedia.summary(person,1)
        talk(info)
        print(info)
    elif 'time' in input:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is ' + time)
        print(time)
    elif 'date' in input:
        date = datetime.datetime.now().date()
        talk(date)
        print(date)
        
    # CHAPTER ONE: MEASUREMENT
    
    elif 'science' in input:
        talk('Science is a systematically organized body of knowledge on a particular subject')
    elif 'physical science' in input:
        talk('there are five major divisions in physical science: physics, chemistry, astronomy, geology and meteorology.')
    elif 'physics' in input:
        talk('Physics is a major division of physical science. it is concerned with the basic principle and concepts of matter and energy')
    elif 'chemistry' in input:
        talk('Chemistry deals with the composition, structure, and reactions of matter.')
    elif 'astronomy' in input:
        talk('Astronomy is the study of the universe: space, time, matter, energy')
    elif 'geology' in input:
        talk('Geology is the science of the planet Earth: composition, structure, processes, history')
    elif 'meteorology' in input:
        talk('meteorology is the study of the atmosphere.')
    elif 'senses' in input:
        talk('there are five human senses: sight, hearing, touch, smell, taste.')
    elif 'unit system' in input:
        talk('in SI system, the standard unit for length is meter, for mass is kilogram and for time is second.')
    
    # CHAPTER TWO: MOTION
    
    elif 'inertia' in input:
        talk('Inertia is the tendency of an object to remain at rest or remain in motion. Inertia is related to mass of an object.')
    elif 'mass' in input:
        talk('mass is amount of matter in a substance.')
    elif 'weight' in input:
        talk('weight is different with mass. weight is the product of mass and gravitational acceleration.')
    elif 'motion' in input:
        talk('An object is in motion when it is undergoing a continuous change in position.')
    elif 'distance' in input:
        talk('Distance is the actual length of the path taken by an object. it is a scalar quatity.')
    elif 'displacement' in input:
        talk('displacement is a vector quantity.')
        talk('displacement is the simply the straight-line distance between where the object started and where it ended up plus direction.')
    elif 'velocity' in input:
        talk('velocity is a vector. it equals displacement divided by time.')
    elif 'speed' in input:
        talk('speed is a scalar quatity. average speed equals distance traveled divided by time to travel the distance.')
    elif 'uniform circular motion' in input:
        talk('uniform circular motion is the motion of an object in a circle at a constant speed.')
    elif 'linear motion' in input:
        talk('linear motion is the motion in one direction.')
    elif 'acceleration' in input:
        talk('in linear motion, acceleration is the time rate of change of velocity.')
    elif 'centripetal acceleration' in input:
        talk('centripetal acceleration equals square of speed divided by the radius of the circular path.')
    elif 'Distance traveled by a dropped object' in input:
        talk('distance traveled by a dropped object d = 0.5*g*t^2. where g is 9.8 meter per second squared.')
        
    # CHAPTER THREE: FORCE & MOTION
    
    elif "newton's laws" in input:
        talk('there are three laws of Newton in classical mechancis.')
    elif "newton's first law" in input:
        talk('an object will remain at rest or in uniform motion in a straight line unless acted on by an external force.')
    elif "newton's second law" in input:
        talk('the acceleration produced by an unbalanced force acting on an object is directly proportional to the magnitud of the force')
        talk('and inversely proportional to the mass of the object.')
    elif "newton's third law" in input:
        talk('for every action there is an equal and opposite reaction')
    elif "newton's gravitational law" in input:
        talk('every particle in the universe attracts every other particle with a force that is directly proportional to the product of their masses')
        talk('and inversely proportional to the square of the distance between them.')
    elif "newton's law of gravitation" in input:
        talk('every particle in the universe attracts every other particle with a force that is directly proportional to the product of their masses')
        talk('and inversely proportional to the square of the distance between them.')
    elif 'torque' in input:
        talk('torque is a vector quantity. it is the vector product of force and lever arm.')
    elif 'linear momentum' in input:
        talk('linear momentum is the product of mass and velocity of an object. it is a vector quantity.')
    elif 'conservation of linear momentum' in input:
        talk('the linear momentum of an object remains constant if there is no external, unbalanced force acting on it.')
    elif 'conservation of angular momentum' in input:
        talk('the angular momentum of an object remains constant if there is no external unbalanced torque acting on it.')
    elif 'angular momentum' in input:
        talk('anular momentum is a vector quantity.')
        talk('it is the product of mass and velocity of an object and distance from the object to the axis of rotation.')
        
    # CHAPTER FOUR: WORK & ENERGY
    
    elif 'work' in input:
        talk('In physics, work applied on an object is the product of distance object moved and horizontall component of force applied on the object ')
        talk('unit of work in SI system is joule.')
    elif 'energy' in input:
        talk('energy is the capacity of doing work. unit of energy is joule.')
    elif 'kinetic energy' in input:
        talk('kinetice energy is the energy of motion. it equals one half of mass time velocity squared. it is always positive.')
    elif 'potential energy' in input:
        talk('potential energy is the energy of position. it is equal to the weight of the object multiplied by the height. it can be negative.')
    elif 'work and kinetic energy' in input:
        talk('work done on the moving object is equal to the change in kinetic energy.')
    elif 'work and potential energy' in input:
        talk('work done by or against gravity sis equal to the change in potential energy.')
    elif 'conservation of energy' in input:
        talk('total energy of an isolated system remains constant.')
        talk('energy cannot be created or destroyed, but it can change from one form to another form of energy.')
    elif 'power' in input:
        talk('power is the time rate of change of work. unit of power in SI system is watt.')
    elif 'forms of energy' in input:
        talk('common forms of energy are chemical energy, electrical energy, nuclear energy, thermal energy, and hydroelectric energy')
    elif 'energy sources' in input:
        talk('common energy sources are coal, oil, natural gas, nuclear, hydroelectric, and renewable sources such as ')
        talk('solar, wind, biofuels, biomass, geothermal, and tides.')
             
    # CHAPTER FIVE: TEMPERATURE & HEAT
    
    elif 'temperature' in input:
        talk('temperature is a measure of the average kinetic energy of the molecules of a substance.')
        talk('unit of temperature in SI system is kelvin.')
    elif 'thermometer' in input:
        talk('thermometer is an instrument to measure temperature.')
    elif 'heat' in input:
        talk('Heat is the form of energy that is transferred between systems or objects with different temperatures.')
    elif 'unit of heat' in input:
        talk('because heat is energy, unit of heat is joule. However, traditional unit of heat is calorie.')
    elif "what's unit of heat" in input:
        talk('unit of heat is joule.')
    elif "calorie" in input:
        talk('a calorie is the amount of heat necessary to raise one gram of pure water by on celsius degree at normal atmospheric pressure')
        talk('one food Calorie is equal to 1000 calories or 4186 joules.')
    elif 'specific heat' in input:
        talk('the amount of heat nessesary to raise the temperature of one kilogram of the subtance one celsius degree.')
    elif 'specific heat capacity' in input:
        talk('specific heat capacity is the same as specific heat')
    elif 'specific heat of water' in input:
        talk('water has highest specific heat capacity 4186 joule per kilogram per celsius')
    elif 'latent heat' in input:
        talk('latent heat is energy absorbed or released by a substance during a change in its physical state or phase that occurs without changing its temperature.')
    elif 'latent heat of vaporization' in input:
        talk('latent heat of vaporization is the latent heat in case of liquid change phase to gas.')
    elif 'latent heat of fusion' in input:
        talk('latent heat of fusion is the latent heat in case of solid change phase to liquid.')
    elif 'phases of matter' in input:
        talk('there are four common phases: solid, liquid, gas and plasma.')
    elif 'solid' in input:
        talk('a solid has relatively fixed molecules and a definite shape and volume.')
    elif 'gas' in input:
        talk('a gas is made up of rapidly moving molecules and assumes the size and shape of its container.')
    elif 'liquid' in input:
        talk('a liquid is an arrangement of molecules that may move and assume the shape of the container.')
    elif 'plasma' in input:
        talk('plasma is a hot gas of electrically charged particles.')
    elif 'heat transfer' in input:
        talk('heat transfer is accomplished by three methods: conduction, convection, and radiation.')
    elif 'conduction' in input:
        talk('conduction is the transfer of heat by molecular collisions, kinetic energy.')
    elif 'convection' in input:
        talk('convection is the transfer of heat by the movement of a substance, or mass, from one place to another.')
    elif 'radiation' in input:
        talk('radiation is the process of transferring energy by means of electromagnetic waves.')
    elif 'ideal gas' in input:
        talk('an ideal gas is one in which the molecules are point particles and interact by collision, no attraction.')
    elif 'pressure' in input:
        talk('pressure is defined as the force per unit area. unit of pressure is Newton per meter squared or pascal.')
    elif 'ideal gas law' in input:
        talk('the pressure of an ideal gas is derectly proportional to the number of molecules and to the kelvin temperature')
        talk('and inversely proportional to the volume.')
    elif 'thermodynamics' in input:
        talk('thermodynamics means the dynamics of heat.')
        talk('its study includes the production of heat, the flow of heat, and the conversion of heat to work.')
    elif 'first law of thermodynamics' in input:
        talk('heat add to a system equals the change in internal energy of the system pluse work done by the system.')
    elif 'second law of thermodynamics' in input:
        talk('it is impossible for heat to flow spontaneously from a colder body to a hotter body.')
        talk('or the entropy of an isolated system never decreases.')
    elif 'third law of thermodynamics' in input:
        talk('it is impossible to attain a teperature of absolute zero in kelvin scale.')
    elif 'pump' in input:
        talk('a heat pump is a device that uses work input to transfer heat from a low temperature reservoir to a high temperature reservoir.')
    elif 'entropy' in input:
        talk('entropy is a mathematical quantity. entropy can be expressed as a measure of the disorder of a system.')
        talk('the total entropy of the universe increases in every natural process.')
    else:
        talk("Please repeat your question again.")
	
# end of function run_query()
# Start chat:
talk("Hi, my name is Max. I am professor Nguyen's assistant.")
talk("How can I help you with physics?")
with sr.Microphone() as source:                
    while True:
        audio = listener.listen(source)
        try:
            #audio = listener.listen(source)
            command = listener.recognize_google(audio)
            command = command.lower()
            print("You said: " + command) 

            if 'stop' in command:    #command =="stop":
                talk('On behalf of professor Nguyen, thank you for studying.')
                break
            else:
                run_query(command)
        except LookupError:
            print("Please, speak more clearly")
	
# end of python part
	
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


