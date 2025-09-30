
# api/weather.py
from flask import Flask, jsonify, make_response
import requests
import os

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    # Development: "*" ; production: ganti dengan domain kamu mis. "https://namakamu.vercel.app"
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET,OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

@app.route("/", methods=["GET", "OPTIONS"])
def weather_proxy():
    try:
        url = "https://meteojuanda.id/share/api-semeru/aws.json"
        # Optional: override URL via env var
        url = os.environ.get("SEMERU_SOURCE_URL", url)
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        return make_response(jsonify(data), 200)
    except requests.exceptions.RequestException as e:
        # Beri debug message (akan terlihat di logs Vercel)
        return make_response({"error": "fetch failed", "detail": str(e)}, 502)
