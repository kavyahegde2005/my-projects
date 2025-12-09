from tkinter import Tk, Label, Button, Entry
import requests

def get_weather():
    city = entry2.get()
    api_key = "7bf94696c65981ce265d1d0afc2f5603"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()
        result = result["main"]["temp"]
        result = result - 273.15
        weather_label.config(text=f"Temperature: {round(result)}")

root = Tk()
root.title("Weather")
root.geometry("500x500")

mylabel1 = Label(root, text="Weather")
mylabel1.pack(pady=20)

mylabel2 = Label(root, text="Enter Your City")
mylabel2.pack(pady=20)

entry2 = Entry(root)
entry2.pack(pady=20)

button = Button(root, text="Get", command=get_weather)
button.pack(pady=20)

weather_label = Label(root, text="")
weather_label.pack(pady=20)

root.mainloop()
