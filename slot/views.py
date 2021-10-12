
from django.http.response import HttpResponse
from django.shortcuts import render
import requests
from datetime import datetime as dt


# Create your views here.
def home(request):
    now = dt.now()
    s = now.strftime("%d-%m-%Y")
 
    pincode=request.GET.get('pincode', 110030)
    date=request.GET.get('date',s )


    print(date)
   
    print(pincode)
  

    url=f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={date}'
    
    data=requests.get(url).json()
    
    payload=data['sessions']

    # print(payload)
    context={'data': payload}
    print(payload)
    return render(request, 'home.html', context)