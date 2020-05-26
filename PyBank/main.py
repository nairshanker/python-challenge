import os
import csv


# Read the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read the csv file 
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        print(csvreader)

        csv_header = next(csvreader)
        print(f"CSV Header: {csv_header}")

        row_count = 0
        for row in csvreader:
                row_count = row_count + 1
                # print(row)
        print("Financial Analysis")
        print("----------------------------")
        print(f"Total Months: {row_count}")

