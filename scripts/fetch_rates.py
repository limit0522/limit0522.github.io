import requests, json, os
SUPPORTED = ['GBP', 'EUR', 'AUD', 'USD', 'CNY', 'INR', 'VND', 'THB', 'IDR']
BASE_URL = "https://api.exchangerate-api.com/v4/latest/"
os.makedirs("api_data", exist_ok=True)
for base in SUPPORTED:
    try:
        res = requests.get(f"{BASE_URL}{base}", timeout=10)
        if res.status_code == 200:
            data = res.json()
            filtered = {"base": base, "date": data.get("date"), "rates": {k: v for k, v in data['rates'].items() if k in SUPPORTED}}
            with open(f"api_data/{base}.json", 'w') as f:
                json.dump(filtered, f, indent=2)
            print(f"Updated {base}.json")
    except: pass
