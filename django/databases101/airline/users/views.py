from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

#TODO-
# create sessions
# create hyperlink to all flights



# create views here
def index(request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("login"))
        else:
            return render(request, "users/home.html")
    

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
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
    return render(request, "users/login.html", context={
        "message" : """
                    Logged out successfully!
                    """
    })    