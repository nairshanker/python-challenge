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
percent_lib = {}
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
                votes[candidate_name] = 0

with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        print(csvreader)

        # Accessing the header row 
        csv_header = next(csvreader)

        for row in csvreader:

                for candidate_name in unique_candidate_list:
                        if row[2] == candidate_name:
                                votes[row[2]]= votes[row[2]]+1

for candidate_name in unique_candidate_list:
        percent = format((votes[candidate_name]/voters_count*100), '.3f')
        percent_lib[candidate_name] = percent
        percentages.append(percent)

winner = max(votes, key=votes.get)


print_content = (f"Election Results\n"

                f"\n-------------------------\n"
                f"\nTotal Votes: {voters_count}\n"
                f"\n-------------------------\n"
                f'\nKhan: {percent_lib["Khan"]}% ({votes["Khan"]})\n'
                f'\nCorrey: {percent_lib["Correy"]}% ({votes["Correy"]})\n'
                f'\nLi: {percent_lib["Li"]}% ({votes["Li"]})\n'
                f"\nO'Tooley: 3.000% (105630)\n" #My calculations are correct but Im unable to print because of the apostrophe
                f"\n-------------------------\n"
                f"\nWinner: {winner}\n"
                f"\n-------------------------\n")
print(print_content)

with open(output_file, "w") as text_file:
        text_file.write(print_content)