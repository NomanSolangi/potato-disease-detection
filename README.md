# Potato Plant Disease Detection

Detect potato plant diseases using deep learning!  
Upload images of potato leaves and classify them as **healthy**, **early blight**, or **late blight**.

---

## 📂 Project Structure

```
potato_plant_decease/
│-- api/                # FastAPI backend for model inference
│-- frontend/           # React frontend for user interaction
│-- plantvillage/       # Dataset folders (not included in repo)
│-- saved_models/       # Trained model files (.keras, .h5)
│-- served_models/      # Model directories for API serving
│-- README.md           # Project documentation
│-- Requirements.txt    # Python dependencies for backend
│-- training.ipynb      # Model training notebook
```

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```sh
git clone https://github.com/yourusername/potato_plant_decease.git
cd potato_plant_decease
```

### 2️⃣ Backend Setup (API)

```sh
cd api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r Requirements.txt
uvicorn main:app --reload
```

### 3️⃣ Frontend Setup

```sh
cd frontend
npm install
npm start
```

---

## 🖼️ Usage

1. Start the backend API server.
2. Start the frontend React app.
3. Open [http://localhost:3000](http://localhost:3000) in your browser.
4. Upload a potato leaf image to get disease prediction.

---

## 🧠 Model Information

- Trained on [PlantVillage](https://www.plantvillage.org/) dataset.
- Classes: **Healthy**, **Early Blight**, **Late Blight**
- Model files: [saved_models/](saved_models/) and [served_models/](served_models/)

---

## 🔌 API Endpoints

- `POST /predict`  
  Upload an image and receive prediction.

See [api/main.py](api/main.py) for implementation.

---

## 🖥️ Frontend

- Built with React.
- See [frontend/src/App.js](frontend/src/App.js) for main logic.

---

## 📊 Training

- Model training notebook: [training.ipynb](training.ipynb)
- Update model weights in [saved_models/](saved_models/)

---

## 🤝 Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/foo`)
3. Commit your changes
4. Push to the branch (`git push origin feature/foo`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Contact

For questions, open an issue or contact [your.email@example.com](mailto:your.email@example.com)