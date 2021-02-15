from dotenv import load_dotenv
import os
import sys
import time
import requests

load_dotenv()

version = os.getenv('VERSION')
api_key = os.getenv('WEATHER_API_KEY')
weather_data = None


def print_slow(str, interval=.05):
    for l in str:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(interval)


def fetch_weather_data(city, state):
    print("inside func   =>    " + api_key)
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},us&units=imperial&appid={api_key}")
    return data.json()


print_slow("Initializing... Bootstrapping WEATHER-STATUS subroutine... END OF LINE\n")
print_slow(f"WEATHER-STATUS --version {version}, PROCESS ID 423114, Status OK... END OF LINE\n", .02)

print_slow("Please input your location...\n")

city = input("City: ")

print_slow("STDIN READ... city: " + city + " was entered.    END OF LINE\n", 0.2)

state = input("Enter State: ")

print_slow("STDIN READ... state: " + state + " was entered.    END OF LINE\n", .02)

print_slow(f"Requesting weather data for {city}, {state}...\n")

weather_data = fetch_weather_data(city, state)

# Main loop, run continuously until Ctrl + C
while True:
    try:
        
    except KeyboardInterrupt:
        sys.exit()