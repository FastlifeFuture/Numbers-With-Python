#Import the os module
#The os module allows us to create file paths across operating modules

import os

#import the module for reading csv
import csv

#create path for reading  csv
csvpath = os.path.join('Resources', 'budget_data.csv')

#count the total numeber of Months
totalmonths = []
#Net total of  "P&L" over a time period
monthlypl = []

totalpl = []
#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes ??
averagechange = []

#The greates increase in profit (date and amount) over the entire perion 
GreatestIncP = []

#The greatest decrease in profits (date and amount) over the entire period
GreatestDecP =[]

#Use the csv module to read the csv file
with open(csvpath) as csvfile:

    #the csv reader specifies the delimeter and the variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #Read the header row 1st (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    # Read each row of data after the header
    for row in csvreader:
          
        totalmonths.append(row[0])
        monthlypl.append(int(row[1]))


    for i in range(len(totalmonths) - 1):

        averagechange.append(monthlypl[i + 1] - monthlypl[i])      
        
totalpl = (sum(monthlypl))
Min = min(averagechange)
Average = round(sum(averagechange)/len(averagechange),2)
Max = max(averagechange)

testmonth = averagechange.index(max(averagechange))
Maxmonth = totalmonths[testmonth + 1]
testmonth = averagechange.index(min(averagechange))
Minmonth = totalmonths[testmonth + 1]

#print(Maxmonth)
#print(Minmonth)
print(Min)
print(Average)
print(Max)
print(totalpl)
print(len(totalmonths))


output_path = os.path.join("Analysis/financialanalysis.txt")

with open(output_path, 'w') as txtfile:


    output = [
        f' Financial Analysis',
        f' ----------------------------------------------',  
        f' Total Months: {len(totalmonths)}',
        f' Total: {totalpl}',
        f' Average Change: {Average}',
        f' Greatest Increase in Profits: {Maxmonth} {Max}',
        f' Greatest Decrease in Profits: {Minmonth} {Min}']
        
    out_join = "\n".join(output)
 
    txtfile.write(out_join)

    

    
    
  