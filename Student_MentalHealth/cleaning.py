import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from Student_MentalHealth.basic_EDA import sleep_pressure

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
    'how many hours do you sleep on average per night?': 'sleep_hours',
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
    elif 'expectations' in text or 'parents' in text:
        return 'Expectations'
    else:
        return 'Other'

df['stress_cause_clean'] = df['stress_cause'].apply(normalize_stress_cause)

# Average pressure group by stress cause
avg_pressure_cause = df.groupby('stress_cause_clean')['academic_pressure'].mean().sort_values(ascending=False)
print(avg_pressure_cause)

plt.figure(figsize=(8,5))
sns.barplot(x=avg_pressure_cause.index, y=avg_pressure_cause.values, palette='pastel')
plt.ylabel('Average Academic Pressure')
plt.xlabel('Main Stress Cause')
plt.title('Average Acadimic Pressure by Stress Cause')
plt.xticks(rotation=30)
#plt.show()

# Group the number of people of different genders in each source of stress.
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
stacked = df.groupby(['stress_cause_clean', 'gender']).size().unstack(fill_value=0)
print(stacked)
stacked.plot(kind='bar', stacked=False, figsize=(10,6), color=['skyblue','lightcoral'])
plt.ylabel('Number of students')
plt.xlabel('Main Stress cause')
plt.xticks(rotation=30)
plt.legend(title='Gender')
plt.title("Number of Students by Stress Cause and Gender")
plt.tight_layout()
#plt.show()

# Group the number of people of different ages in each source of stress.
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
ageStacked = df.groupby(['stress_cause_clean', 'age_group']).size().unstack(fill_value=0)
print(ageStacked)
ageStacked.plot(kind='bar', stacked=False, figsize=(16,6), color=['salmon','orange','olivedrab','lightseagreen','hotpink'])
plt.ylabel('Number of students')
plt.xlabel('Main Stress cause')
plt.xticks(rotation=30)
plt.legend(title='age_group')
plt.title("Number of Students by Stress Cause and ages")
plt.tight_layout()
#plt.show()

# The relaitonship between stress level and sleep hours.
print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-")

def normalize_sleep_hours(x):
    x = x.strip()
    if '–' in x:
        start, end = x.split('–')
        return (float(start) + float(end)) / 2
    elif 'More than' in x:
        return float(x.split()[-1]) + 1
    else:
        return float(x)

df['sleepHours_clean'] = df['sleep_hours'].apply(normalize_sleep_hours)

sleep_pressure = df.groupby('sleepHours_clean')['academic_pressure'].mean().sort_values(ascending=False).reset_index()
print(sleep_pressure)

plt.figure(figsize=(8,6))
plt.bar(
    sleep_pressure['sleepHours_clean'],
    sleep_pressure['academic_pressure'],
    color='orange'
)
plt.ylabel("Average pressure value")
plt.xlabel("Sleep hours")
plt.xticks(rotation=30)
plt.title("The relaitonship between stress level and sleep hours.")
plt.tight_layout()
plt.show()