from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority (DEFCON)", required=True, min_value=1, max_value=3)



def index(request):
    if 'tasks' not in request.session:
        request.session["tasks"] = []
    return render(request, 'todolist/index.html', context={
        'tasks' : request.session["tasks"],
        })


def add(request):
    """
	Adds a new task to the to-do list.

	Parameters:
	- request: The HTTP request object.

	Returns:
	- HttpResponseRedirect: If the form data is valid, the function redirects to the homepage with the updated to-do items.
	- HttpResponse: If the form data is incomplete or invalid, the function renders the 'add.html' template with the form and error message.
	"""


    # server-side validation
    if(request.method == "POST"):
        form = NewTaskForm(request.POST)    # load form data to new form object
        if(form.is_valid()):
            task = form.cleaned_data["task"]    # retrieve user data
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse('index'))   # redirects to homepage with to-do items

        else:       # incomplete form data returned with error message
            return render(request, 'todolist/add.html', context={
                "form" : form,
            })

    return render(request, 'todolist/add.html', context={
        "form" : NewTaskForm(),        # new form, for GET method
    })
