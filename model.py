import joblib
import numpy as np
from catboost import CatBoostClassifier
import sklearn

model_path = "Model/catboost.joblib"
model = joblib.load(model_path)

def predict(data):
    prediction = model.predict(data)
    return prediction
