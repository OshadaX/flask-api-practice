from flask import Blueprint, jsonify, request   # line 1

users_bp = Blueprint("users", __name__)         # line 2

users = [                                        # line 3
    {"id": 1, "name": "Alice", "role": "developer"},
    {"id": 2, "name": "Bob", "role": "designer"},
    {"id": 3, "name": "Charlie", "role": "manager"},
]

# ─── READ ALL ─────────────────────────────────────────────────────

@users_bp.route("/api/users", methods=["GET"])  # line 4
def get_users():
    return jsonify(users)

# ─── READ ONE ─────────────────────────────────────────────────────

@users_bp.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

# ─── CREATE ───────────────────────────────────────────────────────

@users_bp.route("/api/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = {
        "id": users[-1]["id"] + 1,
        "name": data["name"],
        "role": data["role"],
    }
    users.append(new_user)
    return jsonify(new_user), 201

# ─── UPDATE ───────────────────────────────────────────────────────

@users_bp.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    user["name"] = data.get("name", user["name"])
    user["role"] = data.get("role", user["role"])
    return jsonify(user)

# ─── DELETE ───────────────────────────────────────────────────────

@users_bp.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    users.remove(user)
    return jsonify({"message": f"User {user_id} deleted"})