import pyowm
from pyowm.utils import timestamps
import time
from datetime import timedelta, datetime
# import matplotlib.pyplot as plt
from PIL import ImageTk,Image
from collections import namedtuple

api_key='5c11e6890821b5a5c1251f5e14efe615'
# api_key2='a06ced7eea7d6f0a7ef58b5e36105f81'

degree_sign= u'\N{DEGREE SIGN}'

owm=pyowm.OWM(api_key)
# print(owm)
mgr=owm.weather_manager()
features=["code","id","AvgTemp","MaxTemp","MinTemp","Pres","Humd","Wspd","WDir","SunRis","SunSet"]
Daily=namedtuple("Daily",features)

place=models.CharField(max_length=20)
 
obs=mgr.weather_at_place(place)
weather=obs.weather



iTime=time.asctime(time.localtime(time.time()))
temperature=weather.temperature(unit='celsius')['temp']
pressure=weather.pressure
humidity=weather.humidity
mint=weather.temp.get('temp_min')
maxt=weather.temp.get('temp_max')
fls=weather.temp.get('feels_like')

# feels_like=weather.feels_like
wind_speed=weather.wind().get('speed')  
wind_dirc=weather.wind().get('deg')

clouds=weather.clouds
dstatus=weather.detailed_status
sunrise =weather.sunrise_time(timeformat='iso')
sunset=weather.sunset_time(timeformat='iso')
code=weather.weather_code
id=weather.weather_icon_name

icon=['01d','01n','02d','02n','03d','03n','04d','04n','09d','09n','10d','10n','11d','11n','13d','13n','50d','50n']
print('Day & Time '+iTime)
print('Weather code for '+place+ f' is {code} ')
print('temperature in '+place+ f' is {temperature}{degree_sign} C' )
print('Pressure in '+place+ f' is {pressure} hPa' )
print('Humidity in '+place+ f' is {humidity}%' )
# print('temperature in '+place+ f' {feels_like}' )
print('Wind Speed in '+place+ f' is  {wind_speed} m/sec' )
print('Wind Direction in '+place+ f' is  {wind_dirc-273.15 :.2f}{degree_sign} C' )
print('Minimum Temperature in '+place+ f' is {mint}{degree_sign} C' )
print('Maximun Temperature in '+place+ f' is {maxt} {degree_sign} C' )
# print('Sun rise time at '+place+ f' is {sunrise} ' )
print('Cloud Range in '+place+ f' is {clouds}%' )
print('Detailed status of '+place+ f' is {dstatus} ')
print('Sunrise Time  of '+place+ f' is {sunrise} ')
print('Sunset Time  of '+place+ f' is {sunset} ')
print('Human Perception of temperature at '+place+ f' is {fls-273.15 :.2f}{degree_sign} C' )
print('Weather id for '+place+ f' is {id} ')

# if id in icon:
#     while True:
#         image='icons/' + id +'.png'
#         img=Image.open(image)
#         plt.imshow(img)
#         plt.pause(50)

# forecaster = mgr.forecast_at_place(place, '3h')
# forecast = forecaster.forecast
# weather_list = forecast.weathers
# print("\n\n------------------------------forecasting for 5 days--------------------")

# print("\n\n")
# print('Three hours forecast (Times are in GMT):')
# for weather in weather_list:
#     temp = weather.temperature(unit='celsius')['temp']
#     status=weather.detailed_status
#     print((weather.reference_time('iso'), f'Temperature: {temp}{degree_sign}C   Detailed status:  {status}' ))

# print("To get the weather userchoice hours from the current time .\n")

# dy=int(input("enter days interval (supported 4 days) : "))
# hr=int(input("enter hrs interval : "))
# time = datetime.now() + timedelta(days=dy, hours=hr) #max=4,min hr=1{for the time interval}
# if (dy>=5 or hr>=24):
#     print("out of scope")
# else:    
#     print(time)
#     weather = forecaster.get_weather_at(time)
#     temperature = weather.temperature(unit='fahrenheit')['temp']
#     print(f'The temperature at {time.strftime("%Y-%m-%d %H:%M:%S")} is {temperature}{degree_sign}F')

#     time = timestamps.tomorrow(dy,hr)#day,hrs
#     weather = forecaster.get_weather_at(time)
#     temperature = weather.temperature(unit='fahrenheit')['temp']
#     print(f'The temperature at {time} is {temperature}{degree_sign}F')

# print("-------------------------WEEK DETAILS OF YOUR CITY----------------------")
# print("Clear sky this Week "+str(forecaster.will_have_clear()))
# print("Rain this Week "+str(forecaster.will_have_rain()))
# print("Fog this Week "+str(forecaster.will_have_fog()))
# print("Hurricane this Week "+str(forecaster.will_have_hurricane()))
# print("Snow this Week "+str(forecaster.will_have_snow()))
# print("Storm this Week "+str(forecaster.will_have_storm()))
# print("Tornado this Week "+str(forecaster.will_have_tornado()))
# print("Cloudss this Week "+str(forecaster.will_have_clouds()))










   


