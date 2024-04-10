from django.urls import path

from myhomeapp import views
from myhomeapp.views import ProductsList

urlpatterns = [
    path('main_page/', views.main_page, name='main_page'),
    path('about/', views.about, name='about'),
    path('hometable/', views.read_home_table, name='read_home_table'),
    path('prod_list/<int:client>', ProductsList.as_view(), name='p_list'),
    path('home/', views.home, name='home'),
    path('photo/', views.load_photo, name='photo'),
    path('toys_photo/', views.list_toys, name='toys_photo'),

]
