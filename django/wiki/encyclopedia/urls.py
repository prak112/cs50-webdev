from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("renderhtml/<str:title>", views.renderhtml, name="renderhtml"),   # renders all listed titles and notfound pages
    # path("<str:q>", views.search, name="search"),
    path("new_entry", views.new_entry, name="new_entry"),
    path("edit_entry/<str:title>", views.edit_entry, name="edit_entry"),
]
