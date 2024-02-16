from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

if __name__ == "__main__":
  app.run(debug=True)



# import json
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # In-memory data (replace with database interaction)
# data = [
#     {"id": 1, "name": "John Doe"},
#     {"id": 2, "name": "Jane Doe"},
# ]

# @app.route("/users", methods=["GET"])
# def get_users():
#     return jsonify(data)

# @app.route("/users/<int:user_id>", methods=["GET"])
# def get_user(user_id):
#     for user in data:
#         if user["id"] == user_id:
#             return jsonify(user)
#     return jsonify({"error": "User not found"}), 404

# @app.route("/users", methods=["POST"])
# def create_user():
#     new_user = request.get_json()
#     if not new_user or not new_user.get("name"):
#         return jsonify({"error": "Missing name"}), 400
#     new_user["id"] = len(data) + 1
#     data.append(new_user)
#     return jsonify(new_user), 201

# # ... (similarly for PUT and DELETE)

# if __name__ == "__main__":
#     app.run(debug=True)
