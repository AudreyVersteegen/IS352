import pprint
from datetime import datetime
# read watchlist
# search function
Application = None
def printMenu():
    print(f"Welcome to {Application}!")
    print("Would you like to: \n1. Search for a movie or show\n2. Go to your watchlist\n3. Exit")
    userInput = input("Please enter a number:  ").strip()

    if userInput != "1" and userInput != "2" and userInput != "3":
        print("That option was not provided, please choose again. ")
        userInput = printMenu()
    return userInput

def search(input, flag): #flag can be t, r, d
    if flag == 't':
        #search by title
        print("title")
    if flag == 'r':
        # search by runtime
        print("runtime")
    if flag == 'd':
        print("date")
        #search by release Date
    if flag == 'l':
        print("language")
        # search by language


# read in the data, into a dict.
# shows
fileName = "Show_Data.txt"
with open(fileName) as filePointer:
    showFileContents = filePointer.read().strip()
    shows = showFileContents.split('\n')
    showDict = {}

for show in shows:
    elements = show.split('\t')
    releaseDate = elements[1][-4:]
    toAdd = {'releaseDate' : releaseDate, 'misc' : elements[2]}
    if elements[0] not in showDict:
        showDict[elements[0]] = toAdd


# movies
fileName = "Movie_Data.txt"
with open(fileName) as filePointer:
    movieFileContents = filePointer.read().strip()
    movies = movieFileContents.split('\n')
    movieDict = {}

for movie in movies:
    elements = movie.split('\t')
    releaseDate = elements[1][-4:]
    toAdd = {'releaseDate' : releaseDate, 'runtime' : elements[2], 'language' : elements[3]}
    if elements[0] not in movieDict:
        movieDict[elements[0]] = toAdd

# search funtime
# aka main
EXIT = "3"
userInput = printMenu()
while True:
    if userInput == EXIT:
        break
    if userInput == "1":
        # search for the movie with given parameters
        # ask for them
        print("What would you like to search for?")
        print("1. Title \n2. Runtime \n3. Release Date \n4. Language")
        toSearch = input("enter stuff here")
        print("searching....")
    if userInput == "2":
        # show them their watchlist
        print("got to watchlist")
    userInput = printMenu()

