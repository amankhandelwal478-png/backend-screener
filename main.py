from flask import Flask, jsonify
import requests

app = Flask(__name__)

DHAN_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzc1NjIxNTM4LCJpYXQiOjE3NzU1MzUxMzgsInRva2VuQ29uc3VtZXJUeXBlIjoiU0VMRiIsIndlYmhvb2tVcmwiOiIiLCJkaGFuQ2xpZW50SWQiOiIxMTAzNTI1NDM1In0.Fb3drY5hUrkMg1Unrn35tOSyiutaZe8Qh5vTkhuADO1kMmP1Y6TQOvpgLpqFvSg6ndK_upqJPWdTXJziEaTbNQ"

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

    try:
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

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/')
def home():
    return "Backend Running ✅"

if __name__ == '__main__':
    app.run()
