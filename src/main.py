import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib
import numpy as np

# 1. Initialize FastAPI
app = FastAPI(title="Gold Price AI")

# 2. Setup Templates
templates = Jinja2Templates(directory="templates")

# 3. Load Model
model = joblib.load('gold_price_model.pkl')
scaler = joblib.load('scaler.pkl')

# 4. Input Schema
class GoldInput(BaseModel):
    Open: float
    High: float
    Low: float
    Volume: float
    SMA_15: float
    SMA_30: float
    Prev_Close: float

# --- ROUTES ---

# 5. Home Route (Returns the HTML UI)
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 6. Prediction API (Used by the HTML form via JavaScript)
@app.post("/predict")
def predict_price(data: GoldInput):
    features = [
        data.Open, data.High, data.Low, data.Volume,
        data.SMA_15, data.SMA_30, data.Prev_Close
    ]
    features_array = np.array(features).reshape(1, -1)
    scaled_features = scaler.transform(features_array)
    prediction = model.predict(scaled_features)
    
    return {"predicted_price": round(float(prediction[0]), 2)}

# Run
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)