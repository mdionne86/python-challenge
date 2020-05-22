import os
import csv
from collections import Counter 

elect_csv = os.path.join("Resources", "election_data.csv")

#open the file and removes unneccesary columns from the list
with open(elect_csv,'r') as eld:
    csvreader = csv.reader(eld, delimiter=",")
    
    fileheader = next(eld)

    totlist = list(csvreader)
    
    candlist = []
    #we just want a list with all the names
    for row in totlist:
        candlist.append(row[2])

#calc total votes
totvo = len(candlist)

#sets up a dictionary with candidate names and their counts 
#   from the big candidate name list we created earlier
canddict = Counter(candlist)
dict(canddict)

#finds the candidate with the most votes
wincan = max(canddict, key=canddict.get)

print("-------------------------")    
print("Election Results")
print("-------------------------")
print(f'Total Votes: {totvo}')
print("-------------------------")
for key,value in canddict.items():
    print(f'{key}: {"{:.3%}".format(value/totvo)} ({value})')
print("-------------------------")
print(f'Winner: {wincan}')
print("-------------------------")

#create a text file with this information
output_file = os.path.join("analysis","pypoll_results_analysis.txt")

with open(output_file, "w") as datafile:
    datafile.write("-------------------------\n")
    datafile.write("Election Results\n")
    datafile.write("-------------------------\n")
    datafile.write(f'Total Votes: {totvo}\n')
    datafile.write("-------------------------\n")
    for key,value in canddict.items():
        datafile.write(f'{key}: {"{:.3%}".format(value/totvo)} ({value})\n')
    datafile.write("-------------------------\n")
    datafile.write(f'Winner: {wincan}\n')
    datafile.write("-------------------------\n")