from django.shortcuts import render
from django.conf import settings
from django.views import View



# Create your views here.
class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'index.html'
        )

class DepartureView(View):
     def get(self, request, *args, **kwargs):
        return render(
            request, 'departure.html'
        )


class TourView(View):
     def get(self, request, *args, **kwargs):
        return render(
            request, 'tour.html'
        )


