from django.shortcuts import render
from django.http import HttpResponse

# # Create your views here.
def index(request):
    return render(request, 'myfirstapp/index.html')

# def index(request):
#     return HttpResponse("Hello World! This is awesome!")

def page1(request):
    return HttpResponse("This is Page 1")

def page2(request):
    return HttpResponse("Wow! we moved to Page 2")


def pagetext(request, text):        
    """
    Generate a response containing the input text in the url
    
    Args:
        request: The request object.
        text: The input text.
    
    Returns:
        HttpResponse: The response containing the capitalized text.
    """
    return HttpResponse(f"This is {text.capitalize()}")


def pagehtml(request, text):
    """
    Generate html content containing the input text in the url
    
    Args:
        request: The request object.
        text: The input text.
    
    Returns:
        HTML page: Content including the capitalized text with other HTML content.
    """
    return render(request, 'myfirstapp/content.html', 
                  context={'text': text.capitalize()}
                  )