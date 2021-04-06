# This is for Python Challenge: PyBanks Homework 
# Using a the data set given in the Resources folder I am to calculate each of the following:

# Importing the modules 
import os
import csv

#setting up the path for the file
csvpath = os.path.join('Pybanks','Resources', 'budget_data.csv')

with open(csvpath) as data:
    csvreader = csv.DictReader(data, delimiter=',')
    budget_data = list(csvreader) # we have inputed the list of information from csv file as a list in the budget_data
    # print(budget_data)
    month_year = [dates['Date'] for dates in budget_data]
    
    # Total number of months of data: 
    total_months = len(budget_data)     
    # print(f' Total Months: {total_months}')

    #The net total amount of "Profit/Losses" over the entire period
    profit_losses = [float(values['Profit/Losses']) for values in budget_data] # this extracts the values from the dictionary for profit/losses
    net_total = sum(profit_losses)
   # print(f' Total: ${net_total}')

    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    change =[]
    for i in range(1, total_months):
        change.append((int(profit_losses[i]-profit_losses[i-1])))
    
    average_change = sum(change)/len(change)    # total change divided by the length of change
   # print(f'Average Change for the Period: ${average_change}')

    #The greatest increase in profits (date and amount) over the entire period

    greatest_profit = max(change)
    great_loca = change.index(greatest_profit)
    #print(f'The greatest increase in profits: month_year[great_loca] ${greatest_profit}')

    #The greatest decrease in losses (date and amount) over the entire period
     
    greatest_loss = min(change)
    loss_loca = change.index(greatest_loss)
    #print(f' The greatest loss in profits: month_year[loss_loca] ${greatest_loss}')

    
    summar_file = open('pybanksummary.txt', 'w')
    summar_file.write(" Financial Analysis \n" )
    summar_file.write("..................................\n")
    summar_file.write(f'Total Months: {total_months} \n Total: ${net_total} \n Average Change for the Period: ${average_change} \n The greatest increase in profits: month_year[great_loca] ${greatest_profit} \n The greatest loss in profits: month_year[loss_loca] ${greatest_loss} \n' )

    summar_file.close()