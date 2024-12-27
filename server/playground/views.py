from django.shortcuts import render
from django.http import HttpResponse

def cal():
    x = 1
    y = 4
    return x+y


def say_hello(req):

    x = cal()
    y= 2
    z=3

    return render(req, 'hello.html', {'name': 'Mosh'})
