import datetime
from colorama import Fore, Style

def print_weather_data(weather_data, state, print_slow):
    current_date = Fore.CYAN + datetime.date.today().strftime("%b %d %Y") + Style.RESET_ALL
    current_time = Fore.CYAN + datetime.datetime.now().strftime("%H:%M:%S") + Style.RESET_ALL
    
    # Extract relevant info from weather_data into vars
    try:
        weather_data_time = Fore.CYAN + datetime.datetime.fromtimestamp(weather_data['dt']).strftime("%H:%M:%S") + Style.RESET_ALL
    except KeyError:
        weather_data_time = "UNKNOWN"
    try:
        city = Fore.CYAN + weather_data['name'] + Style.RESET_ALL
    except KeyError:
        city = "UNKNOWN"
    try:
        latitude = Fore.CYAN + str(weather_data['coord']['lat']) + Style.RESET_ALL
    except KeyError:
        latitude = "UNKNOWN"
    try:
        longitude = Fore.CYAN + str(weather_data['coord']['lon']) + Style.RESET_ALL
    except KeyError:
        longitude = "UNKNOWN"
    try:
        weather_description = Fore.CYAN + weather_data['weather'][0]['description'] + Style.RESET_ALL
    except KeyError:
        weather_description = "UNKNOWN"
    try: 
        temp = Fore.CYAN + str(weather_data['main']['temp']) + Style.RESET_ALL
    except KeyError:
        temp = "UNKNOWN"
    try:
        temp_feel = Fore.CYAN + str(weather_data['main']['feels_like']) + Style.RESET_ALL
    except KeyError:
        temp_feel = "UNKNOWN"
    try:
        min_observed_temp = Fore.CYAN + str(weather_data['main']['temp_min']) + Style.RESET_ALL
    except KeyError:
        min_observed_temp = "UNKNOWN"
    try:
        max_observed_temp = Fore.CYAN + str(weather_data['main']['temp_max']) + Style.RESET_ALL
    except KeyError:
        max_observed_temp = "UNKNOWN"
    try:
        pressure = Fore.CYAN + str(weather_data['main']['pressure']) + Style.RESET_ALL
    except KeyError:
        pressure = "UNKNOWN"
    try:
        humidity = Fore.CYAN + str(weather_data['main']['humidity']) + Style.RESET_ALL
    except KeyError:
        humidity = "UNKNOWN"
    try:
        wind_speed = Fore.CYAN + str(weather_data['wind']['speed']) + Style.RESET_ALL
    except KeyError:
        wind_speed = "UNKNOWN"
    try:
        wind_direction = Fore.CYAN + str(weather_data['wind']['deg']) + Style.RESET_ALL
    except KeyError:
        wind_direction = "UNKNOWN"
    try:
        wind_gust = Fore.CYAN + str(weather_data['wind']['gust']) + Style.RESET_ALL
    except KeyError:
        wind_gust = "UNKNOWN" 
    try:
        percentage_cloud_cover = Fore.CYAN + str(weather_data['clouds']['all']) + Style.RESET_ALL
    except KeyError:
        percentage_cloud_cover = "UNKNOWN"
    try:
        last_1hr_rain = Fore.CYAN + str(weather_data['rain']['1h']) + Style.RESET_ALL
    except KeyError:
        last_1hr_rain = "UNKNOWN"
    try:
        last_3hr_rain = Fore.CYAN + str(weather_data['rain']['3h']) + Style.RESET_ALL
    except KeyError:
        last_3hr_rain = "UNKNOWN"
    try:
        last_1hr_snow = Fore.CYAN + str(weather_data['snow']['1h']) + Style.RESET_ALL
    except KeyError:
        last_1hr_snow = "UNKNOWN" 
    try:
        last_3hr_snow = Fore.CYAN + str(weather_data['snow']['3h']) + Style.RESET_ALL
    except KeyError:
        last_3hr_snow = "UNKNOWN"
    try:
        sunrise = Fore.CYAN + datetime.datetime.fromtimestamp(weather_data['sys']['sunrise']).strftime("%H:%M:%S") + Style.RESET_ALL
    except KeyError:
        sunrise = "UNKNOWN"
    try:
        sunset = Fore.CYAN + datetime.datetime.fromtimestamp(weather_data['sys']['sunset']).strftime("%H:%M:%S") + Style.RESET_ALL
    except KeyError:
        sunset = "UNKNOWN"
                                                                                            

    # Location
    print_slow(f"LOCATION: {city}, {state}; COORDINATES: {latitude}, {longitude}\n")
    # Date
    print_slow(f"Today is {current_date}\n")
    # Time
    print_slow(f"Current time is {current_time}\n")
    # Description
    print_slow(f"Current weather description at this location is: {weather_description}\n")
    # Temp
    print_slow("TEMPERATURE ...\n")
    print_slow(f"It is currently {temp} degrees FAHRENHEIT, and feels like {temp_feel} degrees FAHRENHEIT\n")
    print_slow(f"As of {weather_data_time}, the minimum observed temperature in this area was {min_observed_temp} FAHRENHEIT, and the maximum observed temperature was {max_observed_temp} FAHRENHEIT\n")
    # Pressure
    print_slow(f"The atmospheric pressure is {pressure} hPa\n")
    # Humidity
    print_slow(f"The humidity percentage is {humidity} percent\n")
    # Wind 
    if wind_gust != "UNKNOWN":
        print_slow(f"The wind speed is {wind_speed} miles per hour, at {wind_direction} degrees. Wind gusts of {wind_gust} miles per hour were reported\n")
    else:
        print_slow(f"The wind speed is {wind_speed} miles per hour, at {wind_direction} degrees\n")
    # Clouds
    print_slow(f"The percentage of cloud cover is {percentage_cloud_cover} percent\n")
    # Rain
    if last_1hr_rain != "UNKNOWN":
        print_slow(f"In the last hour it has rained {last_1hr_rain} millimeters\n")
    if last_3hr_rain != "UNKNOWN":
        print_slow(f"In the last 3 hours it has rained {last_3hr_rain} millimeters\n")
    # Snow
    if last_1hr_snow != "UNKNOWN":
        print_slow(f"In the last hour it has snowed {last_1hr_snow} millimeters\n")
    if last_3hr_snow != "UNKNOWN":
        print_slow(f"In the last 3 hours it has snowed {last_3hr_snow} millimeters\n")
    # Sunrise
    print_slow(f"SUNRISE AT: {sunrise} local time\n")
    # Sunset
    print_slow(f"SUNSET AT: {sunset} local time\n")