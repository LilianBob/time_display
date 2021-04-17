from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime
from datetime import date
def index(request):
    context ={
        "date": strftime("%b %d, %Y", localtime()),
        "time": strftime("%I:%M %p", localtime()),
    }
    
    return render(request, "index.html", context)

# Create your views here.
