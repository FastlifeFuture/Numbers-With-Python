#Import the os module
#The os module allows us to create file paths across operating modules

import os

#import the module for reading csv
import csv

#create path for reading csv
csvpath = os.path.join('Resources', 'election_data.csv')

#count the total number of votes cast
votescast = []
totalvotescast = []

#complete list of candidates who received votes
VoterId = []
County = []
candidates = []

#percentage of votes each cadidate won
votepercentagek = []
votepercentagec = []
votepercentagel = []
votepercentageo = []

#total number of votes each candidate won
votesfork = 0
votesforc = 0
votesforl = 0
votesforo = 0

# winner of the electiom
winner =[]

with open(csvpath) as csvfile:

    #the csv reader specifies the delimeter and the variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    #read the header row 1st(skip this step if there is no header)
    csv_header = next(csvreader)
    #print(f'CSV Header: {csv_header}')

    #read each row of data after the header
    for row in csvreader:

       VoterId.append(row[0])
       County.append(row[1])
       candidates.append(row[2])


       

    totalvotescast = (len(VoterId))
    print(totalvotescast)
 
    for name in candidates:
           
  
            if name == 'Khan':
                votesfork += 1

            elif name == 'Correy':
                votesforc += 1
            
            elif name == 'Li':
                votesforl += 1
            
            else:
                votesforo += 1
    
 

votepercentagek = round((votesfork/totalvotescast),2) * 100
votepercentagec = round((votesforc/totalvotescast),2) * 100
votepercentagel = round((votesforl/totalvotescast),2) * 100
votepercentageo = round((votesforo/totalvotescast),2) * 100
print(votesfork)
print(votesforc)
print(votesforl)
print(votesforo)
   
print(votepercentagek)
print(votepercentagec)
print(votepercentagel)
print(votepercentageo)



output_path = os.path.join("analysis/ElectionResults.txt")


with open(output_path, 'w') as txtfile:

    output = [
        f'Election Results',
        f'-----------------------------',
        f'Total Votes: {totalvotescast}',
        f'-----------------------------',
        f'Khan: {votepercentagec}({votesfork})',
        f'Correy: {votepercentagec} ({votesforc})',
        f'Li: {votepercentagel} ({votesforl})',
        f'O Tooley: {votepercentageo} ({votesforo})',
        f'------------------------------',
        f'Winner: Khan',
        ]
    
    out_join = "\n".join(output)

    txtfile.write(out_join)
    





        