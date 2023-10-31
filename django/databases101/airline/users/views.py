from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

# from django.contrib.sessions.models import Session
# Sessions - 
# - useful to separate user's data
# - for ex. ecommerce store- each session can consist data about 
#   - user profile, user cart items, user checkout

# create views here
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:login'))
    else:
        return render(request, "users/home.html")
    

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            
            # create user session
            request.session['username'] = user.username

            return HttpResponseRedirect(reverse('users:index'))
        else:
            return render(request, "users/login.html", context={
                "message" : """
                            Invalid Credentials.
                            Are you sure you entered correct Username/Password ?
                            """,
            })
        
    else:
        return render(request, "users/login.html")


def logout_view(request):
    logout(request=request)

    # clear user session
    request.session.clear()

    return render(request, "users/login.html", context={
        "message" : """
                    Logged out successfully!
                    """
    })


def redirect_to_flights(request):
    return redirect(reverse('flights:index'))