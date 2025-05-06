from django.shortcuts import render 
from django.views.generic import ListView # o display lists
from .models import Book # to access Book model

# Create your views here.
class BookListView(ListView): # class-based view
    model = Book # specify model
    template_name = 'books/main.html' # specify template
