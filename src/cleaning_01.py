
import pandas as pd
import numpy as np
import sys

def check_required_columns(df: pd.DataFrame):
    required_columns = [
        'Student_ID', 'First_Name', 'Last_Name', 'Email', 'Gender', 'Age',
        'Department', 'Attendance (%)', 'Midterm_Score', 'Final_Score',
        'Assignments_Avg', 'Quizzes_Avg', 'Participation_Score',
        'Projects_Score', 'Total_Score', 'Grade', 'Study_Hours_per_Week',
        'Extracurricular_Activities', 'Internet_Access_at_Home',
        'Parent_Education_Level', 'Family_Income_Level', 'Stress_Level (1-10)',
        'Sleep_Hours_per_Night'
    ]

    missing = [col for col in required_columns if col not in df.columns]
    
    if missing:
        print("❌ Missing required columns:", missing)
        sys.exit("Execution stopped due to missing columns.")
    else:
        print("✅ All required columns are present.")

def get_missing_percentage(df):
    missing_percentage = (df.isnull().sum() / len(df)) * 100
    missing_percentage = missing_percentage[missing_percentage > 0]

    if missing_percentage.empty:
        print("✅ No missing values found.")
    else:
        print("📊 Percentage of missing values:")
    
    return missing_percentage