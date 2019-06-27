import os
import csv
import us_states

csvpath = os.path.join("..",'..','..',"RICEHOU201906DATA1","HW","03-Python","ExtraContent","Instructions","PyBoss","employee_data.csv")
outputcsv = os.path.join("..","ByBoss","newemployee_data.csv")

with open(csvpath, newline = "")as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    csvheader = next(csvreader)
    print(csvheader) 
    
    for row in csvreader:
        name = []
        DOB=[]
        SSN =[]
        names = [letter for letter in row[1]]
        name = split_str(names," ")
            




def split_str(list,a):
    separate=[]
    inter = []
    for i in range(len(list)):
        if list[i] == a: 
            result = ""
            for k in inter:
                result += str(k)
            separate.append(result)
            inter = []
            continue
        else: inter.append(list[i])
        if i == (len(list)-1):
            result = ""
            for k in inter:
                result += str(k)
            separate.append(result)
    return separate



