from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

from . import util

class NewForm(forms.Form):
    # search = forms.CharField(label="Search")
    title = forms.CharField(label="Title")
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":"25", "cols":"50"}))


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
    

def new_entry(request):

    # if request.method == 'POST':
    #     form = NewForm(request.POST)
    #     if form.is_valid():
    #         title = form.cleaned_data["title"]
    #         content = form.cleaned_data["content"]
            

        return render(request, 'encyclopedia/new_entry.html', context={
            # "form" : form,
    })
    
