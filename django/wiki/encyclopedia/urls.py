from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.renderhtml, name="renderhtml"),   # renders all listed titles and notfound pages
    path("<str:q>", views.search, name="search"),
]
