from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/hello')
def get():
    return "HI"

if __name__ == "__main__":
    print("Initiating Flask Server...")
    app.run()