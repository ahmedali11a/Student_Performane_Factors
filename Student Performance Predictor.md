# Student Performance Predictor

## Description

This project is an interactive web application built using Streamlit, designed to predict student exam performance based on a variety of influencing factors. The application utilizes a pre-trained machine learning model (Linear Regression) to provide accurate predictions and offers a user-friendly interface for inputting student data and viewing results.

## Features

*   **Interactive User Interface:** Built with Streamlit for a seamless user experience.
*   **Student Performance Prediction:** Predicts exam scores based on multiple factors.
*   **Comprehensive Influencing Factors:** Considers factors such as Parental Involvement, Access to Resources, Motivation Level, Family Income, Teacher Quality, Distance from Home, Parental Education Level, Peer Influence, Extracurricular Activities, Internet Access, Learning Disabilities, School Type, Study Hours, Tutoring Sessions, Previous Scores, Attendance, Physical Activity, and Sleep Hours.
*   **Graphical Visualizations:** Displays a collection of graphs (heatmaps, box plots, histograms, pie charts) to visualize data and relationships between different factors.
*   **Model Information:** Provides details about the model used, including its type, features utilized, preprocessing steps (ordinal encoding, binary mapping, scaling), and performance metrics (R² and RMSE for training and testing).

## Installation

To run this application locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository_link>
    cd <repository_name>
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    # venv\Scripts\activate  # For Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (Ensure `requirements.txt` contains `streamlit`, `pandas`, `numpy`, `joblib`, `streamlit-option-menu`)

4.  **Place model files:**
    Ensure the following files are present in the project's root directory:
    *   `model.pkl` (Trained model)
    *   `ordinal_encoder.pkl` (Ordinal encoder)
    *   `scaler.pkl` (Scaler)

5.  **Place visualization files:**
    Ensure image files for visualizations (e.g., `heatmap.png`, `Exam_Score_boxplot.png`, etc.) are present in the project's root directory.

## Usage

To run the application, execute the following command in your terminal from the project's root directory:

```bash
streamlit run app.py
```

The application will open in your default web browser. You can then interact with the user interface to input student data and get exam score predictions.

## Model Information

The application uses a Linear Regression model for prediction. The features used in the model include:

*   **Ordinal Features:** Parental_Involvement, Access_to_Resources, Motivation_Level, Family_Income, Teacher_Quality, Distance_from_Home, Parental_Education_Level, Peer_Influence.
*   **Binary Features:** Extracurricular_Activities, Internet_Access, Learning_Disabilities, School_Type.
*   **Numerical Features:** Study_Hours, Tutoring_Sessions, Previous_Scores, Attendance, Physical_Activity, Sleep_Hours.

**Preprocessing:**
*   Ordinal encoding for categorical features.
*   Binary mapping for binary features (e.g., No/Yes to 0/1).
*   Data scaling using StandardScaler.

**Performance Metrics:**
*   Train R²: 0.7274
*   Test R²: 0.7040
*   Train RMSE: 2.0207
*   Test RMSE: 2.1991

## Visualizations

The "Graphs" section of the application displays a variety of visualizations to help better understand the data. These visualizations include:

*   **Heatmaps:** To illustrate relationships between variables.
*   **Box Plots:** To represent the data distribution for variables such as Exam Score, Hours Studied, and Tutoring Sessions.
*   **Histograms:** To show the frequency of values for variables like Exam Score, Hours Studied, and Tutoring Sessions.
*   **Pie Charts:** To illustrate the distribution of categories for categorical variables such as Parental Involvement, Parental Education Level, Teacher Quality, School Type, Extracurricular Activities, Internet Access, Motivation Level, and Peer Influence.

## Contributing

Contributions to this project are welcome. Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

*   Special thanks to the Streamlit developers for providing an excellent framework for web applications.
*   This project is based on the `studentPerformanceFactors` dataset.
