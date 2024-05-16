import requests
import json
import csv

# Authentication details and base URL
AuthClientId = 'YourAPIKey'
AuthSecret = 'YourSecretKey'
baseUrl = "https://console.kamatera.com/"

def list_servers():
    url = baseUrl + "service/servers"
    headers = {'AuthClientId': AuthClientId, 'AuthSecret': AuthSecret, 'Cookie': 'cwmid=001'}
    response = requests.get(url, headers=headers)
    server_list = json.loads(response.text)
    get_ids(server_list)

def get_ids(server_list):
    server_details = []
    for server in server_list:
        server_id = server["id"]
        server_name = server["name"]
        server_details.append((server_id, server_name))
    fetch_nics(server_details)

def fetch_nics(server_details):
    # Prepare to write to CSV
    with open('server_networks.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Server Name', 'Network'])  # Write the header

        for serverid, server_name in server_details:
            url = baseUrl + "svc/server/" + serverid + "/nics"
            headers = {'AuthClientId': AuthClientId, 'AuthSecret': AuthSecret, 'Cookie': 'cwmid=001'}
            response = requests.get(url, headers=headers)
            data = json.loads(response.text)

            # Extract NIC networks for each server and write to CSV
            networks = [nic['network'] for nic in data['nics'] if 'network' in nic]
            for network in networks:
                writer.writerow([server_name, network])  # Write each server and network to the CSV


list_servers()
