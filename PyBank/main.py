# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 17:51:59 2023

@author: avo01
"""

import pandas as pd

import os

# Change the local directory when you download the repo
os.chdir('C:/Users/avo01/Documents/GitHub/python-challenge/PyBank')

df = pd.read_csv ("./budget_data.csv")

#The total number of months included in the dataset
total_number_of_months=len(df["Date"])


#The net total amount of "Profit/Losses" over the entire period
net_total_amount=df["Profit/Losses"].sum()


#The changes in "Profit/Losses" over the entire period, and then the average of those changes
changes=df["Profit/Losses"]-df["Profit/Losses"].shift(1)
df["changes"]=changes
average_change=round(df["changes"].mean(),2)


#The greatest increase in profits (date and amount) over the entire period
max_increase=df["changes"].max()
max_decrease=df["changes"].min()

max_increase_df=df[df["changes"]==max_increase]
increase_date=list(max_increase_df["Date"])[0]
increase_value=list(max_increase_df["changes"])[0]
max_decrease_df=df[df["changes"]==max_decrease]
decrease_date=list(max_decrease_df["Date"])[0]
decrease_value=list(max_decrease_df["changes"])[0]

print("Financial Analysis")
print("\n")
print("----------------------------")
print("\n")
print("Total Months: "+str(total_number_of_months))
print("\n")
print("Total: $"+str(net_total_amount))
print("\n")
print("Average Change: $" + str(average_change))
print("\n")
print("Greatest Increase in Profits:" + increase_date+"  ($"+"{:.0f}".format(increase_value)+")")
print("\n")
print("Greatest Decrease in Profits:"+decrease_date+ "  ($"+"{:.0f}".format(decrease_value)+")")


with open('C:/Users/avo01/Documents/GitHub/python-challenge/PyBank/Budget results.txt', 'w') as f:
    f.write("Financial Analysis")
    f.write("\n")
    f.write("----------------------------")
    f.write("\n")
    f.write("Total Months: "+str(total_number_of_months))
    f.write("\n")
    f.write("Total: $"+str(net_total_amount))
    f.write("\n")
    f.write("Average Change: $" + str(average_change))
    f.write("\n")
    f.write("Greatest Increase in Profits:" + increase_date+"  ($"+"{:.0f}".format(increase_value)+")")
    f.write("\n")
    f.write("Greatest Decrease in Profits:"+decrease_date+ "  ($"+"{:.0f}".format(decrease_value)+")")
