import os
import csv

# define the path to the CSV file:
csv_file = os.path.join("Resources", "election_data.csv")

# initialize variables:
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# read the CSV file:
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)

    # skip the header row:
    next(csv_reader)

    for row in csv_reader:
        # extract data from the current row:
        candidate_name = row[2]

        # count the total votes:
        total_votes += 1

        # update the candidate's vote count:
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1

# determine the winner:
for candidate, votes in candidates.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# calculate the percentage of votes for each candidate:
results = []
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")

# format the analysis results:
linebreak = "\n"
analysis_results = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
{linebreak.join(results)}
-------------------------
Winner: {winner}
-------------------------
"""

# print the analysis to the terminal:
print(analysis_results)

# define the path for the output text file:
output_file = os.path.join("analysis", "election_analysis.txt")

# write the analysis results to the text file:
with open(output_file, 'w') as file:
    file.write(analysis_results)
