from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# PUT YOUR TELEGRAM BOT TOKEN HERE
BOT_TOKEN = "8772881799:AAFAg4ls62UNBJyg9b7cnTPfyvaXXzB3Hhw"

# PUT YOUR TELEGRAM CHAT ID HERE
CHAT_ID = "8391704985"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/subscribe", methods=["POST"])
def subscribe():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    zip_code = data.get("zip")

    message = f"""
New Magazine Subscriber

Name: {name}
Email: {email}
ZIP: {zip_code}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, json=payload)

    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True)
