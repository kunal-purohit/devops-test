from flask import Flask
from datetime import datetime, timezone

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/health", methods=["GET"])
def handle_get():
    return {
        "status": "ok",
        "service": "ecs-demo",
        "timestamp": datetime.now(timezone.utc),
    }


if __name__ == "__main__":
    app.run()
