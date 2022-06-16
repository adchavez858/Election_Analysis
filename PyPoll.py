# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who recieved votes 
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


import csv
import os
# Assign a variable for the file to load and the path.
election_results = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
election_results = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(election_results) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    headers = next(file_reader)
    print(headers)



# Using the open() function with the "w" mode we will write data to the file.
open(election_results, "w")
outfile = open(election_results, "w")
# Write some data to the file.
outfile.write("Hello World")


# Write three counties to the file.
outfile.write("Arapahoe\nDenver\nJefferson")




# Close the file
outfile.close()