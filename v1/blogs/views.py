from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import operator

def drinks(requests):
    return HttpResponse('<h1>Drink 5L water everday to keep your body hydrated</h1>')
def foods(requests):
    return HttpResponse('<h1> Dont eat junk food. Stay healthy</h1>')

