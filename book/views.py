from django.shortcuts import render , get_object_or_404
from .models import book_values
from django.http import FileResponse, Http404
# Create your views here.
a_books = book_values.objects.all()
def index(request):
    books = {
        "books" : a_books  
            }
    return render(request, 'book/index.html' , books)
def book_details(request , id):
    # try:
    #    book = book_values.objects.get(pk = id)
    # except :
    #     raise Http404 # we got book by its id 
    book = get_object_or_404(book_values , pk = id) # it will raise an error if its not
    return render(request , 'book/book_details.html' , {
        "book" : book
     })
    