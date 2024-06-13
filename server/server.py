from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location')
def get_location():
    response = jsonify({
        'location': util.get_location()
    })
    response.headers.add('Access-Control', '*')
    return response

if __name__ == "__main__":
    print("Initiating Flask Server...")
    app.run()