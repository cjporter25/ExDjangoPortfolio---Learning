from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chris(request): 
    return render(request, 'jobs/home.html')
