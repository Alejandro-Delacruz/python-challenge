# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 21:45:06 2023

@author: avo01
"""

import pandas as pd
import os

# Change the local directory when you download the repo
os.chdir('C:/Users/avo01/Documents/GitHub/python-challenge/PyPoll')
df = pd.read_csv ("./election_data.csv")

#The total number of votes cast
Total_Votes=len(df["Ballot ID"])

#A complete list of candidates who received votes
outcome=df.groupby("Candidate")["Ballot ID"].count()
outcome_percentage=round(outcome/Total_Votes*100,2)

winner=outcome.max()
winner=outcome[outcome==winner]
winner.index[0]

print("Election Results")
print("\n")
print("-------------------------")
print("\n")
print("Total Votes: "+str(Total_Votes))
print("\n")
print("-------------------------")
print("\n")
print(str(outcome.index[0]) + ":" + str(outcome_percentage[0]) + "% (" + str(outcome[0]) +")" )
print("\n")
print(str(outcome.index[1]) + ":" + str(outcome_percentage[1]) + "% (" + str(outcome[1]) +")" )
print("\n")
print(str(outcome.index[2]) + ":" + str(outcome_percentage[2]) + "% (" + str(outcome[2]) +")" )
print("\n")
print("-------------------------")
print("\n")
print("Winner: "+winner.index[0] )
print("\n")
print("-------------------------")
print("\n")

with open("C:/Users/avo01/Documents/GitHub/python-challenge/PyPoll/Election results.txt", 'w') as f:
    f.write("Election Results")
    f.write("\n")
    f.write("-------------------------")
    f.write("\n")
    f.write("Total Votes: "+str(Total_Votes))
    f.write("\n")
    f.write("-------------------------")
    f.write("\n")
    f.write(str(outcome.index[0]) + ":" + str(outcome_percentage[0]) + "% (" + str(outcome[0]) +")" )
    f.write("\n")
    f.write(str(outcome.index[1]) + ":" + str(outcome_percentage[1]) + "% (" + str(outcome[1]) +")" )
    f.write("\n")
    f.write(str(outcome.index[2]) + ":" + str(outcome_percentage[2]) + "% (" + str(outcome[2]) +")" )
    f.write("\n")
    f.write("-------------------------")
    f.write("\n")
    f.write("Winner: "+winner.index[0] )
    f.write("\n")
    f.write("-------------------------")
    f.write("\n")