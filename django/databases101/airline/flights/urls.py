from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("flights/<int:flight_id>", views.flight, name="flight"),
    path("<int:flight_id>/add_passenger", views.add_passenger, name="add_passenger"),
]