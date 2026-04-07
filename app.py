from flask import Flask, jsonify
import requests

app = Flask(__name__)

DHAN_TOKEN = "PASTE_YOUR_TOKEN_HERE"

# 👉 Yahan apni stock list daal (jitni badi chaho)
stocks = [
    "RELIANCE", "TCS", "INFY", "HDFCBANK", "ICICIBANK",
    "SBIN", "LT", "ITC", "AXISBANK", "KOTAKBANK",
    "ADANIENT", "BAJFINANCE", "HCLTECH", "WIPRO"
]

@app.route('/data')
def get_data():
    url = "https://api.dhan.co/v2/marketfeed/ltp"

    headers = {
        "access-token": DHAN_TOKEN,
        "Content-Type": "application/json"
    }

    result = {}

    # 🔥 IMPORTANT: 50-50 ka batch bana
    for i in range(0, len(stocks), 50):
        chunk = stocks[i:i+50]

        payload = {
            "NSE_EQ": chunk
        }

        res = requests.post(url, headers=headers, json=payload)
        data = res.json()

        if "data" in data:
            result.update(data["data"])

    return jsonify(result)

@app.route('/')
def home():
    return "Backend Running ✅"

if __name__ == '__main__':
    app.run()
