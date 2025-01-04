# Create your views here.
from time import sleep

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")


def waiting(request):
    sleep(10)
    return HttpResponse("Hello, sleep world.")
