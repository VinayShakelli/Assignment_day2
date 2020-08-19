from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
import operator
#from templates import wcount
#from wcount import 'home.html','aboutus.html'
def home(requests):
    return render(requests,'wcount/home.html',{'name': 'Vinay Shakelli'})
def aboutus(requests):
    return render(requests,'wcount/aboutus.html',{ 'userid': '058'})
