from dotenv import load_dotenv
import os
import sys
import time
import requests

load_dotenv()

api_key = os.getenv('WEATHER_API_KEY')

def print_slow(str):
    for l in str:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(.05)


# 1 call per minute

def fetch_weather_data(city, state):
    print("inside func   =>    " + api_key)
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},us&units=imperial&appid={api_key}")
    return data.json()


# city = input("Enter City: ")

# print_slow("STDIN READ... city: " + city + " was entered.    END OF LINE\n")

# state = input("Enter State: ")

# print_slow("STDIN READ... state: " + state + " was entered.    END OF LINE\n")

# print_slow("Initializing...\n")

# print_slow("WEATHER STATUS READ...\n")

# fetch_weather_data(city, state)

# Main loop, run continuously until Ctrl + C
while True:
    try:
        print_slow("test")
    except KeyboardInterrupt:
        sys.exit()