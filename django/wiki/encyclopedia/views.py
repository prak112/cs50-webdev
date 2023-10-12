from django.core import exceptions
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms

from . import util

from django.conf import settings    # for Base Directory setting
import os           # to join directory path
import subprocess   # to run CLI command for .md to .html conversion
import markdown2    # to convert Markdown to HTML
import random       # for random_page view


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def renderhtml(request, title):
    """
    Render HTML page for a given request and title.

    Args:
        request (HttpRequest): The HTTP request object.
        title (str): The title of the HTML page to render.

    Returns:
        HttpResponse: The rendered HTML page.

    Raises:
        None.
    """
    try:
        return render(request, f"encyclopedia/{title}.html", {"title": util.get_entry(title), "topic": title.upper()})
    
    except exceptions.ObjectDoesNotExist:
        # convert Markdown to HTML
        markdown_file = f"entries/{title}.md"   
        html_file = f"encyclopedia/templates/encyclopedia/{title}.html"
        cli_command = f"python -m markdown2 {markdown_file} > {html_file}"
        subprocess.run(cli_command, shell=True, check=True)
        return render(request, f"encyclopedia/{title}.html", {"title": util.get_entry(title), "topic": title.upper()})


    # if util.get_entry(title) is None:
    #         else:


# class definition for creating Form objects for new_entry & edit_entry
class NewForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'placeholder':'Title here...'}))
    content = forms.CharField(widget=forms.Textarea(attrs=
                                                    {'rows': 10, 'cols': 40, 'placeholder':'Enter Content in Markdown syntax...'}))
    submit = forms.CharField(widget=forms.widgets.Input(attrs={'type':'submit', 'value':'Submit!'}))
  

def new_entry(request):

    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"].replace(" ","")
            content = form.cleaned_data["content"]

            if util.save_entry(title, content):               
                # redirect to new entry
                return renderhtml(request, title)
            
            # return already existing entry
            else:       
                return render(request, 'encyclopedia/page_exists.html', context={'title': title})           

        # request with invalid data
        else:      
            return render(request, 'encyclopedia/new_entry.html', context={"form" : form,})
    # new request to create new entry    
    return render(request, 'encyclopedia/new_entry.html', context={'form':NewForm(),})
    


def random_page(request):
    entries = util.list_entries()
    choice = random.choice(entries)
    return HttpResponseRedirect(reverse('renderhtml', args=[choice]))



def edit_entry(request, title):
    intial_data = {
            'title' : title,
            'content': util.get_entry(title)
                }
    form = NewForm(initial=intial_data)  
    # MAJOR DEBUGGING ---
    # form.is_valid() NOT NECESSARY, form.has_changed IS NECESSARY
    # Request Type changes from POST to GET -- reasons --
        # Double-Form Resubmission -> after an error when refreshing the page, the form is submitted again
                                #  -> the browser interprets this as a GET request and hence changes the Request Type
    

    # pseudo-code 
    """
    1. fill form with initial data
    2. check if form data has changed
    3. if form data has changed, check if "POST" request
    4. if "POST" request, check if updated_form data is valid
    5. if valid, save updated form data
    6. convert Markdown to HTML
    7. redirect to renderhtml
    """ 
   
    if form.has_changed() and request.method == "POST":
        updated_form = NewForm(request.POST)
        
        if updated_form.is_valid():
            title = updated_form.cleaned_data["title"]
            content = updated_form.cleaned_data["content"]                    
            
            # convert Markdown to HTML
            markdown_file = os.path.join(settings.BASE_DIR, f"entries/{title}.md")   
            html_file = os.path.join(settings.BASE_DIR, f"templates/encyclopedia/{title}.html")
            cli_command = f"python -m markdown2 {markdown_file} > {html_file}"
            subprocess.run(cli_command, shell=True, check=True)
            
            util.save_entry(title, content)
                # with open(markdown_file, 'r') as md_file:
                #     md_content = md_file.read()
                #     html_content = markdown2.markdown(md_content)               
                # with open(html_file, 'w') as html_file:
                #     html_file.write(html_content)
            return renderhtml(request, title)
            #return HttpResponseRedirect(reverse('renderhtml', args=[title]))
        

        # render form with initial_data if invalid data /not "POST" request
        # return render(request, 'encyclopedia/edit_entry.html', context={'form': form, 'title': title})


    # else:
        # return render(request, 'encyclopedia/edit_entry.html', context={'title' : title, 'form': form})
        # return HttpResponseRedirect(reverse('new_entry'))

    


# def search(request):
#     """
#     Search for a given query and render the results.
#     """
#     if request.method == 'POST':
#         form = SearchForm(request.POST)

#         if form.is_valid():
#             query = form.cleaned_data["search"]

#             entries = util.list_entries()
#             results = []
#             for entry in entries:
#                 if query.lower() == entry.lower():
#                     return render(request, f"encyclopedia/{entry}.html", context={
#                         "title":util.get_entry(entry)
#                     })
#                 elif entry.__contains__(query):
#                     results.append(entry)
#                 else:
#                     return render(request, 'encyclopedia/notfound.html', {"title": query.upper()})
#             return render(request, 'encyclopedia/results.html', {
#                 "entries": results
#                 })