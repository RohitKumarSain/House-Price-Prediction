import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load('model.joblib')

import sys
st.write(sys.version)

# App Title
st.title("🏠 California House Price Prediction")

st.write("Enter house details below:")

# ---------------- USER INPUTS ---------------- #

longitude = st.number_input("Longitude", value=-122.23)

latitude = st.number_input("Latitude", value=37.88)

housing_median_age = st.number_input(
    "Housing Median Age",
    min_value=0.0,
    value=41.0
)

total_rooms = st.number_input(
    "Total Rooms",
    min_value=0.0,
    value=880.0
)

total_bedrooms = st.number_input(
    "Total Bedrooms",
    min_value=0.0,
    value=129.0
)

population = st.number_input(
    "Population",
    min_value=0.0,
    value=322.0
)

households = st.number_input(
    "Households",
    min_value=0.0,
    value=126.0
)

median_income = st.number_input(
    "Median Income",
    min_value=0.0,
    value=8.3252
)

# Categorical Feature
ocean_proximity = st.selectbox(
    "Ocean Proximity",
    (
        '<1H OCEAN',
        'INLAND',
        'ISLAND',
        'NEAR BAY',
        'NEAR OCEAN'
    )
)

# ---------------- PREDICTION ---------------- #

if st.button("Predict House Price"):

    # Create input dataframe
    input_data = pd.DataFrame({
        'longitude': [longitude],
        'latitude': [latitude],
        'housing_median_age': [housing_median_age],
        'total_rooms': [total_rooms],
        'total_bedrooms': [total_bedrooms],
        'population': [population],
        'households': [households],
        'median_income': [median_income],
        'ocean_proximity': [ocean_proximity]
    })

    # Prediction
    prediction = model.predict(input_data)

    # Show Result
    st.success(f"Predicted House Price: ${prediction[0]:,.2f}")