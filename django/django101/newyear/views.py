from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    # add logic to check if newyear or not
    current_date = datetime.date.today()
    is_new_year = current_date.month == 1 and current_date.day == 1
    
    return render(request, 'newyear/index.html', {
        'is_new_year': is_new_year,
        'year': current_date.year
        })