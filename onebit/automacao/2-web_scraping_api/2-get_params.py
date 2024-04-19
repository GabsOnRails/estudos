import requests

# API JsonPlaceHolder
url = 'https://jsonplaceholder.typicode.com/posts/'

# Adicionando um payload
payload = {
    "id":[1,2,3,4,5],
    "userId":1
}

# Realizando requisição
response = requests.get(url,params=payload)

# Melhorando legibilidade do print
response_json = response.json()
for i in response_json:
    print(i, "\n")

# print(response)
# print(response.json())