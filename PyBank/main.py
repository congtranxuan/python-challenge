import os
import csv
 
#print(os.getcwd())  
csvpath = os.path.join("..",'..','..',"RICEHOU201906DATA1","HW","03-Python","Instructions","PyBank","Resources","budget_data.csv")
textpath = os.path.join("Financial_analysis.text")

with open(csvpath,newline ="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    csvheader = next(csvreader)
    print("Financial Analysis")
    print("----------------------------")
    
    month = 0
    total = 0
    minchange = 0
    maxchange = 0
    for row in csvreader:
        month +=1
        if month ==1:
            sumchange = 0
            change = 0
        else:
            change = int(row[1])-last
            sumchange +=change
        if change >= maxchange:
            maxchange = change
            datemax = row[0]
        elif change <= minchange:
            minchange = change 
            datemin = row[0]        
        total += int(row[1])
        last = int(row[1])

    
    print("Total Months: " + str(month))
    print("Total: $"+str(total))
    print("Average  Change: $" + str(round(sumchange/85,2)))
    print("Greatest Increase in Profits:"+ str(datemax)+ " "+ "($"+str(maxchange)+")")
    print("Greatest Decrease in Profits:"+ str(datemin)+ " "+ "($"+str(minchange)+")")

with open(textpath, 'w', newline='') as textfile:
    csvwriter = csv.writer(textfile,delimiter=' ')
    csvwriter.writerow("Total Months: " + str(month)) 


