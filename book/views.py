from django.shortcuts import render
from .models import book_values
# Create your views here.
a_books = book_values.objects.all()
def index(request):
    books = {
        "books" : a_books  
            }
    return render(request, 'book/index.html' , books)