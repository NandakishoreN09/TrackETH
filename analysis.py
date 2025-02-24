def analyze_eth_wallet(df_eth, wallet):
    df_eth["value"] = df_eth["value"].astype(float)  # Convert ETH values to float

    # Ensure addresses are compared case-insensitively
    df_eth["from"] = df_eth["from"].str.lower()
    df_eth["to"] = df_eth["to"].str.lower()
    wallet = wallet.lower()

    # ETH inflow & outflow calculation
    eth_inflow = df_eth[df_eth["to"] == wallet]["value"].sum()
    eth_outflow = df_eth[df_eth["from"] == wallet]["value"].sum()

    return eth_inflow, eth_outflow
