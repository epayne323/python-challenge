import os
import csv

# the instructions state:

# Your scripts should work for each dataset provided. Run your script for each dataset separately 
# to make sure that the code works for different data.

# However, there are only two csv files for this assignment, and they are formatted differently.
# to make this applicable to different csvs with the same format, I would use inputs:

# filename = input("Please enter name of csv file: ")
# filepath = os.path.join('..',filename)
budgetPath = os.path.join('..','budget_data.csv')
resultsPath = os.path.join('..','budget_data_results.csv')

with open(budgetPath, 'r', newline = '') as file1:
    
    budgetReader = csv.reader(file1, delimiter = ',')
    budgetHeader = next(budgetReader)

    # initializing isn't strictly necessary in Python (I think), but it's still helpful to know beforehand 
    # what type of data to expect for each variable
    nMonths = 0
    netProfit = 0

    cProfit = 0
    pProfit = 0
    profitChanges = []

    maxIncrease = 0
    maxIncreaseDate = ""
    maxDecrease = 0
    maxDecreaseDate = ""
    
    for row in budgetReader:
        nMonths += 1

        # store current row's profit in a variable so we don't need to cast it each time
        cProfit = int(row[1])
        netProfit += cProfit

        # the first element of this list will be equal to the first profit.
        # I've heard it's better to preallocate a list with its expected length, rather than appending in
        # every update, but I couldn't figure out how to ge the number of lines in the csv file without 
        # advancing through it
        profitChanges.append(cProfit-pProfit)
        
        # finding maximum and minimum profits, and their dates
        if cProfit > maxIncrease:
            maxIncreaseDate = row[0]
            maxIncrease = cProfit
        elif cProfit < maxDecrease:
            maxDecreaseDate = row[0]
            maxDecrease = cProfit
        
        # set previous profit to be used in tracking profit changes
        pProfit = cProfit

    # This is asking for the for the average of CHANGES of profit day-to-day, NOT the average of the total 
    # sum of profits/losses. The first element won't be included in the calculation.
    avgProfitChanges = sum(profitChanges[1:])/(nMonths-1)

    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {nMonths}")
    print(f"Total: {netProfit}")
    print(f"Average Change: {avgProfitChanges}")
    print(f"Greatest Increase in Profits: {maxIncreaseDate} {maxIncrease}")
    print(f"Greatest Decrease in Profits: {maxDecreaseDate} {maxDecrease}")

with open(resultsPath, 'w', newline = '') as file2:
    budgetWriter = csv.writer(file2)
    budgetWriter.writerow(["Financial Analysis"])
    budgetWriter.writerow(["------------------"])
    budgetWriter.writerow([f"Total: {nMonths}"])
    budgetWriter.writerow([f"Total: {netProfit}"])
    budgetWriter.writerow([f"Average Change: {avgProfitChanges}"])
    budgetWriter.writerow([f"Greatest Increase in Profits: {maxIncreaseDate} {maxIncrease}"])
    budgetWriter.writerow([f"Greatest Decrease in Profits: {maxDecreaseDate} {maxDecrease}"])