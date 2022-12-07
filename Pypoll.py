# the data we need to retrieve
# 1. The total number of votes cast
# 2. comolete list of camdidates who received votes
# 3. the percentage of votes each candidate von
# 4.the total number of votes each candidate won
# 5.the winner of the election based on popular vote

import os
import csv

file_to_load = os.path.join("resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.csv")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
