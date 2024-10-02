from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serve the HTML page

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    temperature = float(data['temperature'])
    humidity = float(data['humidity'])
    wind_speed = float(data['wind_speed'])

    # Detailed prediction logic based on temperature, humidity, and wind speed
    if temperature > 30:
        if humidity < 50:
            prediction = "Sunny"
        elif 50 <= humidity <= 70:
            prediction = "Hot and Partly Cloudy"
        else:
            prediction = "Very Humid and Hot"
    elif 20 <= temperature <= 30:
        if humidity < 40:
            prediction = "Pleasant"
        elif 40 <= humidity <= 70:
            if wind_speed > 15:
                prediction = "Breezy and Partly Cloudy"
            else:
                prediction = "Comfortable"
        else:
            prediction = "Overcast and Humid"
    else:  # temperature < 20
        if wind_speed > 10:
            if humidity > 80:
                prediction = "Windy and Rainy"
            else:
                prediction = "Cool and Windy"
        elif humidity > 80:
            prediction = "Rainy"
        else:
            prediction = "Cool and Clear"

    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
