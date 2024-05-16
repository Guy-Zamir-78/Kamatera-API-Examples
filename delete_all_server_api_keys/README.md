## Kamatera API Key Deletion with a value of "Server'

This script deletes all API keys with the name "Server" using the Kamatera API.

## Prerequisites

Before running the script, ensure you have:

- Kamatera API Key and Secret Key
- Python installed on your system

## Usage

1. Replace `AuthClientId` and `AuthSecret` with your Kamatera API Key and Secret Key in the script.

2. Run the script:
python delete_all_server_api_keys.py


## Code Explanation

The script performs the following steps:

1. Imports necessary modules: `requests` and `json`.
2. Sets up authentication details and base URL for the Kamatera API.
3. Defines functions:
- `list_keys`: Fetches all API keys.
- `delete_key`: Deletes API keys with the name "Server".
4. Calls the `list_keys` function to start the process.

## Author Information

- **Author:** Guy Zamir
- **Github Link:** [Guy-Zamir-78/Kamatera-API-Examples](https://github.com/Guy-Zamir-78/Kamatera-API-Examples)

