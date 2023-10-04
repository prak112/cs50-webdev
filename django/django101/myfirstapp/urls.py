from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),    # default page view
    path("<str:text>", views.pagetext, name="pagetext"),
    path("pagehtml/<str:text>", views.pagehtml, name="pagehtml"),
    path("page1", views.page1, name="page1"),
    path("page2", views.page2, name="page2"),   
]