import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")
output_analysis = os.path.join("Analysis", "budget_analysis.txt")

# Track financial parameters

total_month= 0
previous_revenue_value = 0
total_net_revenue= 0
total_revenue_profit = 0
month_of_change=[]
revenue_change_list = []
greatest_increase=["",0]
greatest_decrease=["",9999999999999]

with open(budget_data, newline ="") as csvfile:
    
    csvreader = csv.DictReader(csvfile)

    #Find total months in csv
    for row in csvreader:
        total_month += 1
        total_net_revenue = total_net_revenue + int(row["Profit/Losses"])
        
        #Revenue Change
        revenue_change = int(row["Profit/Losses"]) - previous_revenue_value
        previous_revenue_value = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        #Greatest Increase (max)
        if revenue_change > greatest_increase[1]:
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        #Greatest Decrease (min)
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change
revenue_change_list.pop(0)
average_revenue = sum(revenue_change_list)/len(revenue_change_list)


output = (
    f"\nFinancial Analysis\n"
    f"---------------------\n"
    f"Total Months: {total_month}\n"
    f"Total: ${total_revenue_profit:,.2f}\n"
    f"Average Change: $ {average_revenue:,.2f}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} ${greatest_increase[1]:,.2f})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} ${greatest_decrease[1]:,.2f})\n"

)

print(output)
with open(output_analysis, "w") as txt_file:
    txt_file.write(output)
