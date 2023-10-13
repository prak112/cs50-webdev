from django.core import exceptions
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django import forms

from . import util
from . import forms

from django.conf import settings    # for Base Directory setting
import os           # to join directory path
# import subprocess   # to run CLI command for .md to .html conversion
import markdown2    # to convert Markdown to HTML
import random       # for random_page view



def index(request):

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
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

    # convert Markdown to HTML
    markdown_file = os.path.join(settings.BASE_DIR, f"entries\\{title}.md")   
    html_file = os.path.join(settings.BASE_DIR, f"encyclopedia\\templates\\encyclopedia\\{title}.html")
    
    with open (markdown_file, "r") as md_file:
        markdown_conent = md_file.read()
        html_content = markdown2.markdown(markdown_conent)
    with open (html_file, "w") as html_file:
        html_file.write(html_content)
    
    return render(request, 'encyclopedia/entry_template.html', context={'html_content':html_content, 'title': title})



def new_entry(request):
    if request.method == 'POST':
        form = forms.NewForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"].replace(" ","")
            content = form.cleaned_data["content"]

            if title in util.list_entries():       # return already existing entry
                return render(request, 'encyclopedia/page_exists.html', context={'title': title}) 
            
            else:   # redirect to new entry
                util.save_entry(title, content)
                return HttpResponseRedirect(reverse('renderhtml', args=[title]))
          
        else:    # request with invalid data
            return render(request, 'encyclopedia/new_entry.html', context={"form" : form,})
    # new request to create new entry    
    return render(request, 'encyclopedia/new_entry.html', context={'form':forms.NewForm(),})
    


def random_page(request):
    entries = util.list_entries()
    choice = random.choice(entries)
    return HttpResponseRedirect(reverse('renderhtml', args=[choice]))



def edit_entry(request, title):
    intial_data = {
            'title' : title,
            'content': util.get_entry(title)
                }
    form = forms.NewForm(initial=intial_data)  
    
    # --- MAJOR DEBUGGING --- #
    """
    # form.is_valid() NOT NECESSARY, form.has_changed IS NECESSARY
    # Request Type changes from POST to GET -- reason --
        # ERROR -> Double-Form Resubmission 
            # -> after an error when refreshing the page, form is submitted again
            #  -> browser interprets this as a GET request and hence changes request Type
        # Resolution -  
            # -> Clear cache if any. 
            # -> Change browser to incognito mode.
            # -> ALWAYS open browser from command line.
    """
    
    # PSEUDO-code 
    """
    1. fill form with initial data
    2. check if form data has changed
    3. if form data has changed, check if "POST" request
    4. if "POST" request, check if updated_form data is valid
    5. if valid, save updated form data
    6. convert Markdown to HTML
    7. redirect to renderhtml
    """ 
   
    if form.has_changed():
        updated_form = forms.NewForm(request.POST)
        
        if updated_form.is_valid():
            title = updated_form.cleaned_data["title"]
            content = updated_form.cleaned_data["content"]                              
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('renderhtml', args=[title]))
        
    # render form with initial_data if invalid data /not "POST" request
    return render(request, 'encyclopedia/edit_entry.html', context={'form': form, 'title' : title,})
    



def search(request):
    """
    Search for a given query and render the results.
    """
    form = forms.SearchForm(request.GET)

    if form.is_valid():
        query = form.cleaned_data["search_term"]
        entries = util.list_entries()
        results = []
        for entry in entries:
            if entry.lower() == str(query).lower():
                return HttpResponseRedirect(reverse('renderhtml', args=[entry]))
            elif entry.lower().__contains__(str(query).lower()):
                results.append(entry)
        if results:   # appended results lists
            return render(request, 'encyclopedia/search.html', {"results": results, "query": query})
        else:   # if no results
            return render(request, 'encyclopedia/not_found.html', {"title": query})
    else:   # return search form if invalid data
        return render(request, 'encyclopedia/search.html', {"form": form})