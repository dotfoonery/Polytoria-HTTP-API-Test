## Import Deps
from flask import Flask, request, jsonify
## Init flask app
app = Flask(__name__)
@app.route("/get-user/<user_id>")
def get-user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
## 6.47
if __name__ == "__main__":
    app.run(debug=True)