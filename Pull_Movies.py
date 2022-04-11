# to pull from Neflix_Movies.txt and Netflix_Shows.py and generate the dictionaries
from typing import Any

import pprint
import urllib
import requests
apiKey = "OhnrM0IKwIbaIwa1D7tBm96Y32vVd0v3"

baseUrl = "https://api.flixed.io"
#resource = baseUrl + "/v1/streaming-providers/10008/titles?apiKey=" + apiKey

parameters = {
}

parameters['apiKey'] = "OhnrM0IKwIbaIwa1D7tBm96Y32vVd0v3"
print("Getting Endpoint: " + resource + "?" + urllib.parse.urlencode(parameters))

# response = requests.get(resource, params = parameters)
# response_data = response.json()
# print(resource)
# print(response_data)

#making a count
Movie_Data = file.open("Movie_Data.txt", "a")

with open("Netflix_Movies.txt") as filePointer:
    Movie_IDS = filePointer.read()

Movie_IDS = Movie_IDS.split()



#while there are more lines in Movie_IDS then in Data, look for more

