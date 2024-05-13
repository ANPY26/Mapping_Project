from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import explorer

# Create your views here.
def explore_map(request):
    return render(request,"/Users/nikitakulkarni/Documents/MappingProj/django/MapProj/template/home.html")

def display_data(request):
    data = explorer.objects.all()
    return render(request, 'display_data.html', {'data':data})

