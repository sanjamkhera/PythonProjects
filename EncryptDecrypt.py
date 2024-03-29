# pseudocode: 
# Started by giving the user a list of files.
# opened the input file.
# went over the file using read lines. 
# Used a for loop and if statements to strip \n. 
# and count frequency of letters and store it in a dictioanry.
# Created a list of letters and frequency, usinng a for loop
# consisting of tuples only with frequency more than 10.
# Used bubble sort to sort that list of tuples. 
# Extracted the first element of the sorted list and stored in a sep list
# Created another dictionary from two lists using zip, where key is encrypted letter
# and value is decrypted letter
# used that dictionay to decrypt the file

import os
path = "C:/Users/sanja/OneDrive - University of Manitoba/School/COMP 1012/Assignment 2"
listOfFiles = os.listdir(path)

for files in listOfFiles:
    print(files) 
chosenFile = input("choose a file to decrypt?:")
theFile = open(chosenFile,"r")
file = theFile.readlines()
dict1 = {}
freq = []

for line in file:
    line = line.strip("\n")
    for char in line:
        if char not in dict1:
            dict1[char] = 0
        else:
            dict1[char] = dict1[char]+1

for values in dict1.items():
    if values[1] > 10:
        freq.append(values)
        
indexingLength = len(freq)-1
sort = False
while not sort:
    sort = True
    for item in range(0, indexingLength):
        if freq [item][1] < freq[item+1][1]:
            sort = False
            freq[item+1], freq[item] = freq[item], freq[item+1]
print(freq)     
 
letters = []          
for letter in freq:
    if letter not in letters:
        letters.append(letter[0])
print(letters)

shift = int(19)
decryptList = []
newLength = len(freq)

decryptDict = dict(zip(letters,decryptList))
print(decryptDict)

for eachLetter in range(len(letters)):
    decryptData = letters[((eachLetter+shift)%newLength)]
    decryptList.append(decryptData)
    print(decryptData)

decrypted = ""

for text in file:
    if text in decryptDict:
        decrypted += decryptDict[text]
    else:
        decrypted += text
       
print(decrypted)