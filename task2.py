import requests
import pprint

url = "https://jsonplaceholder.typicode.com/posts"


params = {
"userId" : 1
}

response = requests.get(url, params=params)

print(response.status_code)

pprint.pprint(response.json())



