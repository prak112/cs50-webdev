from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Passenger

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {"flights": Flight.objects.all()})


def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    passengers = flight.passengers.all()
    non_passengers = Passenger.objects.exclude(flight=flight).all()

    return render(request, "flights/flight.html", context={
        "flight": flight,
        "passengers": passengers,
        "non_passengers": non_passengers,
        })


def add_passenger(request, flight_id):
    if request.method == "POST":
        # retrieve flight details
        flight = Flight.objects.get(pk=flight_id)

        # retrieve passenger_id from POST request
        passenger_id = int(request.POST["passenger"])
        passenger = Passenger.objects.get(pk=passenger_id)
        
        # add passenger to flight
        passenger.flight.add(flight)

        # redirect to modified flight page
        return HttpResponseRedirect(reverse("flight", args=(flight_id,)))

