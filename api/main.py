from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
from keras.models import load_model
import requests

app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

endpoint = "http://localhost:8501/v1/models/potatoes_model:predict"


# MODEL = TFSMLayer("../saved_models/1.keras")  # Load the model from the saved path
# MODEL = load_model("../saved_models/1.keras")
# # If using a different format, adjust the loading method accordingly
CLASS_NAMES = ['Early Blight', 'Late Blight', 'Healthy']

@app.get("/ping")
def ping():
    return {"message": "Hello, My Name is Potato Plant Disease Detection API"}

def read_file_as_image(data) -> np.ndarray:
    image = Image.open(BytesIO(data)).resize((256, 256))  # Resize if required
    return np.array(image)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)
    json_data = {"instances": img_batch.tolist()}
    
    response = requests.post(endpoint, json = json_data)
    prediction = response.json()["predictions"][0]
    
    predicred_class = CLASS_NAMES[np.argmax(prediction)]
    confidence = float(np.max(prediction))
    
    return {
        "class": [predicred_class],
        "confidence": confidence}
    
    
    # predictions = MODEL.predict(img_batch)
    
    # predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    # confidence = float(np.max(predictions[0]))
    # return {
    #     "class": predicted_class,
    #     "confidence": confidence
    # }
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
