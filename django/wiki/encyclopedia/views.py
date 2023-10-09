from django.shortcuts import render

from . import util


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
        return render(request, 'encyclopedia/notfound.html', {"title": title.upper()})
    return render(request, f"encyclopedia/{title}.html",
                  {"title": util.get_entry(title)})


