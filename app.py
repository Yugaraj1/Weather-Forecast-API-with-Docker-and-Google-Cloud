from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv('WEATHER_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form['city']
        weather_data = get_weather(city)
    return render_template('index.html', weather_data=weather_data)

def get_weather(city):
    url = f'http://api.weatherstack.com/current?access_key={API_KEY}&query={city}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'current' in data:
            return {
                'temperature': data['current']['temperature'],
                'description': data['current']['weather_descriptions'][0],
                'humidity': data['current']['humidity'],
                'wind_speed': data['current']['wind_speed'],
                'city': data['location']['name'],
                'country': data['location']['country']
            }
    return None

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 8080)), debug=True)

    
