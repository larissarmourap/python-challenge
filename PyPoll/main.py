import os
import csv

csvpath = os.path.join('C:\\', 'Users', 'laris', 'Documents', 'Github', 'python-challenge', 'PyPoll', 'Resources', 'election_data.csv')

total_votes = 0 
Charles_votes = 0
Diana_votes = 0
Raymon_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    next(csvreader, None)     

    for row in csvreader: 
        total_votes +=1

        if row[2] == "Charles": 
            Charles_votes +=1
        elif row[2] == "Diana":
            Diana_votes +=1
        elif row[2] == "Raymom": 
            Raymon_votes +=1

    candidates = ["Charles", "Diana", "Raymom"]
    votes = [Charles_votes, Diana_votes, Raymon_votes]

dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

Charles_percent = ((Charles_votes / total_votes) * 100)
Diana_percent = ((Diana_votes / total_votes) * 100)
Raymon_percent = ((Raymon_votes / total_votes) * 100)

print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles: {Charles_percent:.3f%} ({Charles_votes})")
print(f"Diana: {Diana_percent:.3f%} ({Diana_votes})")
print(f"Raymom: {Raymon_percent:.3f%} ({Raymon_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

output_file = os.path.join('C:\\', 'Users', 'laris', 'Documents', 'try', 'election_data.csv')

with open(output_file,"w") as file:

    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Charles: {Charles_percent:.3f%} ({Charles_votes})")
    file.write("\n")
    file.write(f"Diana: {Diana_percent:.3f%} ({Diana_votes})")
    file.write("\n")
    file.write(f"Raymom: {Raymon_percent:.3f%} ({Raymon_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")
