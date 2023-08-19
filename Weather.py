#Add your own appid in APPID part while requesting for api which is the first line of try block
#To get appid visit website http://api.openweathermap.org
#To know the working of weather appication refer to the demo video provided in main branch "Weather demo.mp4"
from tkinter import *
import requests
import json
from tkinter import messagebox
root = Tk()
root.title("Weather")
root.iconbitmap("weather.ico")
root.geometry("193x170")
root.minsize(193,170)
root.maxsize(193,170)
root.resizable(False,False)

E = Entry(root)
E.grid(row = 0, column = 0,padx=33)

def details():
  place = str(E.get())
  E.delete(0,END)
  if place == '':
     messagebox.showerror('Weather','Empty value')
  else:
    try:
       api_request = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={place}&APPID='paste your appid here')
       api =  json.loads(api_request.content)
       city = api['name']
       tempr = api['main']['temp']
       feels = api['main']['feels_like']
       pressure = api['main']['pressure']
       humidity = api['main']['humidity']
       visibility = api['visibility']
       wind = api['wind']['speed']
    except Exception as e:
       messagebox.showerror("Weather","Invalid Entry")

    L1 = Label(root,text = city,font = ("Helvicta",15),padx=45)
    L1.grid(row = 2,column = 0)
 
    L = Label(root,text ='Temperature(Celsius) ' + str(round(tempr - 273.15)) + '\n' + 'Feels like(Celsius) ' + str(round(feels - 273.15)) + '\n' +
            'Pressure(Pascal) ' + str(pressure) + '\n' + 'Humidity(Percent) ' + str(humidity)
            + '\n' + 'Visibility(meter) ' + str(visibility) + '\n' + 'Wind speed(m/s) ' + str(wind)) 
    L.grid(row = 3,column = 0)

            
B = Button(root, text= "Click", command = details).grid(row = 1, column = 0)


root.mainloop()
