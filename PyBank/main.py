import csv

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0

profit_loss_changes = []

greatest_increase = ["", 0]   # for [date, change]
greatest_decrease = ["", 0]   # for [date, change]


# Define the path
with open('./Resources/budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
# Define the value of the header 
    header = next(csvreader)
    
# Loop through the data in the row   
    for row in csvreader:
       
        date = row[0]
        profit_loss = int(row[1])
        
# Update the value of the total months and net total
        total_months = total_months + 1  
        net_total = net_total + profit_loss

# Update the change         
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)

          
            if change > greatest_increase[1]:
                greatest_increase[0] = date
                greatest_increase[1] = change
                
            if change < greatest_decrease[1]:
                greatest_decrease[0] = date
                greatest_decrease[1] = change
        
# Update the previous profit loss  
        previous_profit_loss = profit_loss

# Caculate the average change
average_change = sum(profit_loss_changes) / (total_months - 1)


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
