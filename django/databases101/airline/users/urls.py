from django.urls import path, include

from . import views

app_name = "users"

urlpatterns = [
    path('', views.index, name="index"),
    path('login',views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('redirect-to-flights', views.redirect_to_flights, name="redirect_to_flights")
]

