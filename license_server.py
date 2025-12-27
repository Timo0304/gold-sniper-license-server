import os
from flask import Flask, request, jsonify

app = Flask(__name__)

AUTHORIZED_MACHINES = {
    "GOLD_SNIPER": [
        "5404514578303"
    ]
}

@app.route("/verify", methods=["POST"])
def verify():
    data = request.json

    bot = data.get("bot")
    machine = data.get("machine_id")

    if bot in AUTHORIZED_MACHINES and machine in AUTHORIZED_MACHINES[bot]:
        print("SERVER DEBUG → AUTHORIZED")
        return jsonify(status="AUTHORIZED")

    print("SERVER DEBUG → DENIED")
    return jsonify(status="DENIED"), 403


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render port if available
    app.run(host="0.0.0.0", port=port)

