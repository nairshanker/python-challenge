# Import the necessary modules
import os
import csv


# Specify the csv file path with aa relative reference
csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize values 
month_count = 0
net_p_and_l = 0
net_delta_p_and_l = []
greatest_increase = ["",0]
greatest_decrease = ["",10E10]

# Read the csv file with the improved method using csv reader.
# csv reader method is an iterator. It creates a marker to iterate through the rows and also csv reader creates a list of rows.
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        print(csvreader)

# Accessing the header row 
        csv_header = next(csvreader)

# Skip the header since we are trying to count the number of months in the actual data 
        first_row = next(csvreader)
        month_count += 1
        net_p_and_l += int(first_row[1])

# Initialize the first row            
        previous_row = int(first_row[1])


# csv module has the row option and allows one to iterate row by row
        for row in csvreader:
                month_count = month_count + 1
                net_p_and_l += int(row[1])

                delta_p_and_l = int(row[1])-previous_row
                previous_row = int(row[1])
                net_delta_p_and_l += [delta_p_and_l]
        
        if delta_p_and_l > greatest_increase[1]:
                
        
average = round(sum(net_delta_p_and_l)/len(net_delta_p_and_l),2)

                      

print("Financial Analysis\n")
print("------------------------\n")
print(f"Total Months: {month_count}\n")
print(f"Total: {net_p_and_l}\n")
print(f"Average  Change: ${average}\n")


