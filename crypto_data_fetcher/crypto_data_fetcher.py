import requests
import pandas as pd
from datetime import datetime

# === Crypto Data Fetcher ===
# Fetches Bitcoin & Ethereum prices from the CoinGecko API,
# structures the data with Pandas, and exports it to a CSV file.

# 1 Define API endpoint and parameters
url = "https://api.coingecko.com/api/v3/simple/price"
params = {"ids": "bitcoin,ethereum", "vs_currencies": "usd,eur"}

try:
    # 2 Send GET request
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()  # Raise an error for bad responses

    # 3 Parse JSON response
    data = response.json()

    # 4 Convert to DataFrame
    df = pd.DataFrame(data).T.reset_index()
    df.columns = ["crypto", "price_usd", "price_eur"]

    # 5 Add timestamp
    df["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 6 Save to CSV
    output_file = "crypto_prices.csv"
    df.to_csv(output_file, index=False)

    # 7 Display results
    print("=== CRYPTO DATA REPORT ===\n")
    print(df)
    print(f"\n✅ Data saved successfully as {output_file}")

except requests.exceptions.RequestException as e:
    print(f"❌ API request failed: {e}")
