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
  path('rocks/', views.RockList.as_view(), name='rocks_index'),
  path('rocks/<int:pk>/', views.RockDetail.as_view(), name='rocks_detail'),
  path('rocks/create/', views.RockCreate.as_view(), name='rocks_create'),
  path('rocks/<int:pk>/update/', views.RockUpdate.as_view(), name='rocks_update'),
  path('rocks/<int:pk>/delete/', views.RockDelete.as_view(), name='rocks_delete'),
  path('puffins/<int:puffin_id>/assoc_rock/<int:rock_id>/', views.assoc_rock, name='assoc_rock'),
  path('accounts/signup/', views.signup, name='signup'),
]