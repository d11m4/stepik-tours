from django.shortcuts import render
from django.http import (Http404, HttpResponse)
from django.conf import settings
from django.views import View
from tours.data import (departures, tours, title, subtitle, description)
from django.urls import resolve


    

# Create your views here.
class MainView(View):
    def get(self, request):
        f_tours = dict(((k, v) for (k, v) in tours.items() if k <=6 ))
        return render(
            request, 'index.html',
            {'f_tours' : f_tours,
            'title' : title,
            'subtitle' : subtitle,
            'description' : description,
            'departures' : departures, }
        )

class DepartureView(View):
     def get(self, request, departure:str):
        f_tours = dict(((k, v) for (k, v) in tours.items() if v['departure'] == departure)) 
        f_price = list((v['price']) for (k, v) in f_tours.items())
        f_nights = list((v['nights']) for (k, v) in f_tours.items())
        pricemin = min(f_price)
        pricemax = max(f_price)
        nightsmax = max(f_nights)
        nightsmin = min(f_nights)

        tourcount = len(f_tours)


            
        return render(
            request, 'departure.html',
            { 'title' : title,
            'f_tours' : f_tours,
            'departure' : departures[departure],
            'departures' : departures,
            'pricemin' : pricemin,
            'pricemax' : pricemax,
            'nightsmin' : nightsmin,
            'nightsmax' : nightsmax,
            'tourcount' : tourcount,
            
            }

        )


class TourView(View):

     def get(self, request, id:int):
        
        departure=tours[id]['departure']
        return render(
            request, 'tour.html',
            {'tour' : tours[id],
            'departure' : departures[departure],
            'departures' : departures }

        )


