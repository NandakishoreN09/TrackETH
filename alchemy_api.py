import requests
import pandas as pd
from config import ALCHEMY_URL

# Function to get ERC-20 transactions
def get_erc20_transactions(wallet_address):
    headers = {"Content-Type": "application/json"}
    payload = {
        "jsonrpc": "2.0",
        "method": "alchemy_getAssetTransfers",
        "params": [{
            "fromBlock": "0x0",
            "toBlock": "latest",
            "toAddress": wallet_address,
            "category": ["erc20"],
            "withMetadata": True,
            "excludeZeroValue": True
        }],
        "id": 1
    }
    response = requests.post(ALCHEMY_URL, json=payload, headers=headers).json()
    return pd.DataFrame(response["result"]["transfers"]) if "result" in response else pd.DataFrame()

# Function to get ETH (native) transactions (both received and sent)
def get_eth_transactions(wallet_address):
    headers = {"Content-Type": "application/json"}
    
    # Fetch ETH received transactions
    payload_received = {
        "jsonrpc": "2.0",
        "method": "alchemy_getAssetTransfers",
        "params": [{
            "fromBlock": "0x0",
            "toBlock": "latest",
            "toAddress": wallet_address,
            "category": ["external"],
            "excludeZeroValue": True
        }],
        "id": 1
    }
    response_received = requests.post(ALCHEMY_URL, json=payload_received, headers=headers).json()
    df_received = pd.DataFrame(response_received["result"]["transfers"]) if "result" in response_received else pd.DataFrame()

    # Fetch ETH sent transactions
    payload_sent = {
        "jsonrpc": "2.0",
        "method": "alchemy_getAssetTransfers",
        "params": [{
            "fromBlock": "0x0",
            "toBlock": "latest",
            "fromAddress": wallet_address,
            "category": ["external"],
            "excludeZeroValue": True
        }],
        "id": 1
    }
    response_sent = requests.post(ALCHEMY_URL, json=payload_sent, headers=headers).json()
    df_sent = pd.DataFrame(response_sent["result"]["transfers"]) if "result" in response_sent else pd.DataFrame()

    # Merge received and sent transactions
    df_eth = pd.concat([df_received, df_sent], ignore_index=True)
    
    return df_eth

# Function to get ETH balance directly from Alchemy API
def get_eth_balance(wallet_address):
    headers = {"Content-Type": "application/json"}
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBalance",
        "params": [wallet_address, "latest"],
        "id": 1
    }
    
    response = requests.post(ALCHEMY_URL, json=payload, headers=headers).json()

    if "result" in response:
        return int(response["result"], 16) / 1e18  # Convert Wei to ETH
    return 0.0
