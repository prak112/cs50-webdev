from django.shortcuts import render

from .models import Airport, Flight

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {"flights": Flight.objects.all()})