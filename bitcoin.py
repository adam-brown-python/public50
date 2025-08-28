token = "4d088d8197f8bad817a87ab40ad48071bb3142f83f8b8985a60156a97d031fc4"
import requests
import sys
try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Missing command-line argument")

    else:
        o = requests.get(f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={token}")
        t = o.json()
        
        x = t["data"]["priceUsd"]
        total = (float(x) * float(sys.argv[1]))
        print(f"${total:,.4f}")
except requests.RequestException:
    pass