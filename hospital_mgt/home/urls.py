from django.urls import path, include
from . import views     #. means current app
urlpatterns = [
    path('index/',views.index, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('doctors/', views.doctors, name='doctors'),
    path('department/', views.department, name='department'),
    path('contacts/', views.contacts, name='contacts'),

]