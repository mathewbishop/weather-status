from dotenv import load_dotenv
import os
import sys
import sched
import time
import datetime
import requests

load_dotenv()

version = os.getenv('VERSION')
api_key = os.getenv('WEATHER_API_KEY')
s = sched.scheduler(time.time, time.sleep)
weather_data = None


def print_slow(str, interval=.03):
    for l in str:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(interval)


def fetch_weather_data(city, state):
    print("inside func   =>    " + api_key)
    data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},us&units=imperial&appid={api_key}")
    return data.json()

def print_weather_data(weather_data, print_slow):
    current_date = datetime.date.today().strftime("%b %d %Y")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    
    # Extract relevant info from weather_data into vars
    try:
        weather_data_time = datetime.datetime.fromtimestamp(weather_data['dt']).strftime("%H:%M:%S")
    except KeyError:
        weather_data_time = "UNKNOWN"
    try:
        city = weather_data['name']
    except KeyError:
        city = "UNKNOWN"
    try:
        latitude = weather_data['coord']['lat']
    except KeyError:
        latitude = "UNKNOWN"
    try:
        longitude = weather_data['coord']['lon']
    except KeyError:
        longitude = "UNKNOWN"
    try: 
        temp = weather_data['main']['temp']
    except KeyError:
        temp = "UNKNOWN"
    try:
        temp_feel = weather_data['main']['feels_like']
    except KeyError:
        temp_feel = "UNKNOWN"
    try:
        min_observed_temp = weather_data['main']['temp_min']
    except KeyError:
        min_observed_temp = "UNKNOWN"
    try:
        max_observed_temp = weather_data['main']['temp_max']
    except KeyError:
        max_observed_temp = "UNKNOWN"
    try:
        pressure = weather_data['main']['pressure']
    except KeyError:
        pressure = "UNKNOWN"
    try:
        humidity = weather_data['main']['humidity']
    except KeyError:
        humidity = "UNKNOWN"
    try:
        wind_speed = weather_data['wind']['speed']
    except KeyError:
        wind_speed = "UNKNOWN"
    try:
        wind_direction = weather_data['wind']['deg']
    except KeyError:
        wind_direction = "UNKNOWN"
    try:
        wind_gust = weather_data['wind']['gust']
    except KeyError:
        wind_gust = "UNKNOWN" 
    try:
        percentage_cloud_cover = weather_data['clouds']['all']
    except KeyError:
        percentage_cloud_cover = "UNKNOWN"
    try:
        last_1hr_rain = weather_data['rain']['1h']
    except KeyError:
        last_1hr_rain = "UNKNOWN"
    try:
        last_3hr_rain = weather_data['rain']['3h']
    except KeyError:
        last_3hr_rain = "UNKNOWN"
    try:
        last_1hr_snow = weather_data['snow']['1h']
    except KeyError:
        last_1hr_snow = "UNKNOWN" 
    try:
        last_3hr_snow = weather_data['snow']['3h']
    except KeyError:
        last_3hr_snow = "UNKNOWN"
    try:
        sunrise = datetime.datetime.fromtimestamp(weather_data['sys']['sunrise']).strftime("%H:%M:%S")
    except KeyError:
        sunrise = "UNKNOWN"
    try:
        sunset = datetime.datetime.fromtimestamp(weather_data['sys']['sunset']).strftime("%H:%M:%S")
    except KeyError:
        sunset = "UNKNOWN"
                                                                                            

    # Location
    print_slow(f"LOCATION: {city}; COORDINATES: {latitude}, {longitude}\n")
    # Date
    print_slow(f"DATE: {current_date}\n")
    # Time
    print_slow(f"CURRENT TIME IS: {current_time}\n")
    # Temp
    print_slow("TEMPERATURE..\n")
    print_slow(f"It is currently {temp} degrees, and feels like {temp_feel}.\n")
    print_slow(f"As of {weather_data_time}, the minimum observed temperature in this area was {min_observed_temp}, and the maximum observed temperature was {max_observed_temp}.\n")
    # Pressure
    print_slow(f"The atmospheric pressure is {pressure} hPa.\n")
    # Humidity
    print_slow(f"The humidity percentage is {humidity}.\n")
    # Wind 
    if wind_gust != "UNKNOWN":
        print_slow(f"Wind speed is {wind_speed} miles per hour, at {wind_direction} degrees. Wind gusts of {wind_gust} miles per hour reported.\n")
    else:
        print_slow(f"Wind speed is {wind_speed} miles per hour, at {wind_direction} degrees.\n")
    # Clouds
    print_slow(f"The percentage of cloud cover is {percentage_cloud_cover}%.\n")
    # Rain
    if last_1hr_rain != "UNKNOWN":
        print_slow(f"In the last hour it has rained {last_1hr_rain} millimeters.\n")
    if last_3hr_rain != "UNKNOWN":
        print_slow(f"In the last 3 hours it has rained {last_3hr_rain} millimeters.\n")
    # Snow
    if last_1hr_snow != "UNKNOWN":
        print_slow(f"In the last hour it has snowed {last_1hr_snow} millimeters.\n")
    if last_3hr_snow != "UNKNOWN":
        print_slow(f"In the last 3 hours it has snowed {last_3hr_snow} millimeters.\n")
    # Sunrise
    print_slow(f"SUNRISE AT: {sunrise}.\n")
    # Sunset
    print_slow(f"SUNSET AT: {sunset}.\n")


# Initialize
print_slow("Initializing... Bootstrapping WEATHER-STATUS subroutine... END OF LINE\n")
print_slow(f"WEATHER-STATUS --version {version}, PROCESS ID 423114, Status OK... END OF LINE\n")

print_slow("Please input your location...\n")

city = input("City: ")

print_slow("STDIN READ... city: " + city + " was entered.    END OF LINE\n")

state = input("Enter State: ")

print_slow("STDIN READ... state: " + state + " was entered.    END OF LINE\n")

print_slow(f"Requesting weather data for {city}, {state}...\n")

weather_data = fetch_weather_data(city, state)


prev_weather_update_time = time.time()
# Main loop, run continuously until Ctrl + C
while True:
    try:
        if time.time() - prev_weather_update_time > 60:
            weather_data = fetch_weather_data(city, state)
            print_slow("REQUESTING UPDATED WEATHER DATA... STANDBY\n")
            time.sleep(1)
            print_slow("WEATHER DATA UPDATED REQUEST STATUS: OK\n")
            prev_weather_update_time = time.time()
        else:
            print_weather_data(weather_data, print_slow)
    except KeyboardInterrupt:
        sys.exit()