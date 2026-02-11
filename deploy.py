import streamlit as st
import pandas as pd
import numpy as np
import joblib
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title='Student Performance Predictor',
    page_icon='🎓',
    initial_sidebar_state='collapsed'
)


@st.cache_resource
def load_all():
    try:
        model = joblib.load("model.pkl")   
        ordinal_encoder = joblib.load("ordinal_encoder.pkl")
        scaler = joblib.load("scaler.pkl")        
        return model, ordinal_encoder, scaler
    except FileNotFoundError:
        st.error("Model files not found. Ensure the following exist:")
        st.error("- model.pkl")
        st.error("- ordinal_encoder.pkl")
        st.error("- scaler.pkl")
        return None, None, None

model, ordinal_encoder, scaler = load_all()


ordinal_cols = [
    'Parental_Involvement', 'Access_to_Resources', 'Motivation_Level',
    'Family_Income', 'Teacher_Quality', 'Distance_from_Home',
    'Parental_Education_Level', 'Peer_Influence'
]

binary_cols = [
    'Extracurricular_Activities', 'Internet_Access',
    'Learning_Disabilities', 'School_Type'
]

numerical_cols = ['Study_Hours', 'Tutoring_Sessions', 'Previous_Scores','Attendence','Physical_Activity','Sleep_Hours']  # مثال على numerical

binary_map = {
    'No': 0, 'Yes': 1,
    'Public': 0, 'Private': 1,
}


with st.sidebar:
    choose = option_menu(
        None,
        ["Home", "Graphs", "Model Info"],
        icons=['house', 'graph-up', 'info-circle'],
        menu_icon="app-indicator",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#4CAF50", "color": "white"}
        }
    )


if choose == 'Home':
    st.title('🎓 Student Performance Predictor')
    st.markdown("---")
    st.subheader('Enter student details to predict Exam Score')
    
    col1, col2 = st.columns(2)
    
    with col1:
        parental_involvement = st.selectbox('Parental Involvement', ['Low','Medium','High'])
        access_to_resources = st.selectbox('Access to Resources', ['Low','Medium','High'])
        motivation_level = st.selectbox('Motivation Level', ['Low','Medium','High'])
        family_income = st.selectbox('Family Income', ['Low','Medium','High'])
        teacher_quality = st.selectbox('Teacher Quality', ['Low','Medium','High'])
        distance_from_home = st.selectbox('Distance from Home', ['Near','Moderate','Far'])
    
    with col2:
        parental_education = st.selectbox('Parental Education Level', ['High School','College','Postgraduate'])
        peer_influence = st.selectbox('Peer Influence', ['Negative','Neutral','Positive'])
        extracurricular = st.selectbox('Extracurricular Activities', ['No','Yes'])
        internet_access = st.selectbox('Internet Access', ['No','Yes'])
        learning_disabilities = st.selectbox('Learning Disabilities', ['No','Yes'])
        school_type = st.selectbox('School Type', ['Public','Private'])

    
    st.markdown("### Numerical Features")
    col3, col4 = st.columns(2)
    with col3:
        study_hours = st.number_input('Study Hours per week', min_value=0, max_value=100, value=10)
        tutoring_sessions = st.number_input('Tutoring Sessions per week', min_value=0, max_value=10, value=2)
        Attendance  = st.number_input("Attendence" , min_value=0 , max_value=100,value=5)
    with col4:
        Sleep_Hours = st.number_input("Sleep Hours" , min_value=0 , max_value=100,value=5)
        Previous_Scores = st.number_input('Previous Scores', min_value=0, max_value=100, value=5)
        Physical_Activity = st.number_input('Physical Activity', min_value=0, max_value=20, value=5)

    
    st.markdown("---")
    
    if st.button('🎯 Predict Exam Score', type='primary', use_container_width=True):
        if model is not None:

            new_student = pd.DataFrame([{
            'Hours_Studied': study_hours,
            'Attendance': Attendance,
            'Parental_Involvement': parental_involvement,
            'Access_to_Resources': access_to_resources,
            'Extracurricular_Activities': extracurricular,
            'Sleep_Hours': Sleep_Hours,
            'Previous_Scores': Previous_Scores,
            'Motivation_Level': motivation_level,
            'Internet_Access': internet_access,
            'Tutoring_Sessions': tutoring_sessions,
            'Family_Income': family_income,
            'Teacher_Quality': teacher_quality,
            'School_Type': school_type,
            'Peer_Influence': peer_influence,
            'Physical_Activity': Physical_Activity,
            'Learning_Disabilities': learning_disabilities,
            'Parental_Education_Level': parental_education,
            'Distance_from_Home': distance_from_home
        }])

            new_student = new_student[scaler.feature_names_in_]

            # Encoding
            new_student[ordinal_cols] = ordinal_encoder.transform(new_student[ordinal_cols])
            for col in binary_cols:
                new_student[col] = new_student[col].map(binary_map)
            
            # Scaling
            if scaler is not None:
                new_student_scaled = scaler.transform(new_student)
            else:
                new_student_scaled = new_student.values
            
            # Prediction
            result = model.predict(new_student_scaled)
            st.subheader("Predicted Exam Score")
            st.success(f"🎉 {result[0]:.0f}")

# Graphs Page
elif choose == "Graphs":
    st.title('📊 Visualizations')
    st.markdown("---")
    
    viz_files = [
    # Heatmap
    "heatmap.png",
    
    # Boxplots
    "Exam_Score_boxplot.png",
    "Hours_Studied_boxplot.png",
    "Tutoring_Sessions_boxplot.png",
    
    # Histograms
    "Exam_Score_histogram.png",
    "Hours_Studied_histogram.png",
    "Tutoring_Sessions_histogram.png",
    
    # Pie Charts (categorical data)
    "Pie_chart_Parental_Involvement.png",
    "Pie_chart_Parental_Education_Level.png",
    "Pie_chart_Teacher_Quality.png",
    "Pie_chart_School_Type.png",
    "Pie_chart_Extracurricular_Activities.png",
    "Pie_chart_Internet_Access.png",
    "Pie_chart_Motivation_Level.png",
    "Pie_chart_Peer_Influence.png"
    ]

    
    for viz_file in viz_files:
        try:
            st.image(viz_file, caption=viz_file.replace('.png','').replace('_',' '))
        except:
            st.warning(f"Visualization file '{viz_file}' not found")


elif choose == "Model Info":
    st.title('🤖 Model Information')
    st.markdown("---")
    
    if model is not None:
        st.success("✅ Model loaded successfully!")
        st.info(f"**Model Type**: Linear Regression")
        
        st.info("**Features Used:**")
        for col in ordinal_cols + binary_cols + numerical_cols:
            st.write(f"• {col}")
        
        st.info("**Preprocessing:**")
        st.write("• Ordinal encoding for categorical features")
        st.write("• Binary mapping for Yes/No, Male/Female, Public/Private")
        st.write("• Scaling using StandardScaler")
        
        st.markdown("---")
        st.subheader("Performance Metrics")
        st.metric("Train R²", "0.7274")
        st.metric("Test R²", "0.7040")
        st.metric("Train RMSE", "2.0207")
        st.metric("Test RMSE", "2.1991")
    
    else:
        st.error("❌ Model not loaded")

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🎓 Student Performance Predictor | Built with Streamlit | Based on studentPerformanceFactors Dataset</p>
</div>
""", unsafe_allow_html=True)
