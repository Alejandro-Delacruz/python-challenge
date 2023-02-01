# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 21:45:06 2023

@author: avo01
"""

# Change the local directory when you download the repo
import os
os.getcwd()

ballot=[]
county=[]
candidate=[]

import csv
with open('election_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        ballot.append(row['Ballot ID'])
        county.append(row['County'])
        candidate.append(row["Candidate"])


#The total number of votes cast
Total_Votes=len(ballot)

#A complete list of candidates who received votes
candidate1=0
candidate2=0
candidate3=0
for i in range(len(candidate)):
    if candidate[i]=='Charles Casper Stockham':
        candidate1=candidate1+1
    elif candidate[i]=='Diana DeGette':
        candidate2=candidate2+1
    elif candidate[i]=='Raymon Anthony Doane':
        candidate3=candidate3+1
    

#Store the result as a dictionary
result={'Charles Casper Stockham':candidate1, 'Diana DeGette':candidate2, 'Raymon Anthony Doane':candidate3}

#decide who is the winner
winner=max(candidate1,candidate2,candidate3)
winner_name = list(filter(lambda x: result[x] == winner, result))[0]

##################### print the result to the console
print("Election Results")
print("\n")
print("-------------------------")
print("\n")
print("Total Votes: "+str(Total_Votes))
print("\n")
print("-------------------------")
print("\n")
for i in set(candidate):
    print(i + ": " + str(round(result[i]/Total_Votes*100,3)) + "% (" + str(result[i]) +")" )
    print("\n")
print("-------------------------")
print("\n")
print("Winner: "+winner_name)
print("\n")
print("-------------------------")
print("\n")


##################### write the result as txt
with open("Election results.txt", 'w') as f:
    f.write("Election Results")
    f.write("\n")
    f.write("-------------------------")
    f.write("\n")
    f.write("Total Votes: "+str(Total_Votes))
    f.write("\n")
    f.write("-------------------------")
    f.write("\n")
    for i in set(candidate):
        f.write(i + ": " + str(round(result[i]/Total_Votes*100,3)) + "% (" + str(result[i]) +")" )
        f.write("\n")
    f.write("-------------------------")
    f.write("\n")
    f.write("Winner: "+winner_name )
    f.write("\n")
    f.write("-------------------------")
    f.write("\n")