import streamlit as st
import pandas as pd
import joblib
import os

# Set up page configurations
st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="centered")

st.title("💻 Laptop Price Predictor")
st.write("Input the laptop specifications below to predict the estimated price.")

# Load the saved model pipeline
model_path = 'laptop_model.pkl'

if os.path.exists(model_path):
    model = joblib.load(model_path)
    
    # User Inputs matching the dataset profile
    company = st.selectbox('Brand / Company', ['Apple', 'HP', 'Dell', 'ASUS', 'Lenovo'])
    type_name = st.selectbox('Type', ['Ultrabook', 'Notebook', 'Gaming', 'ZenBook'])
    ram = st.slider('RAM (in GB)', min_value=4, max_value=64, value=8, step=4)
    opsys = st.selectbox('Operating System', ['macOS', 'Windows 10', 'No OS'])
    weight = st.number_input('Weight of Laptop (in kg)', min_value=0.5, max_value=4.0, value=1.5, step=0.1)

    # Predict Button
    if st.button('🔮 Predict Price'):
        # Convert inputs into DataFrame
        input_data = pd.DataFrame([{
            'Company': company,
            'TypeName': type_name,
            'Ram': ram,
            'OpSys': opsys,
            'Weight': weight
        }])
        
        prediction = model.predict(input_data)[0]
        st.success(f"💰 Estimated Price: **\${prediction:,.2f}**")
else:
    st.error("⚠️ Model file not found! Please run `python src/train.py` first to train and generate the model.")
