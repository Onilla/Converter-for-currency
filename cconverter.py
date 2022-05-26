import json
import requests
currency = input().lower()
r = requests.get(f"http://www.floatrates.com/daily/{currency}.json").json()
currency_dict = {}
if currency != "usd":
    usd = r["usd"]["rate"]
    currency_dict["usd"] = usd
if currency != "eur":
    eur = r["eur"]["rate"]
    currency_dict["eur"] = eur
while True:
    currency_for_purchase = input().lower()
    if currency_for_purchase == "":
        print()
        break
    else:
        total = input()
        if currency_for_purchase not in currency_dict:
            currency_dict[currency_for_purchase] = r[currency_for_purchase]["rate"]
            print(f"""Checking the cache...
Sorry, but it is not in the cache!
You received {round(float(total) * currency_dict[currency_for_purchase],2)} {currency_for_purchase.upper()}.""")
        else:
            print(f"""Checking the cache...
Oh! It is in the cache!
You received {round(float(total) * currency_dict[currency_for_purchase], 2)} {currency_for_purchase.upper()}.""")

