import os
import csv

# path to the CSV file:
csv_file = os.path.join("Resources", "budget_data.csv")

# initialize variables to store financial data:
total_months = 0
net_total = 0
previous_profit_loss = 0
change_in_profit_loss = []
months = []

# read the CSV file:
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)

    # skip the header row:
    next(csv_reader)

    for row in csv_reader:
        # extract data from the current row:
        date = row[0]
        profit_loss = int(row[1])

        # calculate the change in profit/loss:
        change = profit_loss - previous_profit_loss

        # append the change to the list:
        change_in_profit_loss.append(change)

        # append the month to the list:
        months.append(date)

        # update the previous profit/loss for the next iteration:
        previous_profit_loss = profit_loss

        # calculate the total months and net total:
        total_months += 1
        net_total += profit_loss

# calculate the average change:
average_change = sum(change_in_profit_loss[1:]) / (total_months - 1)

# find the greatest increase and decrease in profits:
greatest_increase = max(change_in_profit_loss)
greatest_decrease = min(change_in_profit_loss)

# get the corresponding months for the greatest increase and decrease:
increase_month = months[change_in_profit_loss.index(greatest_increase)]
decrease_month = months[change_in_profit_loss.index(greatest_decrease)]

# format the analysis results:
analysis_results = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {increase_month} (${greatest_increase})
Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})
"""

# print the analysis to the terminal:
print(analysis_results)

# Create a folder called "analysis" if it doesn't exist
output_folder = "analysis"
os.makedirs(output_folder, exist_ok=True)

# Define the path for the output text file
output_file = os.path.join(output_folder, "financial_analysis.txt")

# write the analysis results to the text file:
with open(output_file, 'w') as file:
    file.write(analysis_results)
