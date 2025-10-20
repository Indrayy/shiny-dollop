import json

# Open the Jupyter Notebook file safely
with open(r"G:\Engineering & Design Archives\Computing Engineering\Data Science & Engineering Work\Python Grimoire at work\Wes McKinney-Python for Data Analyst\chap4_numpy_array_1m_integers.ipynb", "r", encoding="utf-8") as file:
    data = json.load(file)  # Load JSON content

# Print structured JSON data
print(json.dumps(data, indent=4))