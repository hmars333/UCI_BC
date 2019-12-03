import os
import csv


file= os.path.join("budget_data.csv")
Output_file= os.path.join("Analysis", "final_analysis.txt")

#Analysis Questions
total_months= 0
change_month= []
net_changes=[]
avg_change= []
greatest_increase= [" ", 0]
greatest_loss= [" ", 9999999999999999999999]
total_net= 0

#read csv
with open(file) as csvfile:
    csv_file = csv.reader(csvfile)
    header= next(csv_file)

    row_1= next(csv_file)
    total_months= total_months + 1
    total_net= total_net+ int(row_1[1])
    past_net= int(row_1[1])
    
#find total months, net total
    for row in csv_file:
        total_months= total_months +1
        total_net= total_net + int(row[1])
#average change
    avg_change= int(row[1])- past_net
    past_net= int(row[1])
    net_changes= net_changes + [avg_change]
    change_month= change_month + [row[0]]
#greatest Increase
    if avg_change > greatest_increase[1]:
        greatest_increase[0]= row[0]
        greatest_increase[1]= avg_change
#greatest Loss
    if avg_change < greatest_loss[1]:
        greatest_loss[0]= row[0]
        greatest_loss[1]= avg_change

monthly_avg= sum(net_changes) / len(net_changes)
output_text=(
        f"Budget_Analysis"
        f"Total Months: ${total_months}"
        f"Total ${total_net}"
        f"Average Change: ${monthly_avg}"
        f" Greatest Profit Increase: {greatest_increase[0]} (${greatest_increase[1]})"
        f"Greatest Profit Loss: {greatest_loss[0]} (${greatest_loss[1]})"
    )

print(output_text)
with open(output_text, "w") as txt_file:
        txt_file.write(output_text)







