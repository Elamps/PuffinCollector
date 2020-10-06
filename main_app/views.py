from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
class Puffin:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

puffins = [
  Puffin('Lolo', 'tabby', 'foul little demon', 3),
  Puffin('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Puffin('Raven', 'black tripod', '3 legged Puffin', 4)
]

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def puffins_index(request):
    return render(request, 'puffins/index.html', {'puffins': puffins}) 