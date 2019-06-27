import os
import csv

#get the path to the csv data file
csvpath = os.path.join("..",'..','..',"RICEHOU201906DATA1","HW","03-Python","Instructions","PyPoll","Resources","election_data.csv")
#create an output text file in the same folder with main.py
textpath = os.path.join("..","PyPoll","Election_Results.txt")

#open the csv file and read data into csvfile
with open(csvpath,newline ="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    csvheader = next(csvreader)
    total_vote = 0        #used to calculate the number of votes
    Candidate = []        #stored the names of candidate  
    Candidates_vote = []  #stored the candidates' votes
    i = 0                 #used to represent the number of candidates
    winner = ''
    winner_vote = 0  
    
    for row in csvreader:
        total_vote +=1                  #every row represents for a vote
        if row[2] not in Candidate:     #if there is a new candidate, add to the list
            i +=1                       #mark the number of candidates
            Candidate.append(row[2])    #add name of candidate to the list
            Candidates_vote.append(0)   #increase the candidates's vote list to 1 unit
        for j in range(i):              #in the list
            if Candidate[j] == row[2]: 
                Candidates_vote[j] += 1
            if Candidates_vote [j] > winner_vote:#if the candidate's vote is more than winner vote, update the winner
                winner = Candidate[j]
                winner_vote = Candidates_vote[j]
       #print value to the screen
    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(total_vote))
    print('----------------------------')
    for k in range(len(Candidate)):
        print(str(Candidate[k])+": "+str(round(Candidates_vote[k]*100/total_vote))+".000%"+" ("+str(Candidates_vote[k])+")")
    print("----------------------------")
    print('Winner: '+str(winner))
    print("----------------------------")

#Write the file named Election_Results.txt
with open(textpath, 'w', newline='') as textfile:
    csvwriter = csv.writer(textfile)
    csvwriter.writerow(["Election Results"])                      #used [] to list
    csvwriter.writerow(['------------------------------------'])
    csvwriter.writerow(['Total Votes:  '+ str(total_vote)])
    csvwriter.writerow(['------------------------------------'])
    for k in range(len(Candidate)):
        csvwriter.writerow([str(Candidate[k])+": "+str(round(Candidates_vote[k]*100/total_vote))+".000%"+" ("+str(Candidates_vote[k])+")"])
    csvwriter.writerow(['------------------------------------'])
    csvwriter.writerow(['Winner: '+str(winner)])
    csvwriter.writerow(['------------------------------------'])
