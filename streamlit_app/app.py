# streamlit_app/app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import yaml
from pathlib import Path
import logging

# Configure page
st.set_page_config(
    page_title="Diabetes Prediction MLOps App",
    page_icon="🩺",
    layout="wide"
)

# Load configuration
def load_config():
    config_path = Path(__file__).parent.parent / "params.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

config = load_config()

# Load model
@st.cache_resource
def load_model():
    try:
        model = joblib.load("models/diabetes_model.pkl")
        return model
    except FileNotFoundError:
        st.error("Model not found! Please train the model first by running the training pipeline.")
        return None

model = load_model()

# Main app
def main():
    st.title("🩺 Diabetes Prediction MLOps Application")
    st.markdown("---")

    # Sidebar
    with st.sidebar:
        st.header("ℹ️ About")
        st.markdown("""
        This is a professional MLOps application for predicting diabetes risk
        based on health metrics using machine learning.

        **Features:**
        - Real-time predictions
        - Model performance tracking with MLflow
        - Professional MLOps architecture
        """)

        st.header("🔧 Model Info")
        if model:
            st.success("✅ Model loaded successfully")
        else:
            st.error("❌ Model not available")

    # Main content
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("📊 Enter Health Metrics")

        # Input fields
        pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
        glucose = st.number_input("Glucose Level", min_value=0.0, max_value=300.0, value=120.0)
        blood_pressure = st.number_input("Blood Pressure", min_value=0.0, max_value=200.0, value=70.0)
        bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
        age = st.number_input("Age", min_value=1, max_value=120, value=30)

        # Prediction button
        if st.button("🔮 Predict Diabetes Risk", type="primary"):
            if model is None:
                st.error("Model not available. Please train the model first.")
            else:
                # Prepare input data
                input_data = np.array([[pregnancies, glucose, blood_pressure, bmi, age]])

                # Make prediction
                prediction, probability = model.predict(input_data)[0], model.predict_proba(input_data)[0][1]

                # Display results
                with col2:
                    st.header("🎯 Prediction Results")

                    if prediction == 1:
                        st.error("⚠️ High Risk: Diabetic")
                        st.metric("Confidence", f"{probability:.1%}")
                    else:
                        st.success("✅ Low Risk: Not Diabetic")
                        st.metric("Confidence", f"{(1-probability):.1%}")

                    # Additional info
                    st.markdown("---")
                    st.markdown("**Input Summary:**")
                    input_df = pd.DataFrame({
                        'Metric': ['Pregnancies', 'Glucose', 'Blood Pressure', 'BMI', 'Age'],
                        'Value': [pregnancies, glucose, blood_pressure, bmi, age]
                    })
                    st.table(input_df)

    # Footer
    st.markdown("---")
    st.markdown("*Built with ❤️ using Streamlit and MLOps best practices*")

if __name__ == "__main__":
    main()