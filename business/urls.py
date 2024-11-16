from django.urls import path

from . import views

app_name = 'business'

# Define the URL patterns for the student app
urlpatterns = [

    path('', views.index, name='index'),
    path('portfolio_details', views.index, name='portfolio_details'),
    path('service_details', views.index, name='service_details'),
   
]
