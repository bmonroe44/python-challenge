import os
import csv

# Set path to collect data from the resource folder
poll_data = os.path.join('Resources', 'election_data.csv')

# Create lists to store data and variables
total_votes = 0
Candidates = []
vote_per = 0
candidate_votes = 0



# Read the csv file 
with open(poll_data, newline="") as csvfile:
    # Create csv reader object
    election_results = csv.reader(csvfile, delimiter=",")

    # Find the header, create variables for total votes
    csv_header = next(election_results)
    first_row = next(election_results)
    total_votes = total_votes + 1
    candidate_votes = candidate_votes + 1
    khan_votes = 0

    

    # Loop through data
    for row in election_results:

        #Get list of candidates that received votes
       

        #Get the total number of votes (row count)
        total_votes = total_votes + 1

        # Find the total votes per candidate
        if str(row[2]) == "Khan":
            khan_votes = khan_votes + 1

        
print("Election Results")
print("----------------------------")
print("Total Votes: " + str(total_votes))
print("----------------------------")
