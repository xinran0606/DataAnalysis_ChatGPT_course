import duckdb
import pandas as pd

df = pd.read_csv('StudentsPerformance.xls')

con = duckdb.connect()
con.register('students', df)

result = con.execute("""
    SELECT *
    FROM students
    LIMIT 5
""").fetchdf()

print(result)
