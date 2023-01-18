# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 17:51:59 2023

@author: avo01
"""

import pandas as pd
df = pd.read_csv ("C:/Users/avo01/Documents/GitHub/python-challenge/PyBank/budget_data.csv")
print("Finacial Analysis\n")
print("----------------------------")
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

#The greatest increase in profits (date and amount) over the entire period
max_increase=df["changes"].max()
max_decrease=df["changes"].min()


max_increase_df=df[df["changes"]==max_increase]
increase_date=list(max_increase_df["Date"])[0]
increase_value=list(max_increase_df["changes"])[0]
max_decrease_df=df[df["changes"]==max_decrease]
decrease_date=list(max_decrease_df["Date"])[0]
decrease_value=list(max_decrease_df["changes"])[0]
print("Greatest Increase in Profits:",increase_date,"{:.0f}".format(increase_value))
print("Greatest Decrease in Profits:",decrease_date,"{:.0f}".format(decrease_value))
