from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

from sklearn.linear_model import LinearRegression
import joblib


# Creating FastAPI instance
app = FastAPI()

# Creating class to define the request body
# and the type hints of each attribute


class studentData(BaseModel):
    hours_studied: float
    previous_score: float
    extracurricular_activities: int
    sleep_Hours: float
    sample_question_practiced: float


filepath = "regression_model.joblib"
# Creating and loading model
model = joblib.load(filepath)


@app.post('/predict')
def predict(data: studentData):
    # Making the data in a form suitable for prediction
    test_data = [[
        data.hours_studied,
        data.previous_score,
        data.extracurricular_activities,
        data.sleep_Hours,
        data.sample_question_practiced
    ]]

    # Predicting the Class
    prediction = model.predict(test_data)

    # Return the Result
    return {'prediction:', max(min(prediction[0], 100), 0)}
