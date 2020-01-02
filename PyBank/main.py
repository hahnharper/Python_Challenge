import os
import csv


budget_data = os.path.join("Python_Challenge", "Resources", "budget_data.csv")

with open(budget_data, newline ="") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f'Header: {csv_header}')

# Track financial parameters

total_month=0
total_net_revenue=0
month_of_change=[]
greatest_increase=["",0]
greatest_decrease=["",0]

#Find total months in csv
puppies = {}
for row in csvreader:
    mon, val = row
    puppies[mon] = int(val)
print(puppies)