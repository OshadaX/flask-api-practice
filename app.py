from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/api/hello')
def hello():
    return jsonify({'message': 'Hellooo, World!'})

if __name__ == '__main__':
    app.run(debug=True)