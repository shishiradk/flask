from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory data store
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400
    new_id = max(u["id"] for u in users) + 1 if users else 1
    user = {"id": new_id, "name": data["name"]}
    users.append(user)
    return jsonify(user), 201

@app.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    if not data or "name" not in data:
        return jsonify({"error": "Name is required"}), 400
    user["name"] = data["name"]
    return jsonify(user)

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True) 