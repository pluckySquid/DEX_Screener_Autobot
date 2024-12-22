import requests

def fetch_latest_solana_token_profiles():
    try:
        # API endpoint for latest token profiles
        url = "https://api.dexscreener.com/token-profiles/latest/v1"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        # Filter for Solana-specific profiles
        solana_profiles = [profile for profile in data if profile.get('chainId') == 'solana']
        token_data = []  # List to hold token information
        if solana_profiles:
            for i, profile in enumerate(solana_profiles[:5]):  # Limit to 5 tokens
                token_address = profile.get('tokenAddress', 'N/A')
                price = fetch_token_price(token_address)  # Fetch token price
                
                token_data.append({
                    'name': f"Token {i + 1}",
                    'address': token_address,
                    'price': price,
                    'url': profile.get('url', 'N/A'),
                    'icon': profile.get('icon', 'N/A'),
                    'header': profile.get('header', 'N/A'),
                    'description': profile.get('description', 'N/A'),
                    'links': profile.get('links', [])
                })
        return token_data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
        return []

def fetch_token_price(token_address):
    try:
        # API endpoint for fetching token price
        url = f"https://api.dexscreener.com/latest/dex/tokens/{token_address}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract token price from the first trading pair
        token_info = data.get("pairs", [{}])[0]  # Get the first trading pair
        return float(token_info.get("priceUsd", 0))  # Convert price to float
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price for token {token_address}: {e}")
        return 0
