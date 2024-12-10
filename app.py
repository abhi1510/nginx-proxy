import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    service = os.environ.get("SERVICE")
    return f"{service} Service"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
