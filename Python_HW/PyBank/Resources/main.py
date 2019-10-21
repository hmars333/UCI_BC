import csv

with open('budget_data.csv', newline='') as csvfile:
    csvreader= csv.reader(csvfile, delimiter=' ')
print (csvreader)

