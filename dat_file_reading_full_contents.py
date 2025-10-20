import csv

with open("tmdb_movie_dataset.dat", "r", encoding="utf-8") as dat_file:
    for line in dat_file:
        print(line.strip())  # Print each line without extra spaces
