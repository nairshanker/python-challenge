import os
import csv

# Read the csv file
csvpath = os.path.join(Resources", "budget_data.csv")

# Read the csv
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)