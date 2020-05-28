# Import the necessary modules
import os
import csv


# Specify the csv file path with aa relative reference
csvpath = os.path.join('Resources', 'election_data.csv')
output_file = os.path.join("", "pypoll_result_summary.txt")

# Initialize values 
voters_count = 0
candidate_list = []

# Read the csv file with the improved method using csv reader.
# csv reader method is an iterator. It creates a marker to iterate through the rows and also csv reader creates a list of rows.
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        print(csvreader)

        # Accessing the header row 
        csv_header = next(csvreader)

# Skip the header since we are trying to count the number of months in the actual data 
        first_row = next(csvreader)
        voters_count += 1

        # Initialize the first row            
        previous_row_candidate = first_row[2]

        # csv module has the row option and allows one to iterate row by row
        for row in csvreader:
                voters_count += 1
                candidate_list = [row[2]]
        
candidate_list_final = set(candidate_list)
print(candidate_list_final)
        # if row[2] != previous_row_candidate:
        #     candidate_list = row[2]
    

print(f"Total Votes: {voters_count}\n")
# print(candidate_list)