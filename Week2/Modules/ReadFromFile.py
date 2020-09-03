import csv

def readingFromFile(file):    
    if file.endswith(".txt"):
        with open(file,'r') as file_object:
            lines = file_object.readlines()

        myFile = ''
        for line in lines:
            myFile += line.strip()

        print(myFile) 
    elif file.endswith(".csv"):
        with open(file,'r') as file_object:
            reader = csv.reader(file_object)
            csvList = list(reader)
        
        print(csvList)
