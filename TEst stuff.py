# https://flixed.notion.site/Flixed-Streaming-Availability-Data-Documentation-73d87a1eaea74353b8afeaff91f6d90d
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
# each provider has a numeric id, which will be used for calling for all movie data.
# you might notice that on line 15 there is no parameter "header". I don't know if it is vital to include this, but
# in this case it works.

f = open("test_data.txt", "w")
# param "w" will create a file, if there isnt already one b the given name
# IT WILL ALSO OVERWRITE THE PREVIOUS TEXT IN THE FILE WHEN OU WRITE TO IT
# we can use "a" (like "append") instead of "w" which wont overwrite the data, instead add to the end.
for item in response_data:
    f.write(item["strId"] +" " + str(item["id"]) + "\n")
    # there's more data than just this, but i figured this is the bare bones needed.
