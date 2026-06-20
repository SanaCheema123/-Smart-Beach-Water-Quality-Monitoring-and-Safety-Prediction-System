# 🌊 Smart Beach Water Quality Monitoring and Safety Prediction System
[screen-capture.webm](https://github.com/user-attachments/assets/b0f0a1a0-5852-479a-8aa3-8d04bcb636e5)

## Overview

The **Smart Beach Water Quality Monitoring and Safety Prediction System** is an AI-powered environmental analytics platform designed to assess and predict beach water quality conditions using machine learning techniques. The system analyzes environmental and water quality parameters to classify beach conditions into safety categories and provide recommendations for public health and recreational activities.

The project combines data preprocessing, machine learning, environmental analytics, interactive visualizations, and a modern Streamlit dashboard to support data-driven coastal management and beach safety monitoring.

---

## Project Objectives

* Monitor and analyze beach water quality conditions.
* Predict water safety status using machine learning models.
* Identify environmental factors affecting water quality.
* Generate safety recommendations for beach visitors.
* Provide interactive analytics and reporting dashboards.
* Support environmental monitoring and coastal management decisions.

---

## Dataset

**Dataset Source**

Beach Water Quality Dataset (Kaggle)

The dataset contains various environmental and water quality measurements including:

* Beach Name
* Water Temperature
* Air Temperature
* Turbidity
* Wave Height
* Rainfall
* pH Level
* Dissolved Oxygen
* Conductivity
* Bacteria Count

### Target Variable

Water Quality Status:

* Safe
* Moderate Risk
* Unsafe

---

## Machine Learning Pipeline

```text
Beach Water Quality Dataset
            ↓
Data Cleaning
            ↓
Missing Value Handling
            ↓
Feature Engineering
            ↓
Target Creation
            ↓
Train-Test Split
            ↓
Model Training
            ↓
Model Evaluation
            ↓
Best Model Selection
            ↓
Prediction Engine
            ↓
Interactive Dashboard
            ↓
Reports & Analytics
```

---

## Models Implemented

### Decision Tree Classifier

A simple and interpretable classification model used as a baseline.

### Random Forest Classifier

An ensemble learning algorithm that improves prediction accuracy through multiple decision trees.

### XGBoost Classifier

A gradient boosting model used for high-performance classification and comparison.

---

## Dashboard Features

### Dashboard

* Total Records
* Safe Water Days
* Moderate Risk Days
* Unsafe Days
* Best Model Accuracy
* Water Quality Distribution
* Dataset Preview

### Water Quality Prediction

Users can enter:

* Beach Name
* Water Temperature
* Air Temperature
* Turbidity
* Wave Height
* Rainfall
* pH
* Dissolved Oxygen
* Conductivity
* Bacteria Count

Outputs:

* Water Quality Status
* Confidence Score
* Safety Recommendation

### Beach Analytics

* Beach-wise Risk Analysis
* Turbidity Distribution
* Water Quality Trends
* Environmental Statistics

### Environmental Insights

* Correlation Heatmap
* Bacteria vs Turbidity Analysis
* Environmental Factor Relationships
* Pollution Indicators

### ML Analytics

* Model Comparison
* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

### Reports

* Processed Dataset Export
* Safety Summary Report
* Model Evaluation Report
* CSV Downloads

---

## Project Structure

```text
beach_water_quality_ai_project/
│
├── app/
├── data/
├── docs/
├── models/
├── notebooks/
├── outputs/
├── src/
├── tests/
│
├── requirements.txt
├── README.md
├── run_app.bat
└── setup_project.bat
```

---

## Technology Stack

### Programming Language

* Python

### Machine Learning

* Scikit-Learn
* XGBoost

### Data Processing

* Pandas
* NumPy

### Data Visualization

* Plotly

### Dashboard Development

* Streamlit

### Model Persistence

* Joblib

---

## Installation

### Step 1: Clone Repository

```bash
git clone <repository-url>
cd beach_water_quality_ai_project
```

### Step 2: Install Dependencies

```bash
py -m pip install -r requirements.txt
```

### Step 3: Generate Sample Dataset

```bash
py src/generate_sample_data.py
```

### Step 4: Train Models

```bash
py src/train_model.py
```

### Step 5: Launch Dashboard

```bash
py -m streamlit run app/app.py
```

---

## Expected Outputs

After training, the following files are generated:

### Models

```text
models/
├── best_water_quality_model.pkl
├── random_forest_model.pkl
├── decision_tree_model.pkl
├── xgboost_model.pkl
├── label_encoder.pkl
└── feature_columns.pkl
```

### Evaluation Results

```text
outputs/
├── model_comparison.csv
├── confusion_matrix.csv
├── classification_report.txt
└── water_quality_summary.csv
```

---

## Applications

* Beach Safety Monitoring
* Environmental Management
* Coastal Zone Planning
* Water Pollution Assessment
* Public Health Protection
* Recreational Water Quality Analysis
* Smart Environmental Decision Support Systems

---

## Future Enhancements

* Real-time IoT Sensor Integration
* GIS-Based Beach Mapping
* Satellite Data Integration
* Mobile Application Support
* Automated Alert System
* Cloud Deployment
* Deep Learning Models
* Real-Time Environmental Monitoring

---

## Author

Developed as an educational AI and environmental analytics project demonstrating:

* Machine Learning
* Environmental Data Science
* Interactive Dashboard Development
* Coastal Analytics
* Predictive Modeling
* Water Quality Monitoring

---

## License

This project is intended for educational, research, and portfolio purposes.
