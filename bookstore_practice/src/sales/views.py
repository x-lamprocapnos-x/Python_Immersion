from django.shortcuts import render
#to protect function-based views
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'sales\home.html')

# Define a function based view - records
# Keep Protected
@login_required
def records(request):
    # Do nothing, simply display a page (more next lesson)
    return render(request, 'sales/records.html')