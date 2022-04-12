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
with open("Show_Data.txt") as filePointer:
    Show_Data = filePointer.read()
with open("Netflix_Shows.txt") as filePointer:
    Show_IDS = filePointer.read()

Show_IDS = Show_IDS.strip().split("\n")
shows = Show_Data.strip().split("\n")
if shows[0] == '':
    shows = []
show_number = len(shows)
while(show_number < len(Show_IDS)):
    # DO API CALL
    resource = baseUrl + f"/v1/shows/{Show_IDS[show_number]}?apiKey=" + apiKey

    response = requests.get(resource, params = parameters)
    response_data = response.json()

    # append to new file
    if ('name' in response_data):
        to_append = ''
        to_append += response_data['name'] + '\t' +str(response_data["releaseDate"]) + '\t' + str(response_data['seasons']) + '\t' + response_data['language']

        shows.append(to_append)
        with open('Show_Data.txt', 'a') as fileHandler:
                fileHandler.write(str(to_append) + "\n")
    else:
        break

    show_number += 1

#then we need to write
