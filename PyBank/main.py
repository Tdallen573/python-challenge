#Import program to grab and read csv file
import os
import csv

#create path to csv file
csvpath =  os.path.join("Resources", "budget_data.csv")

#Initialize Variables
total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
dates = []

#read the csv file
try:
    with open(csvpath, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        #skip the Header
        header = next(csvreader)

        # Iterate through each row in the CSV file
        for row in csvreader:
            #incriment the total number of months
            total_months += 1

            #Extract the profit/loss values from the row and set date
            date = row[0]
            profit_loss = int(row[1])

            #Add the value of the profit/loss to the net total
            net_total += profit_loss

            #Calculate the change from previous row
            change = profit_loss - previous_profit_loss

            #store changes and dates in their lists
            changes.append(change)
            dates.append(date)

            #update the previous profit/loss value for the next iteration
            previous_profit_loss = profit_loss

        #calculate average change
        average_change = sum(changes) / len(changes)

    #begin printing analysis in the terminal
    print("Financial Analysis")

    #add break
    print("------------------------------")

    #print Months
    print(f"Total Months: {total_months}")

    #print net total
    print(f"Net Total: ${net_total}")

    #print average change
    print(f"Average Change: ${average_change:.2f}")

    #Calculate the greatest increase and decrease
    greatest_increase = max(changes)
    greatest_decrease = min(changes)

    #Find the corresponding dates for those changes
    greatest_increase_date = dates[changes.index(greatest_increase)]
    greatest_decrease_date = dates[changes.index(greatest_decrease)]

    #Print greatest increase and decrease
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

    #create path for text file
    output_path = os.path.join("analysis", "financial_analysis.txt")

    #open the output file and write a text file
    with open(output_path, 'w') as txtfile:
        #write the results to a text file
        txtfile.write("Financial Analysis\n")
        txtfile.write("------------------------------\n")
        txtfile.write(f"Total Months: {total_months}\n")
        txtfile.write(f"Total: ${net_total}\n")
        txtfile.write(f"Average Change: ${average_change:.2f}\n")
        txtfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
        txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

    #print a message indicating completion of analysis
    print("Financial anlysis has been completed and saved to the analysis directory.")

        
#Function to know if error reading CSV file ever occurs
except Exception as e:
    print(f"Error reading CSV file: {e}")

