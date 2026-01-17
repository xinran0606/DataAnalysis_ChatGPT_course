import duckdb
import pandas as pd

df = pd.read_csv("StudentsPerformance.xls")
con = duckdb.connect()
con.register('students', df)

result = con.execute("""
SELECT 
    AVG("math score") AS avg_math,
    AVG("reading score") AS avg_reading,
    AVG("writing score") AS avg_writing
FROM students
""").fetchdf()

print(result)