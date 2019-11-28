import os
import csv


file= os.path.join("budget_data.csv")

#Total Months in Data, empty lists
Date= []
PnL= []

#read csv
with open(file, 'r') as csvfile:
    csv_file = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        Date.append(row[0])
        PnL.append(int(row[1]))

#find total months
total= len(Date)
total

#The net total amount of "Profit/Losses"
P_L= len(PnL)
P_L
#The average of the changes in "Profit/Losses"
def average(PnL):
    length = len(PnL)
    total = 0.0
    for P in PnL:
        total += PnL
    return total / length







