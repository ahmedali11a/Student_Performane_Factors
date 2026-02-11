# 🎓 Student Performance Predictor

A Streamlit web application that predicts a student's **Exam Score** based on academic, social, and lifestyle factors using a trained **Machine Learning (Linear Regression) model**.

The app allows users to:
- Enter student information through an interactive UI
- Apply the same preprocessing used during training (encoding + scaling)
- Get a predicted exam score instantly
- View dataset visualizations
- See model details and performance metrics

---

## 🚀 Features

- 🧠 **Machine Learning prediction** using a trained Linear Regression model  
- 🎛️ **Interactive user interface** built with Streamlit  
- 🧹 **Automatic preprocessing**:  
  - Ordinal encoding for ordered categorical features  
  - Binary mapping for Yes/No and Public/Private features  
  - Feature scaling using `StandardScaler`  
- 📊 **Visualization gallery** (heatmaps, histograms, boxplots, pie charts)  
- ℹ️ **Model information page** with performance metrics  

---

## 🧪 Model Details

- **Model Type:** Linear Regression  
- **Target:** Exam Score  

### Features Used

**Ordinal features:**
- Parental_Involvement  
- Access_to_Resources  
- Motivation_Level  
- Family_Income  
- Teacher_Quality  
- Distance_from_Home  
- Parental_Education_Level  
- Peer_Influence  

**Binary features:**
- Extracurricular_Activities  
- Internet_Access  
- Learning_Disabilities  
- School_Type  

**Numerical features:**
- Study_Hours  
- Tutoring_Sessions  
- Previous_Scores  
- Attendance  
- Physical_Activity  
- Sleep_Hours  

### Preprocessing

- Ordinal encoding for ordered categorical features  
- Binary mapping (Yes/No, Public/Private)  
- Scaling using `StandardScaler`  

### Performance Metrics

- **Train R²:** 0.7274  
- **Test R²:** 0.7040  
- **Train RMSE:** 2.0207  
- **Test RMSE:** 2.1991  

---

## 📦 Requirements (Dependencies)

This project uses the following Python packages:

- `streamlit`  
- `pandas`  
- `numpy`  
- `scikit-learn`  
- `joblib`  
- `streamlit-option-menu`  
- `matplotlib`  
- `seaborn`  

You can install them all using:

```bash
pip install streamlit pandas numpy scikit-learn joblib streamlit-option-menu matplotlib seaborn
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

Install dependencies (see **Requirements** section above), then make sure the following files exist in the project folder:

- `model.pkl`  
- `ordinal_encoder.pkl`  
- `scaler.pkl`  

---

## ▶️ Run the App

From the project root (where `deploy.py` is located), run:

```bash
streamlit run deploy.py
```

Then open the provided local URL in your browser (e.g. `http://localhost:8501`).

---

## 🖥️ App Pages

### 🏠 Home

- Enter student details (categorical and numerical features).  
- Click **“Predict Exam Score”**.  
- Get the predicted score instantly.  

### 📊 Graphs

View dataset visualizations, including:

- Heatmap  
- Boxplots  
- Histograms  
- Pie charts for categorical features  

### 🤖 Model Info

- View model type.  
- See the full list of features used.  
- Check preprocessing steps.  
- Review performance metrics.  

---

## 📚 Dataset

This project is based on the **Student Performance Factors** dataset, which includes academic, family, and lifestyle attributes to predict student exam performance.  

The dataset (`StudentPerformanceFactors.csv`) contains factors such as:

- Parental involvement and education level  
- Access to resources and internet  
- Motivation level and peer influence  
- Study hours, tutoring, attendance, sleep hours, physical activity  
- School type and family income  

These features are transformed and fed into the regression model to predict the **Exam Score**.
