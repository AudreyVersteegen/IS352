import pprint
from datetime import datetime
import openpyxl

#setting up the language
wkbk = openpyxl.load_workbook("is352 language code.xlsx")
sheet = wkbk.active
langDict = {}
for line in range(2, sheet.max_row):
    code = sheet.cell(row=line, column=1).value
    lang = sheet.cell(row=line, column=2).value
    langDict[code] = lang


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
        print("Would you like a movie that is: ")
        print("1. Less then an hour\n2. In between 1 and 2 hours\n3. Longer then 2 hours")
        runtime = input("Enter: ")
        search(runtime, 'r')
    elif toSearch == '3':
        print("Select the range the release year falls within : ")
        print("1. Before 1920\n2. After 1920 and before 1950 \n3. The 1950's\n4. The 1960's\n5. The 1970's\n6. The 1980's\n7. The 1990's\n8. The 2000's\n9. The 2010's\n10. The 2020's")
        date = input("Enter: ")
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
        for item in movieDict:
            if input == "1" and movieDict[item]['releaseDate'] < 2015:
                print(item)
            elif input == "2" and (movieDict[item]['releaseDate'] >= 1920 and movieDict[item]['releaseDate'] < 1950):
                print(item)
            elif input == "3" and (movieDict[item]['releaseDate'] >= 1950 and movieDict[item]['releaseDate'] < 1960):
                print(item)
            elif input == "4" and (movieDict[item]['releaseDate'] >= 1960 and movieDict[item]['releaseDate'] < 1970):
                print(item)
            elif input == "5" and (movieDict[item]['releaseDate'] >= 1970 and movieDict[item]['releaseDate'] < 1980):
                print(item)
            elif input == "6" and (movieDict[item]['releaseDate'] >= 1980 and movieDict[item]['releaseDate'] < 1990):
                print(item)
            elif input == "7" and (movieDict[item]['releaseDate'] >= 1990 and movieDict[item]['releaseDate'] < 2000):
                print(item)
            elif input == "8" and (movieDict[item]['releaseDate'] >= 2000 and movieDict[item]['releaseDate'] < 2010):
                print(item)
            elif input == "9" and (movieDict[item]['releaseDate'] >= 2010 and movieDict[item]['releaseDate'] < 2020):
                print(item)
            elif input == "10" and movieDict[item]['releaseDate'] >= 2020:
                print(item)

        #search by release Date
    elif flag == 'l':
        # search by language
        for item in movieDict:
            if input.lower() == langDict[movieDict[item]['language']].lower():
                print(item)
        for item in showDict:
            if input.lower() == langDict[showDict[item]['language']].lower():
                print(item)


# read in the data, into a dict.
# shows
fileName = "Show_Data.txt"
with open(fileName) as filePointer:
    showFileContents = filePointer.read().strip()
    shows = showFileContents.split('\n')
    showDict = {}

for show in shows:
    elements = show.split('\t')
    releaseDate = elements[1][-4:].strip()
    if releaseDate != 'None':
        releaseDate = int(releaseDate)
    else:
        releaseDate = 0
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
    releaseDate = elements[1][-4:].strip()
    runtime = elements[2].strip()
    if releaseDate != 'None':
        releaseDate = int(releaseDate)
    else:
        releaseDate = 0
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

