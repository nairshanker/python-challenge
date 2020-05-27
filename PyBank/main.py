# Import the necessary modules
import os
import csv


# Specify the csv file path with aa relative reference
csvpath = os.path.join('Resources', 'budget_data.csv')

# Read the csv file with the improved method using csv reader.
# csv reader method is an iterator. It creates a marker to iterate through the rows and also csv reader creates a list of rows.

with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        print(csvreader)

# Skip the header since we are trying to count the number of months in the actual data 
        csv_header = next(csvreader)

# Initialize row counter adn net_Profile/Loss to zero
        row_count = 0
        net_p_and_l = 0
        # net_p_and_l = []
        delta_p_and_l = 0
        sigma_delta_p_and_l = 0
        # average_change = []


# csv module has the row option and allows one to iterate row by row
        for row in csvreader:
                row_count = row_count + 1
                # net_p_and_l.append(row[1])
                net_p_and_l += int(row[1])
                delta_p_and_l = int(row[1])-delta_p_and_l
                # sigma_delta_p_and_l += delta_p_and_l
                
        # Calculating the average change on P/L after the rows and net P/l have been counted separately
        # Average_change = delta_p_and_l/(row_count-1)
        # total = sum(int(net_p_and_l))


        print("Financial Analysis\n")
        print("----------------------------\n")
        print(f"Total Months: {row_count}\n")
        print(f"Total: ${net_p_and_l}\n")
        print(f"{delta_p_and_l}")
        # print(f"Total: ${str(total)}")
        # print(net_p_and_l)

        
        # print(f"Average Change: ${delta_p_and_l}")

