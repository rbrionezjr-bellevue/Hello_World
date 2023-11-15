# DSC 510
# Week 12
# Final Project Week 12
# Author Ruben Brionez Jr
# 11/19/2023

# Change Log
# Change :1
# Changes Made: Created Program
# Date of Change: 11/13/2023
# Author: Ruben Brionez Jr
# Change Approved by: Ruben Brionez Jr
# Date Moved to Production: 11/19/2023

import requests
from urllib.error import HTTPError
import json


def get_lat_long_zip(zip_code, country_code, api_key):
    api_call = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={api_key}"
    response = requests.get(api_call)
    api_data = response.json()
    lat = api_data["lat"]
    lon = api_data["lon"]
    #  print(f"Your latitude is {lat} and longitude is {lon} ")
    return lat, lon


def get_lat_lon_city(city_name, state_code, country_code):
    api_call = (f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}"
                f"&limit={5}&appid={api_key}")
    response = requests.get(api_call)
    api_data = response.json()
    lat = api_data[0]["lat"]
    lon = api_data[0]["lon"]
    return lat, lon


def get_current_weather(lat, lon):
    current_call = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(current_call)
    current_data = response.json()
    weather = current_data["weather"][0]["description"]
    weather = weather.title()
    temp = current_data["main"]["temp"]
    f_temp = int((((temp - 273.15)*9/5) + 32))
    c_temp = int((temp - 273.15))
    k_temp = temp
    print(f"You can expect {weather}")
    print(f"{f_temp}{degree_sign}F")
    return weather, f_temp, c_temp, k_temp


api_key = "1aa4ba963fc3d2784de2be6a2065c2d3"
degree_sign = u'\N{DEGREE SIGN}'


def main():
    print("***Welcome to the Weather App***")
    choice = ""
    while True:
        choice = input("Do you want to search by 'city' or 'zip code'? Enter 'quit' to exit:  ")
        choice = choice.lower()
        if choice == 'city':
            city_name = input("Please enter your city: ")
            state_code = input("Please enter the two letter abbreviation for state:  ")
            country_code = input("Please enter the country code: ")
            get_lat_lon_city(city_name, state_code, country_code)
            lat = get_lat_lon_city(city_name, state_code, country_code)[0]
            lon = get_lat_lon_city(city_name, state_code, country_code)[1]
            get_current_weather(lat, lon)
        elif choice == 'zip code':
            zip_code = int(input("Please enter your zip code: "))
            country_code = input("Please enter your two letter country code: ")
            lat = get_lat_long_zip(zip_code, country_code, api_key)[0]
            lon = get_lat_long_zip(zip_code, country_code, api_key)[1]
            get_current_weather(lat, lon)
        elif choice == "quit":
            print("Thanks for stopping by!")
            break
        else:
            print("Wrong!")


if __name__ == "__main__":
    main()