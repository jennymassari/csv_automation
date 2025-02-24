import csv

with open("advertising.csv", "r") as file:
    csv_file = csv.reader(file, delimiter=",")
    print(csv_file)
    for i, line in enumerate(csv_file):
        if i == 0:
            print("Attributes: " + str(line))
        else:
            print("Values: " + str(line))
        # print(i, line)