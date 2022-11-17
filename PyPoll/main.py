import os
import csv

poll_csv = os.path.join('..', 'Instructions', 'PyPoll', 'Resources', 'election_data.csv')

vote_count = 0
stockham_count = 0
degette_count = 0
doane_count = 0

with open(poll_csv, 'r') as poll_data:
    next(poll_data, None)

    csvreader = csv.reader(poll_data, delimiter=',')

    for row in csvreader:
        vote_count += + 1
        stockham_count += row.count("Charles Casper Stockham")
        degette_count += row.count("Diana DeGette")
        doane_count += row.count("Raymon Anthony Doane")

    stockham_percent = (stockham_count / vote_count) * 100
    degette_percent = (degette_count / vote_count) * 100
    doane_percent = (doane_count / vote_count) * 100

    if stockham_count > degette_count and doane_count:
        winner = ("Charles Casper Stockham")
    elif degette_count > stockham_count and doane_count:
        winner = ("Diana DeGette")
    else:
        winner = ("Raymon Anthony Doane")
    
election_results = ("Election Results\n"
"---------------------------\n"
f"Total Votes: {vote_count}\n"
"---------------------------\n"
f"Charles Casper Stockham: {round(stockham_percent, 3)}% ({stockham_count})\n"
f"Diana DeGette: {round(degette_percent, 3)}% ({degette_count})\n"
f"Raymon Anthony Doane: {round(doane_percent, 3)}% ({doane_count})\n"
"---------------------------\n"
f"Winner: {winner}\n"
"---------------------------\n")
print(election_results, end= "")
with open("poll_data.txt", 'w') as txt_file:
    txt_file.write(election_results)