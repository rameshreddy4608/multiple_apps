from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1(request):
    return HttpResponse('<h1><marquee>This is app1 project</marquee></h1>')


def app2(request):
    return HttpResponse('<h1><marquee>This is app2 project</marquee></h1>')