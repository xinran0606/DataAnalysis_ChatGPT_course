import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("GPR_distribution_2025-10-17_13-56-19_Kurz(1).csv")

print(df.columns)

group_counts = df.groupby('Gruppe').size().reset_index(name="MitgAnzahl")
group_counts = group_counts.sort_values(by='Gruppe', ascending=True)

print(group_counts.to_string(index=False))

# --------------pie graph with matplotlib---------------------
plt.figure(figsize=(8,8))
plt.pie(
    group_counts['MitgAnzahl'],
    labels=group_counts['Gruppe'],
    autopct='%1.1f%%',
    startangle=90,
    counterclock=False
)
plt.title('Anzahl jeder Gruppe')
# plt.show()

# --------------interagierte pie graph with plotly--------------
def get_student_info(gr):
    sub_df = df[df['Gruppe'] == gr].sort_values('Vorname')
    return "<br>".join(
        sub_df['Vorname'] + " " +
        sub_df['Name'] + " (" +
        sub_df['HRZ-Login'] + ")"
    )

group_counts['students'] = group_counts['Gruppe'].apply(get_student_info)

fig = px.pie(
    group_counts, # Plotly Express 的核心规则是：第一参数 = 数据表（DataFrame）
    values='MitgAnzahl',
    names='Gruppe',
    hover_data=['students'],
    category_orders={
        'Gruppe': group_counts['Gruppe'].tolist()
    },
    title='Mitglieder jeder Gruppe'
)
fig.show()