import pandas as pd
# import numpy as np

budget_file = "03-Python_Homework_PyBank_Resources_budget_data.csv"
budget_file_pd = pd.read_csv(budget_file)
# print(budget_file_pd.head())

# The total number of months included in the dataset
months_count = budget_file_pd['Date'].count() 
# print('Total Months : ' , months_count)

# The net total amount of "Profit/Losses" over the entire period
Total = budget_file_pd['Profit/Losses'].sum()
# print('Total : $', Total)

# The average of the changes in "Profit/Losses" over the entire period
moving_change = budget_file_pd['Profit/Losses'].diff()
budget_file_pd['Moving_Change'] = moving_change
# print(budget_file_pd.head())

sum_moving_change = budget_file_pd['Moving_Change'].sum()
# print(sum_moving_change)

change_count = budget_file_pd["Moving_Change"].count()
# print(change_count)

average_change = sum_moving_change/change_count
# print(average_change)

new_budget_table = budget_file_pd[["Date","Moving_Change"]]

# The greatest increase in profits (date and amount) over the entire period

max_row = new_budget_table["Moving_Change"].max()
print(max_row)

min_row = new_budget_table["Moving_Change"].min()
print(min_row)

max_row_date = new_budget_table.loc[new_budget_table["Moving_Change"]==new_budget_table["Moving_Change"].max()]

for k,v in max_row_date.iterrows():
    max_date = v["Date"]
    max_moving_change = v["Moving_Change"]

min_row_date = new_budget_table.loc[new_budget_table["Moving_Change"]==new_budget_table["Moving_Change"].min()]

for k,v in min_row_date.iterrows():
    min_date = v["Date"]
    min_moving_change = v["Moving_Change"]

print("Financial Analysis")
print("----------------------------------------------------")
print('Total Months : ' , months_count)
print('Total : $', Total)
print('Average  Change: ',average_change.round(2))
print('Greatest Increase in Profits: {0} (${1})'.format( max_date, round(max_moving_change)))
print('Greatest Decrease in Profits: {0} (${1})'.format( min_date, round(min_moving_change)))

with open("Financial_Analysis.txt",'w') as line:
    line.write("Financial Analysis \n")
    line.write("---------------------------------------------------------------\n")
    line.write("Total Months: {total_months} \n".format(total_months = months_count))
    line.write('Total : ${total} \n'.format(total = Total))
    line.write('Average  Change: ${average}\n'.format(average = round(average_change)))
    line.write('Greatest Increase in Profits: {0} (${1})\n'.format( max_date, round(max_moving_change)))
    line.write('Greatest Decrease in Profits: {0} (${1})\n'.format( min_date, round(min_moving_change)))

    
    











