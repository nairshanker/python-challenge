# Import the necessary modules
import os
import csv

# Specify the csv file path with aa relative reference
csvpath = os.path.join('Resources', 'election_data.csv')
output_file = os.path.join("", "pypoll_result_summary.txt")

# Initialize values 
voters_count = 0
candidate_list = []
unique_candidate_list =[]
votes = {}
percentages = []

# Read the csv file with the improved method using csv reader.
# csv reader method is an iterator. It creates a marker to iterate through the rows and also csv reader creates a list of rows.
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        print(csvreader)

        # Accessing the header row 
        csv_header = next(csvreader)

# Skip the header since we are trying to count the number of voters from the first row
        first_row = next(csvreader)
        voters_count += 1

        # Initialize the first row            
        previous_row_candidate = first_row[1]
      


        # csv module has the row option and allows one to iterate row by row
        for row in csvreader:
                voters_count += 1
                # candidate_name = row[2]
                candidate_list += [row[2]]

        unique_candidate_list = set(candidate_list)  

        for candidate_name in unique_candidate_list:
                votes[name] = 0

        for row in csvreader:
        for candidate_name in unique_candidate_list:
                if row[2] == candidate_name:
                        votes[row[2]]= votes[row[2]]+1    
       
print(f"Total Votes: {voters_count}\n")
# print(candidate_list)
print(unique_candidate_list)


#   khans_votes = []
#         li_votes = []
#         otooley_votes = []
#         correy_votes = []
#  no_of_votes_khan = count(khans_votes)
#  if row[2] == str(Khan)
#                         khans_votes += [row[0]]

# print(f"Khans Votes: {khans_votes}")
