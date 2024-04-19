import requests

# API JsonPlaceHolder
url = 'https://jsonplaceholder.typicode.com/posts/1'

# Requisição GET
response = requests.get(url)
print(response)

# Pegar os dados 
response_json = response.json()
print(response_json)