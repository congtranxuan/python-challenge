import os
import csv
from split_string import split_str

filepath = os.path.join("raw_data","paragraph_1.txt")
outputpath = os.path.join("..","PyParagraph","Paragraph_Analysis.txt")
with open(filepath,"r",newline ="")as csvfile:
    csvreader = csv.reader(csvfile,delimiter =",")
    csvheader = next(csvreader)
    text = ""
    for i in csvheader:
        text += i

    letter=[l for l in text]
    group =[" ",",","."]
    count = 0
    for i in range(len(letter)):
        if letter[i] in group:
            count +=1
    word = []
    word = split_str(letter," ")
    sentence = []
    sentence = split_str(letter,".")
  

print("Paragraph Analysis")
print("----------------------------------")
print("Approximate Word Count: "+str(len(word))) 
print("Approximate Sentence Count: "+str(len(sentence)))
print("Average Letter Count: "+str(round((len(letter)-count)/len(word),2)))
print("Average Sentence Length: "+str(len(word)/len(sentence)))

#Write the file named Paragraph Analysis.txt
with open(outputpath,"w",newline ="") as outputtext:
    csvwriter = csv.writer(outputtext)
    csvwriter.writerow(["Paragraph Analysis"])                      #used [] to list
    csvwriter.writerow(['---------------------------------'])
    csvwriter.writerow(["Approximate Word Count: "+str(len(word))])
    csvwriter.writerow(["Approximate Sentence Count: "+str(len(sentence))])
    csvwriter.writerow(["Average Letter Count: "+str(round((len(letter)-count)/len(word),2))])
    csvwriter.writerow(["Average Sentence Length: "+str(len(word)/len(sentence))])
    