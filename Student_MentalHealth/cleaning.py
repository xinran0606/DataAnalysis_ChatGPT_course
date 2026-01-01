import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Student_Mental_Health_Academic_Pressure_2025.csv - Form Responses 1.csv")

df.columns = df.columns.str.strip().str.lower()

# print(df.columns)

df = df.rename(columns={
    'timestamp': 'timestamp',
    'age group': 'age_group',
    'gender': 'gender',
    'current education level': 'education_level',
    'how much academic pressure do you feel?': 'academic_pressure',
    'how often do you feel stressed due to studies?': 'stress_frequency',
    'how many hours do you sleep on average per night?': 'sleep.hours',
    'what is the main cause of your academic stress?': 'stress_cause'
})

# print(df.columns)

df['stress_cause'] = df['stress_cause'].str.strip().str.lower()

def normalize_stress_cause(text):
    if 'exam' in text:
        return 'Exams'
    elif 'financ' in text:
        return 'Financial'
    elif 'understand' in text or 'difficulty' in text:
        return 'Academic difficulty'
    elif 'expectations' in text:
        return 'Expectations'
    else:
        return 'Other'

df['stress_cause_clean'] = df['stress_cause'].apply(normalize_stress_cause)

# print(df['stress_cause_clean'])

# Do people who experience exam pressuire feel more academic pressure than those who experience financial pressure?
