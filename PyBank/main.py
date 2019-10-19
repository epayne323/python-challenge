import os
import csv

# best way to get number of rows of csv?
# sum(1 for row in budgetReader)
# or
# len(file1.readlines())

# should these be inputs?
budgetPath = os.path.join('..','budget_data.csv')
resultsPath = os.path.join('..','budget_data_results.csv')

with open(budgetPath, 'r', newline = '') as file1:
    
    budgetReader = csv.reader(file1, delimiter = ',')
    # totalMonths = len(list(budgetReader)) # why
    budgetHeader = next(budgetReader)

    # initializing isn't strictly necessary in Python (I think), but it's still helpful to know beforehand 
    # what type of data to expect for each variable
    nMonths = 0
    netProfit = 0

    cProfit = 0
    pProfit = 0
    # profitChanges = [None]*totalMonths
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
        # is it worse to append, or to pre-allocate?
        profitChanges.append(cProfit-pProfit)
        # profitChanges[nMonths-1] = cProfit - pProfit
        
        
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