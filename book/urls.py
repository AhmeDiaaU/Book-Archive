from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("" , views.index , name="index"),
    path("<slug:slug>" , views.book_details , name="book_detail"),
    # path("books/" , views.books , name="books"),
    # path("books/detail/<str:book_title>/" , views.book_detail , name="book_detail"),
] 

