from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400
    
    # Dummy weather data for demonstration purposes
    weather_data = {
        'city': city,
        'temperature': '22°C',
        'description': 'Clear sky'
    }
    
    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))