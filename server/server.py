from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location')
def get_location():
    response = jsonify({
        'location': util.get_location()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/home')
def home():
    return "hi"

@app.route('/predict_prices', methods = ['POST'])
def predict_prices():
    try:
        total_sqft = request.form['total_sqft']
        location = request.form['location']
        bhk = request.form['bhk']
        bath = request.form['bath']

        print(f"Received data - Total Sqft: {total_sqft}, Location: {location}, BHK: {bhk}, Bath: {bath}")

        response = jsonify({
            'estimated_price': util.estimated_price(location, total_sqft, bhk, bath)
        })
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    print("Initiating Flask Server...")
    util.load_saved()
    app.run(port = 5001)