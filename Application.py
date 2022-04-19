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

def searchMenu():
    print("What would you like to search for?")
    print("1. Title \n2. Runtime \n3. Release Date \n4. Language")
    toSearch = input("Enter option:")
    if toSearch == '1':
        title = input("Enter title: ")
        search(title, 't')
    elif toSearch == '2':
        # COME BACK TO THIS
        # DO WE WANT TO HAVE A RUNTIME RANGE
        print("Whould you like a movie that is: ")
        print("1. Less then an hour\n2. In between 1 and 2 hours\n3. Longer then 2 hours")
        runtime = input("Enter: ")
        search(runtime, 'r')
    elif toSearch == '3':
        # COME BACK TO THIS
        # DO WE WANT DECADE RANGES
        date = input("Enter date: ")
        search(date, 'd')
    elif toSearch == 'l':
        lang = input("Enter language: ")
        search(lang, 'l')

def search(input, flag): #flag can be t, r, d
    if flag == 't':
        #search by title
        for title in movieDict.keys():
            if input.upper() in title.upper():
                # good
                print(title)
        for title in showDict.keys():
            if input.upper() in title.upper():
                print(title)
    elif flag == 'r':
        # search by runtime
        for item in movieDict:
            if input == "1" and movieDict[item]['runtime'] < 60:
                print(item)
            elif input == "2" and (movieDict[item]['runtime'] >= 60 and movieDict[item]['runtime'] < 120):
                print(item)
            elif input == '3' and movieDict[item]['runtime'] > 120:
                print(item)
    elif flag == 'd':
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
    runtime = elements[2].strip()
    if runtime != 'None':
        runtime = int(runtime)
    else:
        runtime = 0
    toAdd = {'releaseDate' : releaseDate, 'runtime' : runtime, 'language' : elements[3]}
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
        searchMenu()
    if userInput == "2":
        # show them their watchlist
        print("got to watchlist")
    userInput = printMenu()

