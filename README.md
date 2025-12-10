#  Stroke Risk Prediction System

A Machine Learning–powered system that predicts the likelihood of stroke based on clinical, demographic, and lifestyle factors.

This project includes:

* ✔️ A trained **Random Forest ML model**
* ✔️ **FastAPI backend** for predictions
* ✔️ **Streamlit frontend** for user interaction
* ✔️ Full end-to-end deployment (Render API + Streamlit App)

---

## 🚀 Features

### 🔹 Machine Learning

* Preprocessed dataset with 22 medical & lifestyle features
* Encoded categorical values using saved encoders
* Random Forest classifier
* Model exported using **joblib**

### 🔹 Backend (FastAPI)

* `/` → Health check
* `/predict` → Accepts patient data and returns:

  * `prediction` (0 = low risk, 1 = high risk)
  * `probability` (stroke likelihood)

### 🔹 Frontend (Streamlit)

* User-friendly medical input form
* Sends data to deployed API
* Displays prediction with probability score
* Fully responsive UI

---

# 📦 Installation (Run Locally)

### **Clone the repository**

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

---

## ⚙️ Backend Setup (FastAPI)

### **1. Install dependencies**

```bash
pip install -r requirements.txt
```

### **2. Start the API**

```bash
uvicorn app:app --reload
```

### **3. API will run at**

```
http://127.0.0.1:8000
```

### **4. Test the API**

Open your browser or use Postman:

```
GET http://127.0.0.1:8000/
```

**Example predict request:**

```json
POST http://127.0.0.1:8000/predict
Content-Type: application/json

{
  "age": 56,
  "gender": "Male",
  "heart_disease": 0,
  "marital_status": "Married",
  "work_type": "Private",
  "residence_type": "Urban",
  "avg_glucose_level": 134.5,
  "bmi": 28.7,
  "smoking_status": "smokes",
  "alcohol_intake": "Yes",
  "physical_activity": "Yes",
  "stroke_history": 0,
  "family_history_stroke": "No",
  "dietary_habits": "Yes",
  "stress_levels": 5.5,
  "symptoms": 0,
  "systolic_bp": 140,
  "diastolic_bp": 90,
  "hdl": 45,
  "ldl": 120,
  "stroke_score": 80.2
}
```

---

# 🖥️ Frontend Setup (Streamlit)

### **1. Run Streamlit app**

```bash
streamlit run s_app.py
```

### **2. The UI will open automatically at**

```
http://localhost:8501
```

### **3. Using the UI**

* Fill in all required medical/lifestyle fields
* Click **Predict Stroke Risk**
* The system sends data to the API and displays:

  * 🟢 **Low Stroke Risk**
  * ⚠️ **High Stroke Risk**


## **Frontend Deployment (Streamlit Cloud)**

1. Create a new Streamlit app
2. Select repository + `s_app.py`
3. Set environment variable:

```
API_URL = "https://stroke-prediction-api-aksd.onrender.com/predict"
```

4. Deploy → App goes live.

---


# 🧑‍💻 File Structure

```
.
├── s_app.py              # Streamlit frontend
├── stroke_rf_model.pkl   # Trained ML model
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```

---

# 🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first.

---

# ⭐ Support

If you found this project helpful, please give it a **star ⭐ on GitHub**!


