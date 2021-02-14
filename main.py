from dotenv import load_dotenv
import os
import sys
import time
import requests

load_dotenv()

def print_slow(str):
    for l in str:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(.05)



city = input("Enter City: ")

print_slow("STDIN READ... city: " + city + " was entered.    END OF LINE\n")

state = input("Enter State: ")

print_slow("STDIN READ... state: " + state + " was entered.    END OF LINE\n")

print_slow("Initializing...\n")

print_slow("WEATHER STATUS READ...\n")