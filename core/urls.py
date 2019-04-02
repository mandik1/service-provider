from django.contrib import admin
from django.urls import path
from . import views 
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('services/', Services_list.as_view(), name='serviceslist'),
    path('appointment/', Appointment_form.as_view(), name='appointmentcreate'),
    # path('services1/<int:pk>', Servicetype_detail.as_view(), name='servicedetail'),
    path('signup/',SignUp.as_view(), name='signup'),
    
]
