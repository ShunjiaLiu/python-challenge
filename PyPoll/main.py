import csv

# Initialize variables
total_votes = 0
candidates = {}  # Dictionary 

file_path = './Resources/election_data.csv'
with open(file_path,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)
    
    # Loop 
    for row in csvreader:
      
        candidate_name = row[2]

        # Update total votes
        total_votes += 1

        # Update candidate vote counts in the dictionary
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Determine the winner based on the popular vote
winner = max(candidates, key=candidates.get)


print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")


for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results 
with open('election_results.txt', 'w') as result_file:
    result_file.write("Election Results\n")
    result_file.write("-------------------------\n")
    result_file.write(f"Total Votes: {total_votes}\n")
    result_file.write("-------------------------\n")
    
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        result_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

    result_file.write("-------------------------\n")
    result_file.write(f"Winner: {winner}\n")
    result_file.write("-------------------------\n")
