import os
import csv

# Set path to collect data from the resource folder
financial_data = os.path.join('Resources', 'budget_data.csv')

# Create lists to store data and variables
AvgChg = []
greatest_inc = ["", 0]
greatest_dec = ["", 9999999999999]
total_months = 0
net_profit = 0
prev_net = 0

# Read the csv file 
with open(financial_data, newline="") as csvfile:
    # Create csv reader object
    finance = csv.reader(csvfile, delimiter=",")
    
    # Find the header, create variables for total months, net_profit and previous net
    csv_header = next(finance)
    first_row = next(finance)
    total_months = total_months + 1
    net_profit = net_profit + int(first_row[1])
    prev_net = int(first_row[1])
    
    # Loop through data
    for row in finance:
     
        # Get the total total months
        total_months = total_months + 1

        # Calculate net profit
        net_profit = int(row[1]) + net_profit
        
        # Calculate net change
        net_change = int(row[1]) - prev_net
        
        # Redefining previous net to current row
        prev_net = int(row[1])
        
        # Add more values to average change
        AvgChg = AvgChg + [net_change] 

        #Calculate the average change
        avg_change = round(sum(AvgChg) / (total_months - 1), 2)

        # Find greatest increase in profits
        if net_change > greatest_inc[1]:
            greatest_inc[0] = row[0]
            greatest_inc[1] = net_change
            
        # Find the greatest decrease in profits
        if net_change < greatest_dec[1]:
            greatest_dec[0] = row[0]
            greatest_dec[1] = net_change

       
print("Financial Analysis")
print("-----------------------------")
print("Total Months: " +  str(total_months))
print("Total: $" + str(net_profit))
print("Average Change: $" + str(avg_change))
print("Greatest Increase in Profits: " + str(greatest_inc[0]) + " " + str(greatest_inc[1]))
print("Greatest Decrease in Profits: " + str(greatest_dec[0]) + " " + str(greatest_dec[1]))

# Set path to write data
financial_analysis = os.path.join('Resources', 'New_Text_Document.txt')