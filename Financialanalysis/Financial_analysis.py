#First run module to import financial data csv file
import csv

#Opening and returning csv file data for analysis
def read_budget_data():
    data = []
    with open('budget_data.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

#testing the funcion above to check for errors
budget_data = read_budget_data()
print(budget_data)

