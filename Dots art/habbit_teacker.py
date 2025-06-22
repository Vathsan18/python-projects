import requests

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token" : "abcdefgh",
    "username" : "vathsan18",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

create_endpoint = f"{pixela_endpoint}/vathsan18/graphs"

graph_config = {
    "id" : "graph1",
    "name" : "coding",
    "unit" : "min",
    "type" : "int",
    "color" : "shibafu"
}

headers = {
    "X-USER-TOKEN" : "abcdefgh"
}

fill_endpoint = create_endpoint = f"{pixela_endpoint}/vathsan18/graphs/graph1"
fill_data = {
    "date" : "20241109",
    "quantity" : "75"
}

update_endpoint = f"{pixela_endpoint}/vathsan18/graphs/graph1/20241113"
update_data = {
    "quantity" : "70"
}

response = requests.put(url=update_endpoint, json=update_data, headers=headers)
print(response.text)