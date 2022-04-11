import pprint
import urllib
import requests
apiKey = "OhnrM0IKwIbaIwa1D7tBm96Y32vVd0v3"

baseUrl = "https://api.flixed.io"
resource = baseUrl + "/v1/streaming-providers/10008/titles?apiKey=" + apiKey

parameters = {
}

parameters['apiKey'] = "OhnrM0IKwIbaIwa1D7tBm96Y32vVd0v3"
print("Getting Endpoint: " + resource + "?" + urllib.parse.urlencode(parameters))

response = requests.get(resource, params = parameters)
response_data = response.json()
print(resource)
print(response_data)

file = open("Netflix_Movies.txt", "a")
file.write("MOVIES \n")
for item in response_data['movies']:
    file.write(str(item))
    file.write('\n')

file.write("\nSHOWS\n")
for item in response_data['shows']:
    file.write(str(item))
    file.write('\n')