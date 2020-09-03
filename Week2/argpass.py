from Modules.ReadFromFile import *
from Modules.WriteToFile import *
import sys

theType = sys.argv[1]
file = sys.argv[2]

print(file)
    
if theType =="read":
    readingFromFile(file)    

elif theType=="write":    
    writeToFile = file
    listToFile = ["Hey","My","Name","is","2"]
    write_list_to_file(writeToFile,listToFile)






