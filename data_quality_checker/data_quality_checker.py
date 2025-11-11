import pandas as pd
import json
from datetime import datetime

# === Data Quality Checker ===
# Reads a CSV file, detects missing values, duplicates, and data types,
# then saves a JSON report summarizing the dataset's quality.

# 1 Load your CSV file (make sure it's in the same folder)
file_name = "employees.csv"  # <-- Change this to your file name
df = pd.read_csv(file_name)

# 2 Display basic info
print("=== DATA QUALITY CHECK REPORT ===\n")
print(df.head(), "\n")

# 3 Generate report
report = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "file_name": file_name,
    "rows": len(df),
    "columns": list(df.columns),
    "missing_values": df.isnull().sum().to_dict(),
    "duplicates": int(df.duplicated().sum()),
    "data_types": df.dtypes.astype(str).to_dict()
}

# 4 Save report to JSON file
output_file = "data_quality_report.json"
with open(output_file, "w") as f:
    json.dump(report, f, indent=4)

# 5 Confirm output
print("✅ Report generated successfully!")
print(f"Saved as: {output_file}")
