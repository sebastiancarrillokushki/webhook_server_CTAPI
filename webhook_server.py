from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(silent=True)
        if data:
            tipo = data.get("transactionType", "").lower()
            if tipo == "devolucion":
                ruta_archivo = os.path.abspath("devolucion_trx.json")
            else:
                ruta_archivo = os.path.abspath("estado_trx.json")
            with open(ruta_archivo, "w") as f:
                json.dump(data, f)
    except Exception as e:
        pass  # Ignora cualquier error
    return "", 200  # Siempre responde 200

@app.route("/get-estado", methods=["GET"])
def get_estado():
    ruta_archivo = os.path.abspath("estado_trx.json")
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo) as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify({"error": "No data"}), 404

@app.route("/get-devolucion", methods=["GET"])
def get_devolucion():
    ruta_archivo = os.path.abspath("devolucion_trx.json")
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo) as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify({"error": "No data"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port) 