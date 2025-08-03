
from fastapi import FastAPI
import joblib
import pandas as pd

# Load the trained model from Google Drive
model = joblib.load('/content/drive/MyDrive/linear_regression_model.pkl')

# Initialize the FastAPI app
app = FastAPI()

# Create a route to make predictions
@app.post("/predict")
def predict_life_expectancy(data: dict):
    # Convert the input data to a Pandas DataFrame
    input_df = pd.DataFrame([data])
    
    # Make a prediction using the loaded model
    prediction = model.predict(input_df)

    # Return the prediction
    return {"predicted_life_expectancy": prediction.tolist()}
