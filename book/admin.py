from django.contrib import admin
from .models import book_values

# Register your models here.
class bookAdmin(admin.ModelAdmin): 
    prepopulated_fields = {
        'slug' : ('title' , ) 
    }
    list_display = ('title' , 'author',)
    list_filter = ('author' , 'rating' ,)
admin.site.register(book_values , bookAdmin)