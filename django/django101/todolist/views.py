from django.shortcuts import render

# Create your views here.

tasks = ["Buy Milk", "Clean Litterboxes", "Feed Cats", "Become Cat"]
def index(request):
    return render(request, 'todolist/index.html', context={'tasks' : tasks})