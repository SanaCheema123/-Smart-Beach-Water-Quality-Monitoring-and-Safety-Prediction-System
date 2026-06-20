@echo off
echo Starting OceanAI Beach Water Quality Project...
py src\generate_sample_data.py
py src\train_model.py
py -m streamlit run app\app.py
pause
