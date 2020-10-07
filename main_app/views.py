from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Puffin
from .forms import FeedingForm
# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect

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
    feeding_form = FeedingForm()
    return render(request, 'puffins/detail.html', { 
        'puffin': puffin, 'feeding_form': feeding_form
  })

def add_feeding(request, puffin_id):
      # create a ModelForm instance using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the puffin_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.puffin_id = puffin_id
    new_feeding.save()
  return redirect('detail', puffin_id=puffin_id)

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
