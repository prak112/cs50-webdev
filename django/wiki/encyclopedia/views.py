#from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

from . import util

import subprocess   # to run CLI command for .md to .html conversion
import random

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
    if not util.get_entry(title):
        return render(request, 'encyclopedia/not_found.html', {"title": title.upper()})
    return render(request, f"encyclopedia/{title}.html",
                  {"title": util.get_entry(title)})



class NewForm(forms.Form):
    # search = forms.CharField(label="Search")
    title = forms.CharField(label="Title", widget=forms.TextInput(attrs={'placeholder':'Title here...'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 40, 'placeholder':'Enter Content in Markdown syntax...'}))
    submit = forms.CharField(widget=forms.widgets.Input(attrs={'type':'submit', 'value':'Submit!'}))
  

def new_entry(request):

    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"].replace(" ","")
            content = form.cleaned_data["content"]

            if util.save_entry(title, content):               
                # convert Markdown to HTML
                markdown_file = f"entries/{title}.md"   
                html_file = f"encyclopedia/templates/encyclopedia/{title}.html"
                cli_command = f"python -m markdown2 {markdown_file} > {html_file}"
                subprocess.run(cli_command, shell=True, check=True)

                # redirect to new entry
                return renderhtml(request, title) 
            # return already existing entry
            else:       
                return render(request, 'encyclopedia/page_exists.html', context={'title': title})           

        else:   # request with invalid data   
            return render(request, 'encyclopedia/new_entry.html', context={
                            "form" : form,
                        })
    # new request to create new entry    
    return render(request, 'encyclopedia/new_entry.html', context={
                    'form':NewForm(),
                })
    


def random_page(request):
    entries = util.list_entries()    
    return renderhtml(request, random.choice(entries))







# def edit_entry(request, title):

#     return render(request, f"entries/{title}.md")





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