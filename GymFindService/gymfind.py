from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual API key from Google Places or Yelp
API_KEY = 'AIzaSyCU7_7AVDj43laOFeeXenXJEWZQdE-tGqg'
# Base URL might change based on the API you choose
BASE_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

@app.route('/find_gyms', methods=['GET'])
def find_gyms():
    zipcode = request.args.get('zipcode')
    if not zipcode:
        return jsonify({'error': 'No ZIP code provided'}), 400
    
    # Convert ZIP code to coordinates (you might need another API or method for this)
    coordinates = convert_zip_to_coordinates(zipcode)
    
    if not coordinates:
        return jsonify({'error': 'Invalid ZIP code'}), 404

    # Make a request to the chosen API to find gyms
    params = {
        'location': f'{coordinates["lat"]},{coordinates["lng"]}',
        'radius': 5000,  # Adjust the radius as needed
        'type': 'gym',
        'key': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    results = response.json()

    return jsonify(results)

def convert_zip_to_coordinates(zip):
    # Placeholder function: Implement this based on how you can convert ZIP to coordinates
    return {'lat': 40.712776, 'lng': -74.005974}  # Example coordinates for New York City

if __name__ == '__main__':
    app.run(debug=True)