from django.shortcuts import render , get_object_or_404
from .models import book_values
from django.db.models import Avg , Max
from django.http import FileResponse, Http404
# Create your views here.
a_books = book_values.objects.all().order_by("rating") #-"column name" order by descending 
def index(request):

    num_book = a_books.count()
    avg_rating = a_books.aggregate(Avg("rating"))
    books = {
        "books" : a_books ,
        "number_of_books" :num_book,
        "average_Rating" : avg_rating
            }
    return render(request, 'book/index.html' , books)
def book_details(request , slug):
    # try:
    #    book = book_values.objects.get(pk = id)
    # except :
    #     raise Http404 # we got book by its id 
    book = get_object_or_404(book_values , slug = slug) # it will raise an error if its not
    return render(request , 'book/book_details.html' , {
        "book" : book
     })
    