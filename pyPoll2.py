#PyPoll

# import the os and csv modules, counter function
import os
import csv
#from collections import Counter

totalVotes = 0
candidateDic = {}

maxPercent = 0.0
maxCandidate = ""



#reference file path
csvpath = os.path.join('raw_data','election_data_2.csv')

def countVotes():

    with open(csvpath, newline='') as csvpoll1:
        # set csvreader var to read and specify delimiter
        csvreader = csv.reader(csvpoll1, delimiter=',')
        # skip the headers
        next(csvreader)
     
        #count to the last row of values
        totalVotes = len(list(csvreader))
        #print("totalVotes: ",totalVotes)

    return totalVotes



def countVotesForCandidate():
     #loop to put unique candidate names in list, create dictionary with key = name, value = tally of their votes
    newCandidate = ""
    
    
    with open(csvpath, newline='') as csvpoll1:
        # set csvreader var to read and specify delimiter
        csvreader = csv.reader(csvpoll1, delimiter=',')
        # skip the headers
        next(csvreader)

        #set the vote tally to zero within the loop
        votes = 0
        for row in csvreader:
            newCandidate = row[2]
            # check to see if the candidate in column 3 does not exist
            if (newCandidate not in candidateDic.keys()):
                #first vote for candidate
                votes = 1
                candidateDic[newCandidate] = votes
                    
            else:
                # increment the vote of the candidate
                candidateDic[newCandidate] += 1 
        print("Candidates and votes: ",candidateDic)

def testCalcVotePercentages():
    with open(csvpath, newline='') as csvpoll1:
        # set csvreader var to read and specify delimiter
        csvreader = csv.reader(csvpoll1, delimiter=',')
        # skip the headers
        next(csvreader)
        for k, v in candidateDic.items():
            print("key,value",k, v)


def calcVotePercentages():
    with open(csvpath, newline='') as csvpoll1:
        # set csvreader var to read and specify delimiter
        csvreader = csv.reader(csvpoll1, delimiter=',')
        # skip the headers
        next(csvreader)
        for k, v in candidateDic.items():
            voteCalc = v/totalVotes *100
            if (voteCalc > maxPercent):
                maxPercent = voteCalc
                maxCandidate = k
                #issue with maxPercent var even though global?
             
        print("percentage for ",k," is: ","{0:.0f}%".format(voteCalc))
        print("Max : percentage for ",maxCandidate," is: ","{0:.0f}%".format(maxPercent))


  

countVotesForCandidate()
totalVotes = countVotes()
calcVotePercentages()
print("Winner is: ",maxCandidate," with ","{0:.0f}%".format(maxPercent)," of total votes")

#export to text file
file = open("pollTwo.txt","w") 
file.write("Election Results \n")
file.write("Total Votes: " + str(totalVotes) + "\n")
file.write("Candidates and votes: " + str(candidateDic) + "\n")
file.write("Percentage for " + str(k) + " is: " + "{0:.0f}%".format(str(voteCalc) + "\n")
file.write("Winner is: " + str(maxCandidate) + " with " + str("{0:.0f}%".format(maxPercent)) + " of total votes \n")
   
file.close() 










































# #open file
# with open(csvpath, newline='') as csvpoll1:
#     csvreader = csv.reader(csvpoll1, delimiter=',')
#     next(csvreader)



# #reference file path
# csvpath = os.path.join('raw_data','election_data_1.csv')



# #open file
# with open(csvpath, newline='') as csvpoll1:
#     csvreader = csv.reader(csvpoll1, delimiter=',')
#     next(csvreader)

#     #loop to capture candidates
#     for row in csvreader:
#         candidate = row[2]
#         votes = 0
#         if (candidate not in candidates):
#             candidates.append(candidate)
#         else:
#             votes +=1 
#         # add the vote as the value for the index (candidate name), 
#     print(candidates)

    

#     #count instances of each candidates in list 
#     Counter(candidates)
    
#     #[[x,l.count(x)] for x in set(l)]

#     print(Counter)



        
#     print("Election Results")
#     print("Total Votes: ",vote_count())
#     #print(candidate, 
#     #print("Winner: " + candidate with greatest count???)

#     #export to text file