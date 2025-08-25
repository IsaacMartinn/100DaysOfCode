import requests
from datetime import datetime

#URL : https://pixe.la/v1/users/isaacmartinn/graphs/graph1.html

USERNAME = "isaacmartinn"
TOKEN = "abdah345ja123f"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "abdah345ja123f",
    "username":"isaacmartinn",
    "agreeTermsOfService":"yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "gr+aph1",
    "name": "Cycling Graph",
    "unit":"Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

post_config = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"1"
}

# response = requests.post(url=post_endpoint,json=post_config,headers=headers)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d"')}"

new_pixel_data = {
    "quantity":"0"
}

response = requests.delete(url=update_endpoint,json=new_pixel_data,headers=headers)
print(response.text)