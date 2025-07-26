import pandas as pd
from io import StringIO

# Simulated CSV data (like reading a small file)
data = """name,age,department,salary
Alice,30,HR,60000
Bob,35,Engineering,85000
Charlie,25,Sales,50000
David,45,Engineering,95000
Eva,29,HR,62000
Frank,33,Sales,52000
"""

# Load the data into a DataFrame
df = pd.read_csv(StringIO(data))

# Show the full DataFrame
print("Full DataFrame:")
print(df)

# Filter: salary > 60000
print("\nEmployees with salary > 60000:")
print(df[df["salary"] > 60000])

# Group by department and average salary
print("\nAverage salary by department:")
print(df.groupby("department")["salary"].mean())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# %%
