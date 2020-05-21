import os
import csv
from collections import Counter 

elect_csv = os.path.join("Resources", "election_data.csv")


with open(elect_csv,'r') as eld:
    csvreader = csv.reader(eld, delimiter=",")
    
    fileheader = next(eld)

    totlist = list(csvreader)

    #total votes
    totvo = len(totlist)

    #Who are the candidates? I ran this first and printed
    #   the set to see how many candidates there are first
    #   and their names
    candset = set()
    for row in totlist:
        candset.add(row[2])
    #print(candlist)
    candlist = list(candset)

    #Now that I know there are 4 candidates, I can create
    #   variables for each to store thier vote count
    can1tot = 0
    can2tot = 0
    can3tot = 0
    can4tot = 0
    #now to count

    ###Can I make this better with functions?
    for row in range(len(totlist)):
        if totlist[row][2] == candlist[0]:
            can1tot = can1tot + 1
        elif totlist[row][2] == candlist[1]:
            can2tot = can2tot + 1
        elif totlist[row][2] == candlist[2]:
            can3tot = can3tot + 1
        elif totlist[row][2] == candlist[3]:
            can4tot = can4tot + 1
    


    #maths ---- can I use functions here too?
    can1per =
    can2per =
    can3per =
    can4per = 

print("Election Results")
print("-------------------------")
print(f'Total Votes: {totvo}')
print("-------------------------")
print(f'{candlist[0]}: {can1tot}')
print(f'{candlist[1]}: {can2tot}')
print(f'{candlist[2]}: {can3tot}')
print(f'{candlist[3]}: {can4tot}')
print("Correy: 20.000% (704200)**")
print("Khan: 63.000% (2218231)**")
print("O'Tooley: 3.000% (105630)**")
print("Li: 14.000% (492940)**")
# print("-------------------------")
# #   Winner: Khan
# print("-------------------------")

#create a text file with this information
# output_file = os.path.join("analysis","pypoll_results_analysis.txt")

# with open(output_file, "w") as datafile:
#     datafile.write("Election Results\n")
#     datafile.write("-------------------------\n")
#     datafile.write("-------------------------\n")
#     datafile.write("-------------------------\n")
#     datafile.write("-------------------------\n")