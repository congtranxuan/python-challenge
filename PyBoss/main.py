import os
import csv
from us_states import us_state
from split_string import split_str  

csvpath = os.path.join("Resources","employee_data.csv")
outputcsv = os.path.join("..","PyBoss","employee_newdata.csv")

with open(csvpath, newline = "")as csvfile:
    with open (outputcsv,"w",newline = "") as csvwriter:
        csvreader = csv.reader(csvfile, delimiter =",")
        writer = csv.writer(csvwriter,delimiter = ",")
    
        for row in csvreader:
            line = []
            name = []
            date =[]
            SSN =[]
            if row[1]=="Name":
                line = [row[0],"First Name","Last Name",row[2],row[3],row[4]]
                
            else:
                names = [letter for letter in row[1]]
                name = split_str(names," ")
                dates = [letter for letter in row[2]]
                date = split_str(dates,"-")
                ssns = [letter for letter in row[3]]
                ssn = split_str(ssns,"-")
                line = [row[0],name[0],name[1],str(date[1])+"/"+str(date[2])+"/"+str(date[0]),"***-**-"+str(ssn[2]),us_state[row[4]]]
            writer.writerow(line)


            








