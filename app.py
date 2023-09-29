import streamlit as st
import joblib
import pandas as pd 


# Load the trained model
model_filename = "assignment04_model.pkl"
model_and_metrics = joblib.load(model_filename)

# Extract the model and metrics
model = model_and_metrics['model']
mae = model_and_metrics['mae']
mse = model_and_metrics['mse']
r2 = model_and_metrics['r2']

# Create a Streamlit app
st.title("Regression Model App")
st.sidebar.header('User Input')

# Input fields for user to enter feature values
hours_studied = st.sidebar.slider('Hours Studied', 0, 10, 5)
previous_scores = st.sidebar.slider('Previous Scores', 0, 100, 50)
sleep_hours = st.sidebar.slider('Sleep Hours', 0, 12, 6)

# Predict target performance
if st.sidebar.button("Predict"):
    features = {
        "Hours Studied": hours_studied,
        "Previous Scores": previous_scores,
        "Sleep Hours": sleep_hours
    }
    input_data = pd.DataFrame(features, index=[0])
    prediction = model.predict(input_data)
    st.write('### Prediction')
    st.write(f"Predicted Target Performance: {prediction[0]:.2f}")

    st.write(f'Mean Absolute Error: {mae}')
    st.write(f'Mean Squared Error: {mse}')
    st.write(f'R-squared (R^2): {r2}')