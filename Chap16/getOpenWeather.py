#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.
import logging
logging.disable(logging.CRITICAL) # Uncomment to disable debug messages
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s- %(levelname)s- %(message)s')
logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s- %(levelname)s- %(message)s')

APPID = '5f932fae3adb7636e6c65c273ad97dca'

import json, requests, sys

# Compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, state abbreviationn')
    sys.exit()
location = ','.join(sys.argv[1:])
logging.debug('Location entered is (%s)' %location)


# Download the JSON data from OpenWeatherMap.org's API.
url = 'https://api.openweathermap.org/data/2.5/forecast?q=%s&APPID=%s' %(location, APPID)
logging.debug('Site url is (%s)' %url)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.

weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']

print('\nCurrent weather in %s:' %(location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print('Wind Speed: ', w[0]['wind']['speed'])
for thirdHour in range(1, 37):
    print('\nIn %d hours:' %(thirdHour * 3))
    print(w[thirdHour]['weather'][0]['main'], '-', w[thirdHour]['weather'][0]['description'])
    print('Wind Speed: ', w[thirdHour]['wind']['speed'])
print()
