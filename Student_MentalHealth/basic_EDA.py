import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Student_Mental_Health_Academic_Pressure_2025.csv - Form Responses 1.csv")
print(df.columns)

print("-------------------------------------------------------------")
# Average academic pressure by age group
academic_Pressure = df.groupby('Age Group')['  How much academic pressure do you feel?  '].mean().reset_index(name="average pressure")
print(academic_Pressure.to_string(index=False))

plt.figure(figsize=(8,5))
bars = plt.bar(
    academic_Pressure['Age Group'],
    academic_Pressure['average pressure'],
    color='skyblue'
)
plt.ylabel('Average Pressure')
plt.xlabel('Age Group')
plt.xticks(rotation=0)
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, # x Koordinant
             height + 0.02, # y Koordinant
             f'{height}',
             ha='center', va='bottom')
plt.tight_layout()
#plt.show()

print("--------------------------------------------------------------")
# Pressure differences between College and University students
kategories = df.groupby('  Current Education Level  ')['  How much academic pressure do you feel?  '].mean().reset_index(name="average pressure")
print(kategories.to_string(index=False))

print("--------------------------------------------------------------")
# Relationship between sleep hours and academic pressure
sleep_pressure = df.groupby('  How many hours do you sleep on average per night?  ')['  How much academic pressure do you feel?  '].mean().reset_index(name='average preasure')
print(sleep_pressure.to_string(index=False))