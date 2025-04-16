from django.contrib import admin
from .models import book_values , author

# Register your models here.
class bookAdmin(admin.ModelAdmin): 
    prepopulated_fields = {
        'slug' : ('title' , ) 
    }
    list_display = ('title' , 'author',)
    list_filter = ('author' , 'rating' ,)

class authorAdmin(admin.ModelAdmin):
    list_display = ()

admin.site.register(author)
admin.site.register(book_values , bookAdmin)