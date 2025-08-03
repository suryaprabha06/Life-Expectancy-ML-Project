# Life-Expectancy-ML-Project

This project is an end-to-end machine learning solution for predicting life expectancy. It utilizes a Linear Regression model trained on a comprehensive dataset. The model is deployed as a RESTful API using FastAPI and is publicly accessible via a secure ngrok tunnel, allowing for real-time predictions.

### Tools and Technologies
* **Python:** The core programming language used for the project.
* **Scikit-learn:** Used for building and training the machine learning model.
* **FastAPI:** The framework used to create the REST API for the model.
* **ngrok:** Used to create a public, live URL for the API.
* **Google Colab:** The environment where the code was developed.

### Project Files
* `Global_Life_Expectancy_Prediction.ipynb`: This is the Jupyter Notebook containing all the code for data analysis, preprocessing, and model training.
* `linear_regression_model.pkl`: The saved machine learning model file.
* `main.py`: The Python script for the FastAPI application that serves the model via an API.

### Live API Demonstration
You can try the live API by visiting the following link. The API's documentation (Swagger UI) allows you to test the `/predict` endpoint with your own data.

**Live URL:** [https://c71e6f5ae83a.ngrok-free.app]
