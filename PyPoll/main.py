import os
import csv
 
#print(os.getcwd())  
#get the path to the csv data file
csvpath = os.path.join("..",'..','..',"RICEHOU201906DATA1","HW","03-Python","Instructions","PyPoll","Resources","election_data.csv")
#create an output text file in the same folder with main.py
textpath = os.path.join("..","PyPoll","Election_Results.txt")

#open the csvfile and read data into csvfile
with open(csvpath,newline ="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    csvheader = next(csvreader)

# set the initial value for memory variables   
    total_vote = 0        #used to calculate the number of votes
    Khan_vote = 0               
    Li_vote = 0   
    Correy_vote = 0   #
    OTooley_vote = 0
   
    for row in csvreader:
        total_vote +=1                   #every row represent for a vote
        if row[2] =="Khan":
            Khan_vote += 1
        elif row[2] =="Li": 
            Li_vote += 1
        elif row[2] == "Correy":
            Correy_vote += 1 
        elif row[2] =="O'Tooley":
            OTooley_vote +=1

    if Khan_vote > Li_vote and Khan_vote > Correy_vote and Khan_vote > OTooley_vote:
        winner = "Khan"
    elif Li_vote > Khan_vote and Li_vote > Correy_vote and Li_vote > OTooley_vote:
        winner ="Li" 
    elif Correy_vote > Khan_vote and Correy_vote > Li_vote and Correy_vote > OTooley_vote:
        winner = "Correy"  
    else: winner = "O'Tooley"    


    #print value to the screen
    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(total_vote))
    print('----------------------------')
    print("Khan: " +str(round(Khan_vote*100/total_vote))+".000%"+" ("+str(Khan_vote)+")")
    print("Correy: " +str(round(Correy_vote*100/total_vote))+ ".000%" +" ("+str(Correy_vote) + ")")
    print("Li: " +str(round(Li_vote*100/total_vote))+".000%"+" ("+str(Li_vote)+")")
    print("O'Tooley: " +str(round(OTooley_vote*100/total_vote))+".000%"+" ("+str(OTooley_vote)+")")
    print("----------------------------")
    print('Winner: '+str(winner))
    print("----------------------------")

#Write the file named Financial Analysis.txt
with open(textpath, 'w', newline='') as textfile:
    csvwriter = csv.writer(textfile)
    csvwriter.writerow(["Election Results"])                      #used [] to list
    csvwriter.writerow(['------------------------------------'])
    csvwriter.writerow(['Total Votes:  '+ str(total_vote)])
    csvwriter.writerow(['------------------------------------'])
    csvwriter.writerow(["Khan: " +str(round(Khan_vote*100/total_vote))+".000%"+" ("+str(Khan_vote)+")"])
    csvwriter.writerow(["Correy: " +str(round(Correy_vote*100/total_vote))+".000%"+" ("+str(Correy_vote)+")"])
    csvwriter.writerow(["Li: " +str(round(Li_vote*100/total_vote))+".000%"+" ("+str(Li_vote)+")"])
    csvwriter.writerow(["O'Tooley: " +str(round(OTooley_vote*100/total_vote))+".000%"+" ("+str(OTooley_vote)+")"])
    csvwriter.writerow(['------------------------------------'])
    csvwriter.writerow(['Winner: '+str(winner)])
    csvwriter.writerow(['------------------------------------'])
