import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Table/GPR_distribution_2025-10-17_13-56-19_Kurz(1).csv")

df['von'] = pd.to_datetime(df['von'], format='%H:%M')
df['bis'] = pd.to_datetime(df['bis'], format='%H:%M') # String kann nicht von einander substraieren, aber Typ time geht es.

# Neue Tabelle für Kurse erstellt
courses = (
    df[['Gruppe', 'Tag', 'von', 'bis', 'Raum']].drop_duplicates()
)

# Wie Lange hat diese Gruppe in diesem Tag gedauert.
courses['Dauer'] = (courses['bis'] - courses['von']).dt.total_seconds() / 60

total_duration_per_day = (
    courses.groupby('Tag')['Dauer'].sum().reset_index()
)

order = ['Montag', 'Dienstag', 'Mittwoch']

# 把 Tag 变成有序类别
total_duration_per_day['Tag'] = pd.Categorical(total_duration_per_day['Tag'], # 把 Tag 列转换成 类别型（Categorical）数据
                                               categories=order, # categories=order → 设置类别的顺序
                                               ordered=True # 表示这个顺序是有序的（而不是无序标签）
                                               )
total_duration_per_day = total_duration_per_day.sort_values('Tag')
print(total_duration_per_day)

# -----------------bar graph--------------------------------
plt.figure(figsize=(8,5))
bars = plt.bar(
    total_duration_per_day['Tag'],
    total_duration_per_day['Dauer'],
    color='skyblue'
)
plt.ylabel('Totale Zeitlänge eines Tages')
plt.xlabel('Tage')
plt.title('Vergleich die Unterrichtszeitlänge jeden Tag')
plt.xticks(rotation=0)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, # x Koordinant
             height + 5, # y Koordinant
             f'{int(height)}',
             ha='center', va='bottom')

plt.tight_layout()
plt.show()

