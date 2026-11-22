from flask import Flask, jsonify, request

app = Flask(__name__)

orders_db = [
    {"id": 1, "customer": "Carlos", "sku": "SKU-0", "quantity": 1, "amount": 99.90, "status": "APPROVED"}
]


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/ready", methods=["GET"])
def ready():
    return jsonify({"status": "ready"}), 200


@app.route("/orders", methods=["GET", "POST"])
def orders():
    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        new_order = {
            "id": len(orders_db) + 1,
            "customer": data.get("customer", "Cliente"),
            "sku": data.get("sku", "SKU-1"),
            "quantity": data.get("quantity", 1),
            "amount": data.get("amount", 0.0),
            "status": "CREATED",
        }
        orders_db.append(new_order)
        return jsonify({"message": "Pedido criado com sucesso", "order": new_order}), 201

    return jsonify({"total": len(orders_db), "orders": orders_db}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
