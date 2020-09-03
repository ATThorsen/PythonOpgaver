from Modules.ReadFromFile import *
from Modules.WriteToFile import *
import sys

print("1 for read a file")
print("2 for writing to a file")
print("3 for taking text from 1 file and moving it to another")
theInput = input()
print(theInput)

def readFromFile() :
    print("File name you wanna take text from")
    file = input("")
    with open(file,'r') as file_object:
        lines = file_object.readlines()

    myFile = ''
    textInList = []
    for line in lines:
        myFile += line.strip() + '\n'
        textInList.append(line.strip())
    print(textInList)
    
    writeToAFile(myFile)

def writeToAFile(TextToAdd) :
    
    
    print("Name a file you wanna write to")
    writeToFile = input()+".txt"
    with open(writeToFile, 'w') as file_object:
        file_object.write(TextToAdd)

    print(TextToAdd)


if theInput=="1":
    print("File name")
    file = input("")
    readingFromFile(file)
    
elif theInput=="2":    
    print("Name a file you wanna write to")
    writeToFile = input()
    listToFile = ["Hey","My","Name","is","2"]
    write_list_to_file(writeToFile,listToFile)

elif theInput == "3":
    readFromFile()




