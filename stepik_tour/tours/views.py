from django.http import Http404
from django.shortcuts import render
from django.views import View

from tours.data import (departures, tours, title, subtitle, description)


# Create your views here.
class MainView(View):
    def get(self, request):
        index_tours = dict(((tour_id, tour) for (tour_id, tour) in tours.items() if tour_id <= 6))

        return render(
            request, 'index.html',
            {'index_tours': index_tours,
             'title': title,
             'subtitle': subtitle,
             'description': description,
             'departures': departures, }
        )


class DepartureView(View):
    def get(self, request, departure: str):
        if departure not in departures.keys():
            raise Http404('Страница не найдена')

        departure_tours = dict(((tour_id, tour) for (tour_id, tour) in tours.items() if tour['departure'] == departure))

        tours_price = list((tour['price']) for tour in departure_tours.values())
        tours_nights = list((tour['nights']) for tour in departure_tours.values())

        price_min = min(tours_price)
        price_max = max(tours_price)
        nights_max = max(tours_nights)
        nights_min = min(tours_nights)

        tourcount = len(departure_tours)

        return render(
            request, 'departure.html',
            {'title': title,
             'departure_tours': departure_tours,
             'departure': departures[departure],
             'departures': departures,
             'price_min': price_min,
             'price_max': price_max,
             'nights_min': nights_min,
             'nights_max': nights_max,
             'tourcount': tourcount,

             }

        )


class TourView(View):
    def get(self, request, id: int):
        if id not in tours.keys():
            raise Http404('Страница не найдена')

        departure = tours[id]['departure']

        return render(
            request, 'tour.html',
            {'tour': tours[id],
             'departure': departures[departure],
             'departures': departures}

        )
