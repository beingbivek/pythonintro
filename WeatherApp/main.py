import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

API_KEY = 'ff9424ddef9982068d41346eb332f16f'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    try:
        params = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", "Failed to retrieve data. Please check your network connection and try again.")
        return None

def show_weather():
    city_name = city_entry.get()
    if not city_name:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return
    
    weather_data = get_weather(city_name)
    if weather_data:
        update_weather_info(weather_data)

def update_weather_info(weather_data):
    city = weather_data['name']
    country = weather_data['sys']['country']
    temp = weather_data['main']['temp']
    weather = weather_data['weather'][0]['description'].title()
    icon_code = weather_data['weather'][0]['icon']
    icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"

    city_label.config(text=f"{city}, {country}")
    temp_label.config(text=f"{temp}°C")
    weather_label.config(text=weather)
    
    # Load weather icon
    icon_image = Image.open(requests.get(icon_url, stream=True).raw)
    icon_photo = ImageTk.PhotoImage(icon_image)
    icon_label.config(image=icon_photo)
    icon_label.image = icon_photo

def clear_weather_info():
    city_label.config(text="")
    temp_label.config(text="")
    weather_label.config(text="")
    icon_label.config(image="")

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.config(bg="#d3e0ea")

# Create and place widgets
city_entry = tk.Entry(root, font=("Helvetica", 16), width=20)
city_entry.pack(pady=20)

search_button = tk.Button(root, text="Get Weather", command=show_weather)
search_button.pack(pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_weather_info)
clear_button.pack(pady=5)

city_label = tk.Label(root, font=("Helvetica", 20), bg="#d3e0ea")
city_label.pack(pady=10)

temp_label = tk.Label(root, font=("Helvetica", 20), bg="#d3e0ea")
temp_label.pack(pady=5)

weather_label = tk.Label(root, font=("Helvetica", 20), bg="#d3e0ea")
weather_label.pack(pady=5)

icon_label = tk.Label(root, bg="#d3e0ea")
icon_label.pack(pady=10)

# Start the main loop
root.mainloop()
