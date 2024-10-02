import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Create fuzzy variables
temperature = ctrl.Antecedent(np.arange(-10, 51, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
wind_speed = ctrl.Antecedent(np.arange(0, 51, 1), 'wind_speed')
weather = ctrl.Consequent(np.arange(0, 101, 1), 'weather')

# Define fuzzy membership functions for temperature
temperature['cold'] = fuzz.trimf(temperature.universe, [-10, 0, 20])
temperature['mild'] = fuzz.trimf(temperature.universe, [10, 25, 40])
temperature['hot'] = fuzz.trimf(temperature.universe, [30, 50, 50])

# Define fuzzy membership functions for humidity
humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['medium'] = fuzz.trimf(humidity.universe, [30, 50, 70])
humidity['high'] = fuzz.trimf(humidity.universe, [50, 100, 100])

# Define fuzzy membership functions for wind speed
wind_speed['slow'] = fuzz.trimf(wind_speed.universe, [0, 10, 20])
wind_speed['moderate'] = fuzz.trimf(wind_speed.universe, [10, 25, 40])
wind_speed['fast'] = fuzz.trimf(wind_speed.universe, [30, 50, 50])

# Define fuzzy membership functions for weather prediction
weather['clear'] = fuzz.trimf(weather.universe, [0, 0, 50])
weather['cloudy'] = fuzz.trimf(weather.universe, [25, 50, 75])
weather['rainy'] = fuzz.trimf(weather.universe, [50, 100, 100])

# Define fuzzy rules
rule1 = ctrl.Rule(temperature['cold'] & humidity['low'] & wind_speed['slow'], weather['clear'])
rule2 = ctrl.Rule(temperature['cold'] & humidity['high'] & wind_speed['moderate'], weather['rainy'])
rule3 = ctrl.Rule(temperature['mild'] & humidity['medium'] & wind_speed['moderate'], weather['cloudy'])
rule4 = ctrl.Rule(temperature['hot'] & humidity['high'] & wind_speed['fast'], weather['rainy'])

# Control system creation and simulation
weather_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
weather_simulation = ctrl.ControlSystemSimulation(weather_ctrl)

def predict_weather(temp, hum, wind):
    weather_simulation.input['temperature'] = temp
    weather_simulation.input['humidity'] = hum
    weather_simulation.input['wind_speed'] = wind
    weather_simulation.compute()

    return weather_simulation.output['weather']
