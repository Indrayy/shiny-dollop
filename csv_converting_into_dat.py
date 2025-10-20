import csv

# Read CSV and write to DAT file with UTF-8 encoding
with open(r"F:\terrabox download\TMDB_movie_dataset_v11.csv", "r", encoding="utf-8") as csv_file, open("tmdb_movie_dataset.dat", "w", encoding="utf-8") as dat_file:
    reader = csv.reader(csv_file)
    for row in reader:
        dat_file.write(" | ".join(row) + "\n")  # Formatting the output
