import streamlit as st
import pandas as pd
import pickle

# Load the trained model
filename = 'rf_model.pkl'
rf_model = pickle.load(open(filename, 'rb'))

# Create a title for the app
st.title("Marketing Response Prediction App")

# Create input fields for user input
# Replace these with the actual features from your dataset
st.header("Enter Customer Information:")
age = st.number_input("Age", min_value=18, max_value=100, value=30)
income = st.number_input("Income", min_value=0, max_value=1000000, value=50000)
education = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
# Add more input fields for other features as needed

# Create a button to make predictions
if st.button("Predict Response"):
    # Create a DataFrame with the user input
    input_data = pd.DataFrame({
        'Age': [age],
        'Income': [income],
        # Add other features here
    })

    # Perform one-hot encoding for categorical features if needed
    # ...

    # Make predictions using the loaded model
    prediction = rf_model.predict(input_data)[0]

    # Display the prediction
    if prediction == 1:
        st.success("The customer is likely to respond to the marketing campaign.")
    else:
        st.warning("The customer is likely not to respond to the marketing campaign.")
