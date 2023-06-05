#grab os to read csv file
import os
import csv

#define path to csv
csvpath = os.path.join("Resources", "election_data.csv")

#initialize variables
total_votes = 0
candidate_votes = {}

#open and read csv file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header row
    header = next(csvreader)

    #process each row in the Csv file
    for row in csvreader:

        #incriment the number of total votes
        total_votes += 1

        #get the candidate name from the row
        candidate_name = row[2]

        #create if statement to add candidate name if it is not already in our dictionary
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0

        #incriment vote counts for candidates
        candidate_votes[candidate_name] += 1

#determine winner
winner = max(candidate_votes, key=candidate_votes.get)

#generate analysis report
analysis_report = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)

for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    analysis_report += f"{candidate}: {percentage:.3f}% ({votes})\n"

analysis_report += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

#print report to the terminal
print(analysis_report)

#save report to the analysis directory
output_path = os.path.join("analysis", "election_analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.write(analysis_report)