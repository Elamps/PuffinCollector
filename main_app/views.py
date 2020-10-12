from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Puffin, Rock
from .forms import FeedingForm
# Add the following import
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Define the home view

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def puffins_index(request):
    puffins = Puffin.objects.filter(user=request.user)
    return render(request, 'puffins/index.html', {'puffins': puffins})

@login_required
def puffins_detail(request, puffin_id):
    puffin = Puffin.objects.get(id=puffin_id)
    rocks_puffin_doesnt_have = Rock.objects.exclude(id__in = puffin.rocks.all().values_list('id'))
    feeding_form = FeedingForm()
    return render(request, 'puffins/detail.html', { 
        'puffin': puffin, 'feeding_form': feeding_form,
        'rocks': rocks_puffin_doesnt_have
  })

@login_required
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


class PuffinCreate(LoginRequiredMixin, CreateView):
      model = Puffin
      fields = ['name', 'breed', 'description', 'age']
      def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class PuffinUpdate(LoginRequiredMixin, UpdateView):
      model = Puffin
    # Let's disallow the renaming of a puffin by excluding the name field!
      fields = ['breed', 'description', 'age']

class PuffinDelete(LoginRequiredMixin, DeleteView):
      model = Puffin
      success_url = '/puffins/'

class RockList(LoginRequiredMixin, ListView):
      model = Rock

class RockDetail(LoginRequiredMixin, DetailView):
  model = Rock

class RockCreate(LoginRequiredMixin, CreateView):
  model = Rock
  fields = '__all__'

class RockUpdate(LoginRequiredMixin, UpdateView):
  model = Rock
  fields = ['name', 'color']

class RockDelete(LoginRequiredMixin, DeleteView):
  model = Rock
  success_url = '/rocks/'

@login_required
def assoc_rock(request, puffin_id, rock_id):
  Puffin.objects.get(id=puffin_id).rocks.add(rock_id)
  return redirect('detail', puffin_id=puffin_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('index')
      else:
        error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)