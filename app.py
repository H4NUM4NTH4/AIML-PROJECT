import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("house_price_model.pkl")

# Set up the web page
st.set_page_config(page_title="Real Estate Valuation", layout="centered")

# UI Title
st.title("🏡 Real Estate Valuation App")
st.markdown("Enter the details below to get the estimated house price.")

# User Input Fields
bedrooms = st.number_input("🛏 Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("🛁 Bathrooms", min_value=1, max_value=10, value=2)
sqft = st.number_input("📏 Square Feet Area", min_value=300, max_value=10000, value=1500)
zipcode = st.text_input("📍 Zip Code", value="12345")

# Predict Button
if st.button("🔍 Predict Price"):
    # Convert input to DataFrame
    input_data = pd.DataFrame([[bedrooms, bathrooms, sqft, zipcode]], 
                              columns=["beds", "baths", "size", "zip_code"])
    
    # Make Prediction
    predicted_price = model.predict(input_data)[0]

    # Display Output
    st.success(f"💰 Estimated House Price: **${predicted_price:,.2f}**")
