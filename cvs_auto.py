import csv

with open("advertising.csv", "r") as file:
    csv_file = csv.reader(file, delimiter=",")
    print(csv_file)
    for line in csv_file:
        print(line)