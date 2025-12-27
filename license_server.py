from flask import Flask, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Format: machine_id: {"bot": bot_name, "expiry": "YYYY-MM-DD"}
AUTHORIZED_MACHINES = {
    "5404514578303": {
        "bot": "GOLD_SNIPER",
        "expiry": "2025-01-27"  # YYYY-MM-DD
    },
    # Add more machines as needed
}

@app.route("/verify", methods=["POST"])
def verify():
    data = request.json
    bot = data.get("bot")
    machine = data.get("machine_id")

    # Check if machine exists
    if machine in AUTHORIZED_MACHINES:
        record = AUTHORIZED_MACHINES[machine]

        # Check bot name
        if record["bot"] != bot:
            return jsonify(status="DENIED", reason="Bot name mismatch"), 403

        # Check expiry
        expiry_date = datetime.strptime(record["expiry"], "%Y-%m-%d")
        if datetime.now() > expiry_date:
            return jsonify(status="DENIED", reason="License expired"), 403

        # Authorized
        return jsonify(status="AUTHORIZED")

    return jsonify(status="DENIED", reason="Machine not authorized"), 403

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

