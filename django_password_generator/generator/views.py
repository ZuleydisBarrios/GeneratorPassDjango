from codecs import xmlcharrefreplace_errors
from operator import length_hint
import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnpqrstuvxyz')
    generated_password=''
    
    length=int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('-_?.<>\!@#$%^&&*()+'))
    
    if request.GET.get('number'):
        characters.extend(list('1234567890'))


    for char in range(length):
        generated_password += random.choice(characters)

        
    return render(request, 'generator/password.html', {'password': generated_password})