import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Change Name & Logo
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️")

# Background Image Setup
background_image_url = "https://www.strategyand.pwc.com/m1/en/strategic-foresight/sector-strategies/healthcare/ai-powered-healthcare-solutions/img01-section1.jpg"

# Custom CSS for Background & UI Styling
st.markdown(f"""
    <style>
    /* Set Background Image */
    .stApp {{
        background: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Hide Streamlit Default Menus */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}

    /* Style Dropdown Text */
    div[data-testid="stSelectbox"] label {{
        color: black !important;
        font-weight: bold;
    }}

    div[data-testid="stSelectbox"] div[role="listbox"] * {{
        color: black !important;
        font-weight: bold;
    }}

    /* Change Input Box Text Color */
    input[type="text"], input[type="number"] {{
        color: black !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# Load the saved models
models = {
    'diabetes': pickle.load(open('Models/diabetes_model.sav', 'rb')),
    'heart_disease': pickle.load(open('Models/heart_disease_model.sav', 'rb')),
    'parkinsons': pickle.load(open('Models/parkinsons_model.sav', 'rb')),
    'lung_cancer': pickle.load(open('Models/lungs_disease_model.sav', 'rb')),
    'thyroid': pickle.load(open('Models/Thyroid_model.sav', 'rb'))
}

# Disease Selection Dropdown
selected = st.selectbox(
    'Select a Disease to Predict',
    ['Diabetes Prediction',
     'Heart Disease Prediction',
     'Parkinsons Prediction',
     'Lung Cancer Prediction',
     'Hypo-Thyroid Prediction']
)

def display_input(label, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key)
    elif type == "number":
        return st.number_input(label, key=key, step=1)

# Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction')

    Pregnancies = display_input('Number of Pregnancies', 'Pregnancies', 'number')
    Glucose = display_input('Glucose Level', 'Glucose', 'number')

    if st.button('Check Diabetes'):
        prediction = models['diabetes'].predict([[Pregnancies, Glucose]])
        st.success("Diabetic" if prediction[0] == 1 else "Not Diabetic")
