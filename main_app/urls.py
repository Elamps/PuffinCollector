from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('puffins/', views.puffins_index, name='index'),
  path('puffins/<int:puffin_id>/', views.puffins_detail, name='detail'),
  path('puffins/create/', views.PuffinCreate.as_view(), name='puffins_create'),
  path('puffins/<int:pk>/update/', views.PuffinUpdate.as_view(), name='puffins_update'),
  path('puffins/<int:pk>/delete/', views.PuffinDelete.as_view(), name='puffins_delete'),
  path('puffins/<int:puffin_id>/add_feeding/', views.add_feeding, name='add_feeding'),

]