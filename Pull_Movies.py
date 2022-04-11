# to pull from Neflix_Movies.txt and Netflix_Shows.py and generate the dictionaries
from typing import Any

import pprint
import urllib
import requests
apiKey = "OhnrM0IKwIbaIwa1D7tBm96Y32vVd0v3"

baseUrl = "https://api.flixed.io"
parameters = {
}
parameters['apiKey'] = "OhnrM0IKwIbaIwa1D7tBm96Y32vVd0v3"

# response = requests.get(resource, params = parameters)
# response_data = response.json()
# print(resource)
# print(response_data)

#making a count
with open("Movie_Data.txt") as filePointer:
    Movie_Data = filePointer.read()
with open("Netflix_Movies.txt") as filePointer:
    Movie_IDS = filePointer.read()

Movie_IDS = Movie_IDS.strip().split("\n")
movies = Movie_Data.strip().split("\n")
if movies[0] == '':
    movies = []
movie_number = len(movies)
while(movie_number < len(Movie_IDS)):
    # DO API CALL
    resource = baseUrl + f"/v1/movies/{Movie_IDS[movie_number]}?apiKey=" + apiKey

    response = requests.get(resource, params = parameters)
    response_data = response.json()

    # append to new file
    if ('title' in response_data):
        to_append = ''
        to_append += response_data['title'] + '\t' +str(response_data["releaseDate"]) + '\t' + str(response_data['runtimeMins']) + '\t' + response_data['language']

        movies.append(to_append)
        with open('Movie_Data.txt', 'a') as fileHandler:
                fileHandler.write(str(to_append) + "\n")
    else:
        break

    movie_number += 1

#then we need to write



