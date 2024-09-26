import streamlit as st
import pandas as pd
import pickle

# Load the trained Lasso model
filename = 'lasso_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Create a Streamlit app
st.title("Monthly Revenue Prediction App")

# Input features for prediction
st.header("Enter Input Features:")

# Get input values from user
website_traffic = st.number_input("Website Traffic", min_value=0)
marketing_spend = st.number_input("Marketing Spend", min_value=0)
customer_acquisition_cost = st.number_input("Customer Acquisition Cost", min_value=0)
average_order_value = st.number_input("Average Order Value", min_value=0)
conversion_rate = st.number_input("Conversion Rate", min_value=0.0, max_value=1.0, step=0.01)

# Create a button to trigger prediction
if st.button("Predict Monthly Revenue"):
    # Create a DataFrame with user input
    input_data = pd.DataFrame({
        'website_traffic': [website_traffic],
        'marketing_spend': [marketing_spend],
        'customer_acquisition_cost': [customer_acquisition_cost],
        'average_order_value': [average_order_value],
        'conversion_rate': [conversion_rate]
    })

    # Make the prediction
    predicted_revenue = loaded_model.predict(input_data)[0]

    # Display the predicted revenue
    st.header("Predicted Monthly Revenue:")
    st.write(f"{predicted_revenue:.2f}")

