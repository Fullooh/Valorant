from flask import Flask, jsonify  # Add jsonify to handle JSON responses
import requests  # Add requests to make API calls
# Comment out Firebase imports temporarily
# from services.firebase_admin import get_firestore_db
# from services.database_service import init_db

app = Flask(__name__)

@app.route('/')
def home():
    # Temporarily skip Firebase connection
    # db = get_firestore_db()
    return 'Backend is working without Firebase!'

# Route to fetch player data using Henrik's Unofficial Valorant API
@app.route('/api/valorant/player/<name>/<tag>', methods=['GET'])
def get_player_data(name, tag):
    try:
        # Encode the name and tag to handle special characters (e.g., "#")
        api_url = f'https://api.henrikdev.xyz/valorant/v1/account/{name}/{tag}'

        # Make a GET request to Henrik's Unofficial Valorant API
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            player_data = response.json()
            return jsonify(player_data), 200
        else:
            return jsonify({'error': f'Failed to fetch player data: {response.content.decode()}'}), response.status_code

    except Exception as e:
        return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
