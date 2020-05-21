import os
import csv

print("Financial Analysis")
print("----------------------------")

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv,'r') as bud:
    csvreader = csv.reader(bud, delimiter=",")
    
    fileheader = next(bud)

    budlist = list(csvreader)

    #total months
    totmo = len(budlist)
    print(f'Total Months: {totmo}')

    #net total
    nettot = sum(int(r[1]) for r in budlist)
    Format_nettot = "{:,}".format(nettot)
    print(f'Total: ${str(Format_nettot)}')
 
    #Avg Change
    for row in range(len(budlist)):
        #calculate change month to month
        if row == 0:
            budlist[row].append(0)
        else:
            budlist[row].append(int(budlist[row][1]) - int(budlist[row-1][1]))
    chatot = sum(int(r[2]) for r in budlist)
    #total month -1 to drop the very first month
    avgcha = chatot / (totmo-1)
    Format_avgcha = "{:,.2f}".format(avgcha)
    print(f'Avearge Change: ${Format_avgcha}')

    #greatest increase
    vmax = max(int(r[2]) for r in budlist)
    for row in range(len(budlist)):
        if budlist[row][2] == vmax:
            dmax = budlist[row][0]
    Format_vmax = "{:,}".format(vmax)
    print(f'Greatest Increase in Profits: {dmax} (${Format_vmax})')

    #greatest decrease
    vmin = min(int(r[2]) for r in budlist)
    for row in range(len(budlist)):
        if budlist[row][2] == vmin:
            dmin = budlist[row][0]
    Format_vmin = "{:,}".format(vmin)
    print(f'Greatest Decrease in Profits: {dmin} (${Format_vmin})')

#create a text file with this information
output_file = os.path.join("analysis","pybank_analysis.txt")

with open(output_file, "w") as datafile:
    datafile.write("Financial Analysis \n")
    datafile.write("----------------------------\n")
    datafile.write(f'Total Months: {totmo}\n')
    datafile.write(f'Total: ${str(Format_nettot)}\n')
    datafile.write(f'Avearge Change: ${Format_avgcha}\n')
    datafile.write(f'Greatest Increase in Profits: {dmax} (${Format_vmax})\n')
    datafile.write(f'Greatest Decrease in Profits: {dmin} (${Format_vmin})\n')