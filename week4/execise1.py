#Exercise 1¶
#Open the file './data/befkbhalderstatkode.csv'
#Turn the csv file into a numpy ndarray with np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
#Using this data:
#neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
#       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
#       10: 'Amager Vest', 99: 'Udenfor'}
#Find out how many people lived in each of the 11 areas in 2015
#Make a bar plot to show the size of each city area from the smallest to the largest
#Create a boolean mask to find out how many people above 65 years lived in Copenhagen in 2015
#How many of those were from the other nordic countries (not dk)
#Make a line plot showing the changes of number of people in vesterbro and østerbro from 1992 to 2015

import numpy as np
import csv
import matplotlib.pyplot as plt

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
               5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
               10: 'Amager Vest', 99: 'Udenfor'}

ds = np.genfromtxt('../../data/befkbhalderstatkode.csv',delimiter=',',dtype=np.uint,skip_header=1)
#AAR,BYDEL,ALDER,STATKODE,PERSONER

def peopleInPart(neighb):
    returnT = []
    for part in neighb:
        
        
     
        mask = (ds[:,0] == 2015) & (ds[:,1] == part)
        np.sum(ds[mask][:,4])
        amount = np.sum(ds[mask][:,4])
        returnT.append(amount)
    print(returnT)
    return returnT

#listOfPeople = peopleInPart(neighb)

def plotPart(neighb):
    listForPlot = peopleInPart(neighb)
    print(listForPlot.values())
    for p in inlistForPlot:
        plt.xticks(rotation=45)
        plt.bar(neighb.keys,p)
    plt.show()

peopleInPart(neighb)

def peopleAboveAge65(ds, neighb):
    mask = (ds[:,0] == 2015) & (ds[:,2] > 65) & (ds[:,3] == 5100)
    sum = 0
    for k in neighb:
        sum += number_of_people_per_neighbourhood(ds,k,mask)
    return sum