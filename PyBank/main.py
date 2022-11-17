import os
import csv

bank_csv = os.path.join('..', 'Instructions', 'PyBank', 'Resources', 'budget_data.csv')

profit_loss_total = 0
month_count = 0
net_change_list = []
previous_profit_loss = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

with open(bank_csv, 'r') as budget_data:
    csvreader = csv.reader(budget_data, delimiter=',')
    first_row = next(budget_data, None)
    for row in csvreader:
        if previous_profit_loss == 0:
            previous_profit_loss = float(row[1])
            month_count += 1
            profit_loss_total += float(row[1])
        else:
            month_count += + 1
            profit_loss_total += + float(row[1])
            net_change = float(row[1]) - previous_profit_loss
            net_change_list += [net_change]
            previous_profit_loss = float(row[1])
            if (net_change > greatest_increase):
                greatest_increase = net_change
                greatest_increase_month = row[0]
            if (net_change < greatest_decrease):
                greatest_decrease = net_change
                greatest_decrease_month = row[0] 

avg_change = sum(net_change_list) / len(net_change_list)

financial_analysis = ("Financial Analysis\n"
"------------------------------\n"
f"Total Months: {month_count}\n"
f"Total: ${round(profit_loss_total)}\n"
f"Average Change: ${round(avg_change, 2)}\n"
f"Greatest Increase in Profits: {greatest_increase_month} (${round(greatest_increase)})\n"
f"Greatest Decrease in Profits: {greatest_decrease_month} (${round(greatest_decrease)})\n")
print(financial_analysis, end= "")
with open("bank_data.txt", 'w') as txt_file:
    txt_file.write(financial_analysis)