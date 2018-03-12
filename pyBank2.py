#PyBankv3

# import the os and csv modules
import os
import csv

totalRevenue = 0
totalMonths = 0

average = 0

#use a dictionary
revDic = {}

#Dictionary of key = month, value = rev
changeInRevenuePerMonth =[]
monthlyRevenueList =[] 
revenueChangeList =[]
        
#open the csv
csvpath = os.path.join('raw_data','budget_data_2.csv')

def printToTextFile(myList):
    #export to text file
    file = open("bankTwo.txt","w") 
 
    file.write("Financial Analysis \n") 
    file.write("Total Months: " + str(totalMonths)+ "\n") 
    file.write("Total Revenue: " + str(totalRevenue) + "\n") 
    file.write("max change in revenue: "+ str(max(myList)) + "min change in revenue: " + str(min(myList)) + "\n")
    file.write("average change in month to month revenue: " + str(average) + "\n") 
    #since avg is local, seems it won't print to txt here?
 
    file.close() 
    


def compareRevMonths():
     #loop to make dictionary with key = month, value = rev
    total = 0
    with open(csvpath, newline='') as csvbank1:
        # set csvreader var to read and specify delimiter
        csvreader = csv.reader(csvbank1, delimiter=',')
        # skip the headers
        next(csvreader)
        
        for row in csvreader:
            revDic[row[0]] = int(row[1])
            monthlyRevenueList.append(int(row[1]))
        print("monthRevenueList: ", monthlyRevenueList)
            
        #got help wit a "comprehesion" that replaces the commented logic below in one line :-)
        revenueChangeList = [month1 - month2 for month1, month2 in zip(monthlyRevenueList, monthlyRevenueList[1:])]
        
        #
        #for month in range(len(monthlyRevenueList)):
          #      print ("month index",month, month + 1)
           #     revenueDifference = int(monthlyRevenueList[month + 1]) - int(monthlyrevenueList[month])
            #    revenueChangeList.append(revenueDifference)
                                      
    print("the diff list", revenueChangeList,"max: ", max(revenueChangeList), "min : ", min(revenueChangeList))
    
    printToTextFile(revenueChangeList)
    
    return revenueChangeList

def calcAverageMonthlyRevenue(myList):
    
    listLen = len(myList)
    total = 0
    print('calcAverageMonthlyRevenue: revenue change list',myList, listLen)
    # use the next line instead of: for elem in myList:
    for elem in range(len(myList)):
        #print(myList[elem])
        total =  myList[elem] + total 
    average = total / listLen
    print("average change in month to month revenue: ", average)
    
    


with open(csvpath, newline='') as csvbank1:

    # set csvreader var to read and specify delimiter
    csvreader = csv.reader(csvbank1, delimiter=',')
    next(csvreader)

    #find count of row values (number of months) minus header)
    for row in csvreader:
        
        totalMonths = totalMonths + 1

        #find sum of column 1/revenue with loop, capture int value in column 1 and add to total_revenue
        totalRevenue = int(row[1]) + totalRevenue
        
    #print(int(row[1]))
    print("Total Months: " + str(totalMonths))
    print("Total Revenue: " + str(totalRevenue))
    

#call functions
            
calcAverageMonthlyRevenue(compareRevMonths())
#print("the diff list", revenueChangeList,"max: ", max(revenueChangeList), "min : ", min(revenueChangeList))