import os
import csv
 
#print(os.getcwd())  
#get the path to the csv data file
csvpath = os.path.join("..",'..','..',"RICEHOU201906DATA1","HW","03-Python","Instructions","PyBank","Resources","budget_data.csv")
#create an output text file in the same folder with main.py
textpath = os.path.join("..","PyBank","Financial_Analysis.txt")

#open the csvfile and read data into csvfile
with open(csvpath,newline ="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    csvheader = next(csvreader)
# print report to the screen 
    print("Financial Analysis")
    print("----------------------------")
# set the initial value for memory variables   
    month = 0       #used to calculate the number of months
    total = 0       #used to calculate the total profit/losses          
    minchange = 0   #used to find greatest decrease value of change
    maxchange = 0   #used to find greatest increase value of change
    for row in csvreader:
        month +=1                   #every row represent for each month
        if month ==1:               #at first row, set change and sum of change equal to 0
            sumchange = 0
            change = 0
        else:                       #from row 2, calculate the change
            change = int(row[1])-last
            sumchange +=change
                    
        if change >= maxchange:      #find the min and max value of change and save the date
            maxchange = change
            datemax = row[0]
        elif change <= minchange:
            minchange = change 
            datemin = row[0]        
        total += int(row[1])        #get the total profit/losses
        last = int(row[1])          #update the value for last profit/loss

    #print value to the screen
    print("Total Months: " + str(month))
    print("Total: $"+str(total))
    print("Average  Change: $" + str(round(sumchange/85,2)))
    print("Greatest Increase in Profits:"+ str(datemax)+ " "+ "($"+str(maxchange)+")")
    print("Greatest Decrease in Profits:"+ str(datemin)+ " "+ "($"+str(minchange)+")")

#Write the file named Financial Analysis.txt
with open(textpath, 'w', newline='') as textfile:
    csvwriter = csv.writer(textfile)
    csvwriter.writerow(["Financial Analysis"])                      #used [] to list
    csvwriter.writerow(['------------------------------------'])
    csvwriter.writerow(['Total Months: '+ str(month)])
    csvwriter.writerow(['Total: $'+str(total)])
    csvwriter.writerow(["Average  Change: $" + str(round(sumchange/85,2))])
    csvwriter.writerow(["Greatest Increase in Profits:"+ str(datemax)+ " "+ "($"+str(maxchange)+")"])
    csvwriter.writerow(["Greatest Decrease in Profits:"+ str(datemin)+ " "+ "($"+str(minchange)+")"])


