'''
The following code consists of three functions and a while loop

First function: nxtgen, takes in two arguments "population" (living amoebas)
and "survivalRate" (chance of survival) to predict the population of living 
amoebas in the next generation using numpy's built in method np.random.choice.

Second function: singleTrial, takes in one argument "survival rate" (chance of survival)
and uses a while loop and nxtgen (function) to simulate upto 20 generations of the amoeba.
It also uses an if statement to determine if the colony of amoeba dies before
20 generations. Retrnuning the number of generations it survived uptill 20, a boolean
if the amoebas die before 20 generations and the count of amoeba after 20 generations.

Third function: repeatedTrial, takes in two arguments "survival rate" (chance of survival)
and "noOfTrials" number of iterations. It creates an empty array of zeros "results" and
populates the array using second function "singleTrial" with 2 dimesional data 
which consists of no of generations,booleans and amoeba count. 
It also consists varaibles that are used to print desired data.

Finally, a while loop is used to print data for diffenret survival odds, as per the
question.

'''

import numpy as np 

def nxtGen(population,survivalRate):
    a = survivalRate
    b = 1-survivalRate #death rate
    survived = np.random.choice([0,1],population,p=[b,a])
    # p = probability
    amoebasInSecondGen = (survived.sum()*2)
    # print (survived)
    return amoebasInSecondGen

def singleTrial(survivalRate):
    amoebaCount = 1
    generations = 0
    deadBefore20 = False
    while amoebaCount>0 and generations<20:
        amoebaCount = nxtGen(amoebaCount, survivalRate)
        generations = generations + 1
        if amoebaCount == 0:
            deadBefore20 = True
        # print(deadBefore20)
    return (generations,deadBefore20,amoebaCount)

# print(singleTrial(0.9))

def repeatedTrials(survivalRate, noOfTrials):
    results = np.zeros((noOfTrials,3))
    for index in range(noOfTrials):
        results[index] = singleTrial(survivalRate)
    # print(results[index])
    # According to week 9 Lecture videos, 
    # You run for loops to get the following three values.
    # I used splicing, indexing and built in numpy methods to get desired results
    didNotSurvive = (100*results[:,1].sum())/noOfTrials
    genAvgOnFailures = (results[results[:,1]>0][:,0].mean())
    amoebaAvgOnSurvival = (results[results[:,1]==0][:,2].mean())
    print("The Amoebas did not survive {:.2f}% of the time.".format(didNotSurvive))
    print("On failures, there were {:.2f} generations on averge.".format(genAvgOnFailures))
    print("If the amoebas did survive, the average population was {:.2f}".format(amoebaAvgOnSurvival))
# print(repeatedTrials(0.50,1000))

survivalOdds = 0.5
# starting with 50% survival odds going upto 95%

while survivalOdds < 1:
    print("For survival odds {:.2f}:".format(survivalOdds))
    repeatedTrials(survivalOdds,1000)
    survivalOdds = survivalOdds + 0.05
    

