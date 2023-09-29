{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "df16f18b-f321-4644-b5da-d61ea975d6e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import pandas as pd \n",
    "\n",
    "# Load the trained model\n",
    "model_filename = \"assignment04_model.pkl\"\n",
    "pipeline = joblib.load(model_filename)\n",
    "\n",
    "# Create a Streamlit app\n",
    "st.title(\"Regression Model App\")\n",
    "\n",
    "# Sidebar for user input\n",
    "st.sidebar.header(\"User Input\")\n",
    "hours_studied = st.sidebar.slider(\"Hours Studied\", min_value=0, max_value=10)\n",
    "previous_scores = st.sidebar.slider(\"Previous Scores\", min_value=0, max_value=100)\n",
    "sleep_hours = st.sidebar.slider(\"Sleep Hours\", min_value=0, max_value=24)\n",
    "\n",
    "# Predict target performance\n",
    "if st.sidebar.button(\"Predict\"):\n",
    "    features = {\n",
    "        \"Hours Studied\": hours_studied,\n",
    "        \"Previous Scores\": previous_scores,\n",
    "        \"Sleep Hours\": sleep_hours\n",
    "    }\n",
    "    input_data = pd.DataFrame(features, index=[0])\n",
    "    prediction = pipeline.predict(input_data)\n",
    "    st.write(f\"Predicted Target Performance: {prediction[0]:.2f}\")\n",
    "    \n",
    "    st.write(f'Mean Absolute Error: {mae}')\n",
    "    st.write(f'Mean Squared Error: {mse}')\n",
    "    st.write(f'R-squared (R^2): {r2}')\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    # main()\n",
    "    st.run()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
