from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ''

    Characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        Characters.extend(list(map(lambda x:x.upper(), Characters)))

    if request.GET.get('number'):
        Characters.extend(list('1234567890'))

    if request.GET.get('special'):
        Characters.extend(list('!@#$%^&*()'))

    length = int(request.GET.get('length', 12))

    for x in range(length):
        thepassword = thepassword+random.choice(Characters)
    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
