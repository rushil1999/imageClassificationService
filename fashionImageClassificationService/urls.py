from django.urls import path 
from . import views 
urlpatterns = [ path('predImg',views.predImg, name='predImg') ]