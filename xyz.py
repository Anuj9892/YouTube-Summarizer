import requests

response = requests.get(f"")
output= response.json()
print(output)