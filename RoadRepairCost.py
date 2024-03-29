COST_PER_KM = 1400000
FUNDING_AVAILABLE = 40000000

# Text string used in __str__ method of street class
text = """{} is {:.2f} km long, sees {} cars per day, and is in {} condition."""

class Street:
    # Built in constructor used to store variables
    def __init__(self, streetName, streetLength, noOfCars, streetCondition):
        self.streetName = streetName
        self.streetLength = streetLength
        self.noOfCars = noOfCars
        self.streetCondition = streetCondition

    # compareStreets method compares street conditions
    def compareStreets (self, other):
        if (self.streetCondition == "poor") and (other.streetCondition == "good"):
            return True
        if (self.streetCondition == "poor") and (other.streetCondition == "fair"):
            return True
        if (self.streetCondition == "fair") and (other.streetCondition == "good"):
            return True
        if (self.streetCondition == other.streetCondition) and (self.noOfCars > other.noOfCars):
            return True
        else:
            return False

    # Built in method used for printing
    def __str__(self):
        return (text.format(self.streetName,self.streetLength,self.noOfCars,self.streetCondition))

    # costOfRepair helps find repair cost of each street
    def costOfRepair(self):
       return COST_PER_KM*self.streetlength
 

def streetSort(streets):
    """
    Takes a list "street"
    ---------------------
    streets : list

    Returns: Sorted Lists 
    
    Bubble Sort Lab 09
    """
    for i in range(len(streets)-1,0,-1):
        for j in range(i):
            if streets[j]<streets[j+1]:
                temp = streets[j]
                streets [j] = streets[j+1]
                streets [j+1] = temp

streetsList = []

def streetFunc():
    """
    This function opens the input file name, uses a for loop to parse 
    through the file, gets each components, makes instances of street 
    class for each line and appends it empty streetsList. 
    It uses the function streetSort to sort the list. Then, a for loop 
    is used to print each component of the list and another for loop
    uses costOfRepair method from street class to check for funding.
    """
    inpFile = input("Please enter the name of the road file:")
    file = open(inpFile, encoding = "UTF = 8")
    data = file.readlines()
    for line in data:
        line = line.strip()
        line = line.split(",")
        streetName = line[0]
        streetLength = float(line[1])
        noOfCars = int(line[2])
        streetCondition = line[3]
        streetsList.append(Street(streetName,streetLength,noOfCars,streetCondition)) 

    streetSort(streetsList)

    print("The streets, in decreasing order of priority, are:")
    print("--------------------------------------------------")
    
    for i in streetsList:
        print(i)
        
    moneySpent = 0
    
    for i in streetsList:
        repairCost = i.costOfRepair()
        while repairCost <= FUNDING_AVAILABLE-moneySpent:
            moneySpent = moneySpent + repairCost
            print("{} will be fixed at a cost of ${}".format(i.streetName,repairCost))
            print()
        if FUNDING_AVAILABLE < repairCost:
            REM_BALANCE = FUNDING_AVAILABLE-moneySpent
            print("The amount left over is {:.2f}".format(REM_BALANCE))

streetFunc()