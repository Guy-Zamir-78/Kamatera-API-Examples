## Get all server VLAN names

## Introduction
This script retrieves VLAN names for all servers under the user's Kamatera account using the Kamatera API and saves them in a CSV file.

## Prerequisites

Before running the script, ensure you have:

- Kamatera API Key and Secret Key
- Python installed on your system

## Installation

1. Clone the repository:
git clone https://github.com/Guy-Zamir-78/Kamatera-API-Examples.git

2. Navigate to the directory:
cd Kamatera-API-Examples

3. Install dependencies:
pip install requests
pip install json
pip install csv

## Usage

1. Replace `YourAPIKey` and `YourSecretKey` with your Kamatera API Key and Secret Key in the script.
2. Run the script:

python get_vlan_names.py


3. The script will fetch VLAN names for all servers using the Kamatera API and store them in a CSV file named `vlan_names.csv`.

## Code Explanation

The script performs the following steps:

- Sets up authentication details and base URL for the Kamatera API.
- Defines functions:
- `list_servers`: Fetches the list of servers.
- `get_ids`: Extracts server IDs and names from the server list.
- `fetch_vlans`: Fetches VLAN names for each server and writes them to a CSV file.
- Calls the `list_servers` function to initiate the process.

## Author Information

- **Author:** Guy Zamir
- **Github Link:** https://github.com/Guy-Zamir-78/Kamatera-API-Examples.git