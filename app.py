from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, CI/CD!"

@app.route('/status')
def status():
    return jsonify({"status": "running", "message": "API is up and running!"})

if __name__ == "__main__":
    app.run(debug=True)
