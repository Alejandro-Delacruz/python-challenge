# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 17:51:59 2023

@author: avo01
"""

#import pandas as pd

import os
os.getcwd()

Date=[]
profit_losses=[]

import csv
with open('budget_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Date.append(row['Date'])
        profit_losses.append(row['Profit/Losses'])

out = []
for item in profit_losses:
    out.append(float(item))




#The total number of months included in the dataset
total_number_of_months=len(Date)


#The net total amount of "Profit/Losses" over the entire period
net_total_amount=sum(out)


#The changes in "Profit/Losses" over the entire period, and then the average of those changes
shift=out[1:len(out)]

change=[]
for i in range(len(out)-1):
    change.append(out[i+1]-out[i])
    

# Average change, max and min changes
average_change=round(sum(change)/len(change),2)
increase_value=max(change)
decrease_value=min(change)
increase_date=Date[change.index(increase_value)+1]
decrease_date=Date[change.index(decrease_value)+1]


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


with open('Budget results.txt', 'w') as f:
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
