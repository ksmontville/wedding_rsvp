from django.urls import path
from . import views

app_name = 'rsvp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('menu/', views.menu, name='menu'),
    path('events/', views.events, name='events'),
    path('travel/', views.travel, name='travel'),
    path('registry/', views.registry, name='registry'),
    path('faqs/', views.faqs, name='faqs'),
    path('thank_you', views.thank_you, name='thank_you'),
    path('password', views.password, name='password')
]
