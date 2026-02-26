from flask import Flask, send_from_directory
from routes.users import users_bp

app = Flask(__name__)

app.register_blueprint(users_bp)

@app.route("/")
def home():
    return send_from_directory("templates", "index.html")  # changed static → templates

@app.route("/users")
def users_page():
    return send_from_directory("templates", "users.html")  # changed static → templates

if __name__ == "__main__":
    app.run(debug=True)