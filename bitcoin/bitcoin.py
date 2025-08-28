import requests
import sys
try:
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    elif sys.argv[1].isalpha():
        sys.exit("Missing command-line argument")

    else:
        o = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        t = o.json()
        x = t["bpi"]["USD"]["rate_float"]
        total = (float(x) * float(sys.argv[1]))
        print(f"${total:,.4f}")
except requests.RequestException:
    pass

