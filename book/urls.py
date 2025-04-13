from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index , name="index"),
    # path("books/" , views.books , name="books"),
    # path("books/detail/<str:book_title>/" , views.book_detail , name="book_detail"),
]

