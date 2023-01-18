# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 21:45:06 2023

@author: avo01
"""

import pandas as pd
df = pd.read_csv ("C:/Users/avo01/Documents/GitHub/python-challenge/PyPoll/election_data.csv")
print("Election Results")

print("-------------------------")

#The total number of votes cast
Total_Votes=len(df["Ballot ID"])
print("Total Votes: "+str(Total_Votes))

print("-------------------------")
#A complete list of candidates who received votes
outcome=df.groupby("Candidate")["Ballot ID"].count()
outcome_percentage=round(outcome/Total_Votes*100,2)



print(str(outcome.index[0]) + ":" + str(outcome_percentage[0]) + "% (" + str(outcome[0]) +")" )

print(str(outcome.index[1]) + ":" + str(outcome_percentage[1]) + "% (" + str(outcome[1]) +")" )

print(str(outcome.index[2]) + ":" + str(outcome_percentage[2]) + "% (" + str(outcome[2]) +")" )

winner=outcome.max()
winner=outcome[outcome==winner]
winner.index[0]

print("-------------------------")

print("Winner: "+winner.index[0] )

print("-------------------------")