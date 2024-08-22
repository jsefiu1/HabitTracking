import requests
from datetime import datetime

USERNAME = "joni69"
TOKEN = "8e29hh02skfjhw0s02"

pixela_endpoint = " https://pixe.la/v1/users"

user_params = {
	"token": TOKEN,
	"username": USERNAME,
	"agreeTermsOfService": "yes",
	"notMinor": "yes",
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

graphs_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graphs_config = {
	"id": "graph1",
	"name": "Cycling Graph",
	"unit": "Km",
	"type": "float",
	"color": "ajisai"
}

headers = {
	"X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graphs_endpoint, json=graphs_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
today= datetime(year=2024, month=1, day=27)
# print(today.strftime("%Y%m%d"))
pixel_data = {
	# "date": today.strftime("%Y%m%d"),
	"quantity": "9.00",
}

# response = requests.post(url=pixel_creation_endpoint,json=pixel_data, headers=headers)
# print(response.text)

# pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime("%Y%m%d")}"
# response = requests.put(url=pixel_update_endpoint, json=pixel_data, headers=headers)
# print(response.text)


pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime("%Y%m%d")}"
response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)