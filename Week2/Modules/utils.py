import sys
import os
from WriteToFile import *
from pathlib import Path

#print("Flie      part", Path(__file__).absolute())
#print("Directory part", Path().absolute())

#thePath = sys.argv[1]

def filesInFolder(dir):
    listOfPaths = (os.listdir(dir))
    myFile = ""
    output_file = "Paths.txt"
    for path in listOfPaths:
        myFile += path + '\n'

    with open(output_file, 'w') as file_object:
        file_object.write(myFile)


#filesInFolder(thePath)
#filesInFolder("/home/jovyan/")
r = []
def list_files(dir):                                                                                                                                                                                                      
    for root, dirs, files in os.walk(dir):
        for name in files:
            print(name)
            r.append(os.path.join(root, name))
            print(root + name)
    return r
            
             
#list_files(thePath)
#list_files("/home/jovyan/")
def firstLine(lst):
    for myFile in lst:
        if myFile.endswith(".txt"):
            with open(myFile,'r') as file_object:
                lines = file_object.readlines()
                for i in range(1):
                    print(lines[0])


#firstLine(r)
#firstLine(r)
def emails(lst):
    for myFile in lst:
        if myFile.endswith(".txt"):
            with open(myFile,'r') as file_object:
                lines = file_object.readlines()
                for line in lines:
                    if(("@")in line): print(line)

#emails(r)
#emails(r)
def markDowns(lst):
    for myFile in lst:
        if myFile.endswith(".md"):
            with open(myFile,'r') as file_object:
                lines = file_object.readlines()
                for line in lines:
                    if "#" in line[0]:
                        markDownList = [line]
                        write_list_to_file("MarkDownFiles.txt", markDownList)
                        

#markDowns(r)
#markDowns(r)