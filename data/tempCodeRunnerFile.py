import pandas as pd

# Sample data
data = {
    "Name": ["Amit", "Priya", "Rahul"],
    "Score": [85, 90, 78]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("students_scores.xlsx", index=False)

print("Excel file created successfully!")