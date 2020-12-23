from django.shortcuts import render,HttpResponse
# manually
from home.models import *
from datetime import datetime
from django.contrib import messages
from home.form import ContactForm
import folium




# Create your views here.
def index(request):

    return render(request,"index.html")
    
def about(request):
   
    return render(request,"about.html")

def searchcity(request):

    prs=""
    tmp=""
    hum=""
    fel=""
    wnd=""
    form=ContactForm(request.POST or None)

    map=folium.Map( )
    # folium.Marker(location=[l_lat, l_long],raduis=5,tooltip=f"{city['city']}, {city['region']}, {city['country_name']}, {city['country_code']}",icon=folium.Icon(color="red")).add_to(map)
    folium.TileLayer('Mapbox Control Room').add_to(map)
    folium.TileLayer('Stamen Toner').add_to(map)
    folium.TileLayer('Stamen Terrain').add_to(map)
    folium.TileLayer('Stamen Watercolor').add_to(map)
    folium.TileLayer('CartoDB positron').add_to(map)
    folium.TileLayer('CartoDB dark_matter').add_to(map)


    if form.is_valid(): 
        instance = form.save(commit=False)
        
        locat=form.cleaned_data.get('Location')
        # print(locat)
        

        api_key='5c11e6890821b5a5c1251f5e14efe615'
        # api_key2='a06ced7eea7d6f0a7ef58b5e36105f81'

        degree_sign= u'\N{DEGREE SIGN}'

        owm=pyowm.OWM(api_key)
        # print(owm)
        mgr=owm.weather_manager()
        obs=mgr.weather_at_place(locat)
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

        if weather!=None:
            tmp=str(temperature)+'°C'
            prs=  str(pressure['press'])+'hPa'
            hum=str(humidity)+'%'
            fel=str(fls)+'°C'
            wnd=str(wind_speed)+'m/sec'

        icon=['01d','01n','02d','02n','03d','03n','04d','04n','09d','09n','10d','10n','11d','11n','13d','13n','50d','50n']
        print('Day & Time '+iTime)
        print('Weather code for '+locat+ f' is {code} ')
        # print('temperature in '+locat+ f' is {temperature}{degree_sign} C' )
        # print('Pressure in '+locat+ f' is {pressure} hPa' )
        # print(pressure['press'])
        # print('Humidity in '+locat+ f' is {humidity}%' )
        # print('temperature in '+locat+ f' {feels_like}' )
        # print('Wind Speed in '+locat+ f' is  {wind_speed} m/sec' )
        print('Wind Direction in '+locat+ f' is  {wind_dirc-273.15 :.2f}{degree_sign} C' )
        print('Minimum Temperature in '+locat+ f' is {mint}{degree_sign} C' )
        print('Maximun Temperature in '+locat+ f' is {maxt} {degree_sign} C' )
        # print('Sun rise time at '+locat+ f' is {sunrise} ' )
        print('Cloud Range in '+locat+ f' is {clouds}%' )
        print('Detailed status of '+locat+ f' is {dstatus} ')
        print('Sunrise Time  of '+locat+ f' is {sunrise} ')
        print('Sunset Time  of '+locat+ f' is {sunset} ')
        print('Human Perception of temperature at '+locat+ f' is {fls-273.15 :.2f}{degree_sign} C' )
        print('Weather id for '+locat+ f' is {id} ')

    map.add_child(folium.LayerControl())
    map=map._repr_html_()


    context={
   
    'temperature':tmp,
    'pressure':prs,
    'humidity':hum,
    'feels':fel,
    'wind_speed':wnd,
    'form':form,
    'map':map
    }

    return render(request,"searchcity.html",context)       


def contact(request):
    # return(HttpResponse("this is contact page"))  
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Form has been submitted')

    return render(request,"contact.html")  
