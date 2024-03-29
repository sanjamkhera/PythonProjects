# Importing necessary libraries
import random
import os
import time

# Defining the path where the books are located
# Change this to required library 
path = "."

# Getting the list of books in the directory
listOfBooks = os.listdir(path)

# Printing the list of books
for books in listOfBooks:
    print(books) 

# Asking the user to choose a book from the list
chosenBook = input("choose a book from list and type it's name?>>")

print("When you are ready type as fast as you can!")

# Opening the chosen book
book = open(chosenBook, encoding = "UTF = 8")

# Choosing a random line from the book
inpLine = random.choice(open(chosenBook, encoding= "UTF = 8").readlines())

# Getting the length of the line
lengthOfLine = len(inpLine)

# If the length of the line is greater than or equal to 10
if lengthOfLine >= 10:
    print("Type:\n"  + inpLine)
    
    # Recording the start time
    t0 = time.time() 
    
    # Asking the user to enter the phrase
    userInput = input("enter the phrase:")
    
    # Recording the end time
    t1 = time.time() 
    
    # Calculating the time taken
    timeTaken = float(t1 - t0)
    
    # Counting the number of words in the user's input
    wordCount = len(userInput.split(" "))
    
    # Counting the number of characters in the user's input
    charCount = len(userInput)
    
    # Calculating words per minute (WPM)
    WPM = ((wordCount/timeTaken)*60)
    
    # Calculating characters per minute (CPM)
    CPM = ((charCount/timeTaken)*60)
    
    # Printing the WPM and CPM
    print("you typed at {:.0f} WPM and {:.2f} CPM".format(WPM,CPM))      
else:
    print("Oops, try again. line had less than 10 characters\n","Here are some characterstics of the book")

# Initializing character and word counts
characters=0
words = 0