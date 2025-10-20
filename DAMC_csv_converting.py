import pandas as pd

# Path to your XLS file
xls_path = r"G:\ebook\Certificate & Skill\Revo U - DAMC\Study Case 7-18 april 2025\DAMC_pivot.xlsx"
# Path for the output CSV file
csv_path = "damc_google_data.csv"  # Replace with your desired CSV file name

# Read the Excel file
df = pd.read_excel(xls_path)

# Save as CSV
df.to_csv(csv_path, index=False)
print(f"Converted {xls_path} to {csv_path} successfully!")
