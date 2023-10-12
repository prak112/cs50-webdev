from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("renderhtml/<str:title>", views.renderhtml, name="renderhtml"),   # renders all listed titles and notfound pages
    path("new_entry", views.new_entry, name="new_entry"),
    path("random_page", views.random_page, name="random_page"),
    path("edit_entry/<str:title>", views.edit_entry, name="edit_entry"),
    path("search", views.search, name="search")
]
