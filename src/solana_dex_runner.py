from solana_dex_fetcher import fetch_latest_solana_token_profiles
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Global data to hold token information
token_data = []

def update_plot(frame):
    global token_data

    # Fetch latest token profiles and prices
    token_data = fetch_latest_solana_token_profiles()

    # Update the plot with current prices
    names = [token['name'] for token in token_data]
    prices = [token['price'] for token in token_data]

    ax.clear()
    ax.bar(names, prices, color='green')
    ax.set_title('Dynamic Token Prices on Solana')
    ax.set_ylabel('Price (USD)')
    ax.set_xlabel('Tokens')
    ax.set_ylim(0, max(prices + [1]) * 1.2)  # Set dynamic y-axis range
    ax.grid(True)

    # Print token details in the console
    for token in token_data:
        print(f"Token: {token['name']}, Price: {token['price']} USD, Address: {token['address']}")

# Set up Matplotlib figure and animation
fig, ax = plt.subplots(figsize=(10, 6))
ani = FuncAnimation(fig, update_plot, interval=5000)  # Update every 5 seconds

plt.show()
