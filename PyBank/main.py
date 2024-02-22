# import csv file
import os
import csv

datacsv = os.path.join("csv", "budget_data.csv")

# lists to store data
month = []
profits = []

# turn csv file into lists
with open(datacsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read header row as headers
    csvheader = next(csvreader) 

    for row in csvreader:
        month.append(row[0])
        profits.append(int(row[1]))
        
    # count no of months/entries
    entries = len(month)

    # calculate net profit
    net = 0
    
    for monthprofit in profits:
        net += int(monthprofit)
    
    
# csv file into other list
with open(datacsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read header row as headers
    csvheader = next(csvreader) 
    #first row as row after header
    first_row = next(csvreader)    

    # calculate average change in profit
    # calculate individual changes
    # loop compare two entries and add value to list
    # new list for change in profit amounts
    listchange = []
    oldprofit = int(first_row[1])

    for row in csvreader:
        month.append(row[0])
        profits.append(int(row[1]))
        
        # change = month2 - month1
        monthchange = int(row[1]) - oldprofit
        oldprofit = int(row[1])
        
        listchange.append(monthchange)
        
    
    # average change from list
    averagechange = sum(listchange)/len(listchange)

    # calculate greatest increase
    # largest +ve change and equivalent month
    # find list max, place in list, and month in that place
    greatincrease = max(listchange)
    placemax = listchange.index(greatincrease)
    increasemonth = month[placemax + 1]
    
    # calculate greatest decrease
    # largest -ve change and equivalent month
    # reverse increase
    greatdecrease = min(listchange)
    placemin = listchange.index(greatdecrease)
    decreasemonth = month[placemin + 1]
    
# print final info - total months, net profit, average change in profit, greatest increase, greatest decrease (month and amount)

    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {entries}")
    print(f"Total: ${net}")
    print(f"Average Change: ${round(averagechange,2)}")
    print(f"Greatest Increase in Profits: {increasemonth} (${greatincrease})")
    print(f"Greatest Decrease in Profits: {decreasemonth} (${greatdecrease})")


# import text file
analysistxt = 'analysis/analysis.txt'

# write results to file
with open(analysistxt, "w") as txtfile:
    txtfile.write("Financial Analysis"
                  '\n' "------------------------"
                  '\n' f"Total Months: {entries}"
                  '\n' f"Total: ${net}"
                  '\n' f"Average Change: ${round(averagechange,2)}"
                  '\n' f"Greatest Increase in Profits: {increasemonth} (${greatincrease})"
                  '\n' f"Greatest Decrease in Profits: {decreasemonth} (${greatdecrease})")
    