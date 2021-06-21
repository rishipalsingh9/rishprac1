from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def learn_django(request):
    return HttpResponse('<h1>Hello Django</h1>')

def learn_var(request):
    a = '<h1>Hello to Variables</h1>'
    return HttpResponse(a)


def learn_math(request):
    a = 29 + 9450 * 5390 - 850
    return HttpResponse(a)

def learn_format(request):
    a = 29 + 9450 * 5390 - 850
    return HttpResponse(f'The Total Sum To Recieve in GBP {a}')
