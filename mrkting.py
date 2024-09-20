import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load the trained model
# Replace 'rf_model.pkl' with the actual filename of your saved model
with open('rf_model.pkl', 'rb') as f:
    rf_model = pickle.load(f)

# Create a title for your app
st.title("Marketing Campaign Response Prediction")

# Create input fields for the features
st.header("Enter Customer Data:")

# Assuming your features are named accordingly, replace with actual feature names
# Create input fields for the features
# Example:
# age = st.number_input("Age", min_value=18, max_value=100, value=30)
# income = st.number_input("Income", min_value=0, value=50000)

# Get the feature names from your training data
feature_names = X_train.columns.tolist()

user_inputs = {}
for feature_name in feature_names:
    if df[feature_name].dtype == 'object':
        unique_values = df[feature_name].unique().tolist()
        user_inputs[feature_name] = st.selectbox(feature_name, unique_values)
    else:
        user_inputs[feature_name] = st.number_input(feature_name)

# Create a button to make predictions
if st.button("Predict Response"):
    # Create a DataFrame from the user inputs
    input_df = pd.DataFrame([user_inputs])

    # Make predictions using the loaded model
    prediction = rf_model.predict(input_df)[0]

    # Display the prediction
    if prediction == 1:
        st.success("The model predicts that the customer will respond to the campaign.")
    else:
        st.warning("The model predicts that the customer will not respond to the campaign.")

# Optional: Add a section to explain the model
st.markdown("---")
st.header("About the Model")
st.write("This model is trained using a Random Forest Classifier to predict customer response to a marketing campaign.")

# Save the trained model
# with open('rf_model.pkl', 'wb') as f:
#     pickle.dump(rf_model, f)
