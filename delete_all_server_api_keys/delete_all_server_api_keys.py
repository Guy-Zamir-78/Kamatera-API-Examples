import requests
import json

# Authentication details and base URL
AuthClientId = "YourAPIKey"
AuthSecret = "YourSecretKey"
baseUrl = "https://console.kamatera.com/"


def list_keys():
    url = baseUrl + "svc/apikeys?filter=&size=500&sorting=&from="
    print(url)

    payload = {}
    headers = {"AuthClientId": AuthClientId, "AuthSecret": AuthSecret}

    response = requests.request("GET", url, headers=headers, data=payload)

    data = response.json()
    for item in data.get("items", []):
        if item.get("specialType") == "Server":
            delete_key(item["id"])


def delete_key(server_id):
    print(f"Deleting server with ID: {server_id}")
    url = baseUrl + "svc/apikeys/" + str(server_id)

    payload = {}
    headers = {"AuthClientId": AuthClientId, "AuthSecret": AuthSecret}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)


list_keys()
