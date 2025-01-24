import requests

response = requests.get(
    url="https://petstore.swagger.io/v2/pet/1"
)

print(response.json())
