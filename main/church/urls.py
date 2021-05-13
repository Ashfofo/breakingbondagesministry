from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contactus', views.contactus, name='contactus'),
    path('donate', views.donate, name='donate'),
    path('visit', views.visit, name='visit'),
    path('partner', views.partner, name='partner'),
    path('bio', views.bio, name='bio'),
    path('about', views.about, name='about'),
    path('index', views.index, name='index'),

]