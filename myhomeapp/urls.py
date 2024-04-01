from django.urls import path

from myhomeapp import views

urlpatterns = [
    path('main_page/', views.main_page, name='main_page'),
    path('about/', views.about, name='about'),
    path('hometable/', views.read_home_table, name='read_home_table'),

]
