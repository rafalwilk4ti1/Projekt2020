#Weather Forecast 
from tkinter import *
import requests
from PIL import ImageTk, Image
from io import BytesIO


#api key 8416a2c3ce097fa15a8378890441ff65

#Define a window
root = Tk()
root.title('Weather Forecast')
root.iconbitmap('C:/Users/rafal/Desktop/THEArtOFDoing GUI apps/Exercises/original.ico')
root.geometry('400x400')
root.resizable(0,0)

#Configuration - colors,font etc.
sky_color = '#76c3ef'
grass_color = '#aad207'
output_color = '#dcf0fb'
input_color = '#ecf2ac'
large_font = ('SimSun',14)
small_font = ('SimSun',10)

#Define functions
def search():
    #Download datas from the website using API
    global response
    #declare our api key and url website which we use 
    url = 'http://api.openweathermap.org/data/2.5/weather'
    api_key = '8416a2c3ce097fa15a8378890441ff65'

    #if to choose oppurtunity to look for by a name city or zip code
    if search_method.get() == 1:
        #creating dictionary/ could be tuple and propably list, to get neccesery information using requests.request 
        querystring = {'q':first_entry.get(),'appid':api_key,'units':'metric'}
    elif search_method.get()==2:
        #the same function but here we use zip code
        querystring = {'zip':first_entry.get(),'appid': api_key,'units':'metric'}

    #connect to url, and getting datas
    response = requests.request("GET", url, params=querystring)
    #information which we got, they are in directory now
    response = response.json()
    
    #Weather in my town 
    #{'coord': {'lon': 21.15, 'lat': 51.4}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 
    # 'base': 'stations', 'main': {'temp': 276.55, 'feels_like': 271.91, 'temp_min': 275.93, 'temp_max': 277.04, 'pressure': 1015, 'humidity': 83},
    #  'visibility': 10000, 'wind': {'speed': 3.96, 'deg': 108}, 'clouds': {'all': 100}, 'dt': 1609679678, 
    # 'sys': {'type': 3, 'id': 2000265, 'country': 'PL', 'sunrise': 1609656009, 'sunset': 1609684759}, 'timezone': 3600, 'id': 760778, 'name': 'Radom', 'cod': 200}

    get_weather()
    get_photo()

def get_weather():
    #Creating variables to get the most neccesesary information from directories
    #first line
    city_name = response['name']
    city_lat = str(response['coord']['lat'])
    city_lon = str(response['coord']['lon'])
    
    #second line
    city_weather = str(response['weather'][0]['main']) #
    city_weather_2 = str(response['weather'][0]['description'])
    #third line
    city_temperature = response['main']['temp']
    #forth line
    city_feels = str(response['main']['feels_like'])
    #fifth line
    city_temp_min = str(response['main']['temp_min'])
    #sixth line
    city_temp_max = str(response['main']['temp_max'])
    #seventh line
    city_humidity = str(response['main']['humidity'])
    

    display_on_app(city_name,city_lat,city_lon,city_weather,city_weather_2,city_temperature,city_feels,city_temp_min,city_temp_max,city_humidity)


def display_on_app(city,lat,lon,weather,weather2,temperature,feels,min,max,humidity):
    local_encoding = 'cp850'
    city_label.config(text=str(city)+"("+str(lat)+","+str(lon)+")")
    weather_label.config(text="Weather: "+str(weather)+" , "+str(weather2))
    temp_label.config(text="Temperature: "+str(temperature)+" C\xb0")
    feels_label.config(text="Feels like: "+str(feels)+" C\xb0")
    mintemp_label.config(text="Min. Temperature: "+str(min)+" C\xb0")
    maxtemp_label.config(text="Max. Temperature: "+str(max)+" C\xb0")
    humidity_label.config(text="Humidity: "+str(humidity)+" C\xb0")
    
def get_photo():
    global img
    # #eight line
    city_photo = response['weather'][0]['icon'] 
    print(city_photo)
    #convert url adress for changable to set option "change photo"available 
    url = 'http://openweathermap.org/img/wn/{icon}.png'.format(icon=city_photo)
    #download our picture
    icon_request = requests.get(url, stream=True)
    
    #Turn into a form tkinter/python can use 
    img_data = icon_request.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    #set picture in our app
    photo_label.config(image=img)



#Create major frames
sky_frame = Frame(root,height=250,bg=sky_color)
grass_frame = Frame(root,bg=grass_color)
sky_frame.pack(fill=BOTH,expand=True)
grass_frame.pack(fill=BOTH,expand=True)

#Creating Labelframes inside major frame
output_labelframe = LabelFrame(sky_frame,width=325,height=225,bg=output_color)
input_labelframe = LabelFrame(grass_frame,width=325,bg=input_color)
output_labelframe.pack(pady=30)
output_labelframe.pack_propagate(0)
input_labelframe.pack(pady=20)

#Setting our output frame 
city_label = Label(output_labelframe,text='City: ',bg=output_color,font=large_font)
weather_label = Label(output_labelframe,text='Weather: ',bg=output_color,font=small_font)
temp_label = Label(output_labelframe,text='Temperature: ',bg=output_color,font=small_font)
feels_label = Label(output_labelframe,text='Feels: ',bg=output_color,font=small_font)
mintemp_label = Label(output_labelframe,text='Temp. Min: ',bg=output_color,font=small_font)
maxtemp_label = Label(output_labelframe,text='Temp. Max.: ',bg=output_color,font=small_font)
humidity_label = Label(output_labelframe,text='Humidity: ',bg=output_color,font=small_font)
photo_label = Label(output_labelframe,text='Photo: ',bg=output_color,font=small_font)

city_label.pack(pady=8)
weather_label.pack()
temp_label.pack()
feels_label.pack()
mintemp_label.pack()
maxtemp_label.pack()
humidity_label.pack()
photo_label.pack(pady=8)

#Setting our input frame
first_entry = Entry(input_labelframe,width=20,font=large_font)
submit_button = Button(input_labelframe,text="Submit",bg=input_color,font=large_font,command=search)

submit_button.grid(padx=10,pady=(10,0),row=0,column=1)
first_entry.grid(padx=10,pady=(10,0),row=0,column=0)

search_method = IntVar()
search_method.set(1)

radio_1 = Radiobutton(input_labelframe,text='Search by a city',bg=input_color,font=small_font,variable=search_method,value=1)
radio_2 = Radiobutton(input_labelframe,text='Search by a zip code',bg=input_color,font=small_font,variable=search_method,value=2)
radio_1.grid(row=1,column=0,pady=1,padx=5)
radio_2.grid(row=1,column=1,pady=1,padx=5)


#Run root's mainloop
root.mainloop()
