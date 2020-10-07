from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Puffin
# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Define the home view

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def puffins_index(request):
    puffins = Puffin.objects.all()
    return render(request, 'puffins/index.html', {'puffins': puffins})

def puffins_detail(request, puffin_id):
    puffin = Puffin.objects.get(id=puffin_id)
    return render(request, 'puffins/detail.html', { 'puffin': puffin })

class PuffinCreate(CreateView):
      model = Puffin
      fields = '__all__'

class PuffinUpdate(UpdateView):
      model = Puffin
    # Let's disallow the renaming of a puffin by excluding the name field!
      fields = ['breed', 'description', 'age']

class PuffinDelete(DeleteView):
      model = Puffin
      success_url = '/puffins/'
