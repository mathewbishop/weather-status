from dotenv import load_dotenv
import os
import sys
import sched
import time
import requests

load_dotenv()

version = os.getenv('VERSION')
api_key = os.getenv('WEATHER_API_KEY')
s = sched.scheduler(time.time, time.sleep)
weather_data = None


def print_slow(str, interval=.04):
    for l in str:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(interval)


def fetch_weather_data(city, state):
    print("inside func   =>    " + api_key)
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},us&units=imperial&appid={api_key}")
    return data.json()


# print_slow("Initializing... Bootstrapping WEATHER-STATUS subroutine... END OF LINE\n")
# print_slow(f"WEATHER-STATUS --version {version}, PROCESS ID 423114, Status OK... END OF LINE\n", .02)

# print_slow("Please input your location...\n")

# city = input("City: ")

# print_slow("STDIN READ... city: " + city + " was entered.    END OF LINE\n", 0.2)

# state = input("Enter State: ")

# print_slow("STDIN READ... state: " + state + " was entered.    END OF LINE\n", .02)

# print_slow(f"Requesting weather data for {city}, {state}...\n")

# weather_data = fetch_weather_data(city, state)

sample_weather_obj = {'coord': {'lon': -94.4191, 'lat': 39.2461}, 'weather': [{'id': 721, 'main': 'Haze', 'description': 'haze', 'icon': '50n'}], 'base': 'stations', 'main': {'temp': -1.7, 'feels_like': -14.08, 'temp_min': -2.99, 'temp_max': -0.4, 'pressure': 1025, 'humidity': 78}, 'visibility': 8047, 'wind': {'speed': 10.36, 'deg': 360}, 'clouds': {'all': 100}, 'dt': 1613443997, 'sys': {'type': 1, 'id': 4246, 'country': 'US', 'sunrise': 1613394555, 'sunset': 1613433275}, 'timezone': -21600, 'id': 4395052, 'name': 'Liberty', 'cod': 200}

def do_something(sc): 
    print_slow("Getting weather data...\n")
    # do your stuff
    s.enter(5, 1, do_something, (sc,))

s.enter(5, 1, do_something, (s,))
s.run()
# Main loop, run continuously until Ctrl + C
while True:
    try:
        print_slow("first loop\n")
    except KeyboardInterrupt:
        sys.exit()