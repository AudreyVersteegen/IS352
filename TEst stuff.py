import pprint
import urllib
import requests
apiKey = "OhnrM0IKwIbaIwa1D7tBm96Y32vVd0v3"

baseUrl = "https://api.flixed.io"
resource = baseUrl + "/v1/streaming-providers?apiKey=" + apiKey

parameters = {
}

parameters['apiKey'] = "OhnrM0IKwIbaIwa1D7tBm96Y32vVd0v3"
print("Getting Endpoint: " + resource + "?" + urllib.parse.urlencode(parameters))

response = requests.get(resource, params = parameters)
response_data = response.json()
print(resource)
print(response_data)
# here response_data is a list of dictionaries, each entry in the list is for a different provider
# im just here to test run the code, give an example of it working
# you might notice that on line 15 there is no parameter "header". I don't know if it is vital to include this, but
# in this case it works.