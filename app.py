from flask import Flask, request, jsonify
from bd import Itens

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route("/itens", methods=['GET'])
def getItens():
    return Itens


@app.route("/itens/create", methods=['POST'])
def creatItens():
    iten = request.json
    Itens.append(iten)
    return jsonify(message="Roupa cadastrada com sucesso", iten=iten)


@app.route("/itens/<id>", methods=['GET'])
def showItem(id):
    try:
        id = int(id)
    except ValueError:
        return jsonify({"error": "ID invalid"}), 400

    item = next((item for item in Itens if item["id"] == int(id)), None)

    if item:
        return jsonify(item), 200
    else:
        return jsonify({"error": "Item not found"}), 404


@app.route("/itens/<id>", methods=['DELETE'])
def deleteItem(id):
    try:
        id = int(id)
    except ValueError:
        return jsonify({"error": "ID invalid"}), 400
    
    item = next((item for item in Itens if item["id"] == id), None)

    if item:
        Itens.remove(item)
        return Itens
    else:
        return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
