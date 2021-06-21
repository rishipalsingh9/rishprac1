from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def my_love(request):
    a = 'what is love'
    return HttpResponse(f'{a}, Baby dont hurt me')