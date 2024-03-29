import os
import csv

# the instructions state:

# Your scripts should work for each dataset provided. Run your script for each dataset separately 
# to make sure that the code works for different data.

# However, there are only two csv files for this assignment, and they are formatted differently.
# to make this applicable to different csvs with the same format, I would use inputs:

# filename = input("Please enter name of csv file: ")
# filepath = os.path.join('..',filename)
electionPath = os.path.join('..','election_data.csv')
resultsPath = os.path.join('..','election_data_results.csv')

with open(electionPath, 'r', newline = '') as file1:
    electionReader = csv.reader(file1, delimiter = ',')
    electionHeader = next(electionReader)

    totalVotes = 0
    # store the candidate names as keys in a dictionary, with vote totals as values
    candidateTotals = {}
    
    for row in electionReader:
        totalVotes += 1

        # if the candidate name is already a key in the dictionary, add 1 to their vote total
        if row[2] in candidateTotals:
            candidateTotals[row[2]] += 1
        # otherwise set their vote total to 1
        else:
            candidateTotals[row[2]] = 1
        
print("Election Results")
print("----------------")
print(f"Total Votes: {totalVotes}")
print("----------------")
for key in candidateTotals:
    print(f"{key}: {candidateTotals[key]*100/totalVotes}% ({candidateTotals[key]})")
print("----------------")
# truly, lambdas are the intended solution.
# no really, use the built in max function, setting the key function to look at the values
print("Winner: " + max(candidateTotals, key = lambda x: candidateTotals[x]))
print("----------------")

with open(resultsPath, 'w', newline = '') as file2:
    electionWriter = csv.writer(file2, delimiter = ',')

    electionWriter.writerow(["Election Results"])
    electionWriter.writerow(["----------------"])
    electionWriter.writerow([f"Total Votes: {totalVotes}"])
    electionWriter.writerow(["----------------"])
    for key in candidateTotals:
        electionWriter.writerow([f"{key}: {candidateTotals[key]*100/totalVotes}% ({candidateTotals[key]})"])
    electionWriter.writerow(["----------------"])
    electionWriter.writerow(["Winner: " + max(candidateTotals, key = lambda x: candidateTotals[x])])
    electionWriter.writerow(["----------------"])