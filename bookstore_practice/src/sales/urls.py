from django.urls import path
from .views import home
from . import views

app_name = 'Sales'

urlpatterns = [
    path('', views.records, name='sales-records'),
    path('home/', views.records, name='sales-home'),
]