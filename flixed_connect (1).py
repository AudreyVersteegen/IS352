import pprint
import urllib
import requests

def getEndpoint(endpoint, parameters):
    baseUrl = "https://api.flixed.io/v1/"
    resource = baseUrl + endpoint

    parameters['apiKey'] = "PASTE KEY HERE"

    print("Getting Endpoint: " + resource + "?" + urllib.parse.urlencode(parameters))
    response = requests.get(resource, headers=headers, params=parameters)
    response_data = response.json()
    # pprint.pprint(response_data)
    return response_data


# https://api.flixed.io/v1/episodes/62422?apiKey=<apiKey>

# the resource is the endpoint and the parameters are any values that would be passed in to
# the endpoint. The point of these lines is to rebuild the url
episode_id = 62422
resource = f"episodes/{episode_id}"
parameters = {
}

# the getEndpoint function requests the data from the endpoint and passes in any parameters tha may
# be needed. The function returns a dictionary containing the api's response. Each time the getEndpoint
# function is called, a new request to the API is made and new data are requested.
response = getEndpoint(resource, parameters)
pprint.pprint(response)

