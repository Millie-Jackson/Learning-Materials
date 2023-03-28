import csv

my_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

with open("my_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["a", "b", "c"])
    writer.writerows(my_data)