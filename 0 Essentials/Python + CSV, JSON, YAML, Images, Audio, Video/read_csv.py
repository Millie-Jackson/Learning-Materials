import csv

with open("Salaries.csv", newline="") as f:
    reader = csv.reader(f)
    my_data = list(reader)

print(my_data[0:4])