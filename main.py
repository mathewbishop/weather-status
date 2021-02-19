from dotenv import load_dotenv
import os
import sys
import time
import datetime
import requests
from colorama import init
from termcolor import colored
from print_weather_data import print_weather_data

# For colors on Windows
init()

load_dotenv()

version = os.getenv('VERSION')
api_key = os.getenv('WEATHER_API_KEY')
weather_data = None


def print_slow(str, interval=.08, color='white'):
    text = colored(str, color)
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(interval)


def fetch_weather_data(city, state):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},us&units=imperial&appid={api_key}")
    # res = requests.get(f"http://httpbin.org/status/404")
    if not res.ok:
        print_slow(f"WEATHER DATA REQUEST FAILURE ... STATUS {res.status_code}\n", .05, 'red')
        print_slow("RE-INITIATING REQUEST ... STANDBY\n", .05, 'green')
        time.sleep(30)
        fetch_weather_data(city, state)
    else:
        print_slow("WEATHER DATA UPDATED ... STATUS OK\n")
        return res.json()



# Initialize
print_slow("Initializing ... Bootstrapping WEATHER-STATUS subroutine ... END OF LINE\n", .03)
print_slow(f"WEATHER-STATUS --version {version}, PROCESS ID {os.getpid()}, STATUS OK ... END OF LINE\n", .03)

print_slow("Please input your location:\n", .04)

city = input("City: ")

print_slow("STDIN READ ... city: " + city + " was entered.    END OF LINE\n", .02)

state = input("Enter State: ")

print_slow("STDIN READ... state: " + state + " was entered.    END OF LINE\n", .02)

print_slow(f"Requesting weather data for {city}, {state} ...\n", .05)

weather_data = fetch_weather_data(city, state)


prev_weather_update_time = time.time()
# Main loop, run continuously until Ctrl + C
while True:
    try:
        # Update the weather data roughly every 2 minutes
        if time.time() - prev_weather_update_time > 120:
            print_slow("REQUESTING WEATHER DATA UPDATE ... STANDBY    END OF LINE\n")
            weather_data = fetch_weather_data(city, state)
            prev_weather_update_time = time.time()
        else:
            print_weather_data(weather_data, state, print_slow)
    except KeyboardInterrupt:
        sys.exit()
