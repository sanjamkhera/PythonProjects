data = open("winning lottery numbers.csv")
lines = data.readlines() # Read each line of the file
dict1 = {} # Created empty dictionary
freq= [] # Created empty list

for line in lines: # used a for loop to split comma separated text in each line
    line = line.split(",")
    winningNum = line[1]
    # print(winningNum)
    for eachNum in winningNum: 
        eachNum = winningNum.split()
    # print(eachNum)
    for number in eachNum:
        # print(number)
        if number not in dict1: # Used an if statement to append to a 
            dict1[number]=0 #dictionary. where key is the number and value is frequency
        dict1[number] = dict1[number] + 1

for values in dict1.items(): #Created a list of tuples from dictionary to sort
    freq.append(values) #appened to the list
    
indexingLength =  len(freq)-1

sort = False

#used bubble sort to sort the list

while not sort: #Since we were not allowed to use Sort
    sort = True #I found this method called "Bubble Sort"
    for item in range(0, indexingLength): 
        if freq[item][1] > freq[item+1][1]:
            sort = False
            freq[item], freq[item+1] = freq[item+1], freq[item]

#printed statements as per the assignment
print("The 10 most frequent numbers are:")
for numbers in freq[-10:]:
    print("{} was drawn {} times.".format(numbers[0],numbers[1]))
print("The 10 least frequent numbers are:")        
for numbers in freq[:10]:
    print("{} was drawn {} times.".format(numbers[0],numbers[1]))
