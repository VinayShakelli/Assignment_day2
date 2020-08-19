from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import operator


def name(requests):
    return HttpResponse('<h1>My name is Vinay Shakelli</h1>')
def number(requests):
    return HttpResponse('<h1> My number is 9888545690</h1>')

