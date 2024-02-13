import os
import csv

csvpath = os.path.join('C:\\', 'Users', 'laris', 'Documents', 'Github', 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')
total_months = []
total_profit = []
monthly_profit_change = []
 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    next(csvreader, None)  

    for row in csvreader: 
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
max_incr_value = max(monthly_profit_change)
max_decr_value = min(monthly_profit_change)

max_incr_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decr_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_incr_month]} (${(str(max_incr_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decr_month]} (${(str(max_decr_value))})")

output_file = os.path.join('C:\\', 'Users', 'laris', 'Documents', 'Github', 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

with open(output_file,"w") as file:
     
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_incr_month]} (${(str(max_incr_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decr_month]} (${(str(max_decr_value))})")
