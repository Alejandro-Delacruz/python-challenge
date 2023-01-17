# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 21:45:06 2023

@author: avo01
"""

import pandas as pd
df = pd.read_csv ("C:/Users/avo01/Documents/GitHub/python-challenge/PyBank/budget_data.csv")

#The total number of months included in the dataset
total_number_of_months=len(df["Date"])
print("Total Months: "+str(total_number_of_months))

#The net total amount of "Profit/Losses" over the entire period
net_total_amount=df["Profit/Losses"].sum()
print("Total: "+str(net_total_amount))

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
changes=df["Profit/Losses"]-df["Profit/Losses"].shift(1)
df["changes"]=changes
average_change=df["changes"].mean()
print("Average Change:" + str(average_change))
