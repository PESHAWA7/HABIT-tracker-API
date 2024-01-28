# !it's all about using pixela((JUST)).
import requests
from datetime import datetime


pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = "odjjedij3294j43j"
username = "peshawaomer7"
GRAPH_ID = "graph1"

user_params = {
    'token': TOKEN,
    'username': username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "gragh_1",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}"
today = datetime(year=2024, month=1, day=18).strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": "9.74"

}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

pixel_update_endpoint = f"{pixela_endpoint}/{username}/graphs/{GRAPH_ID}/{today}"

pixel_update = {
    "quantity": "5.0"
}
response = requests.delete(url=pixel_update_endpoint, headers=headers)
