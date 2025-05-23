from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def full_name(self):
        return f"{self.first_name}{self.last_name}"
    def __str__(self):
        return self.full_name()
    

class book_values (models.Model):
    title = models.CharField(max_length=100) # title of the book
    author = models.ForeignKey(author , on_delete = models.CASCADE , null = True , related_name="books") # author of the book
    rating = models.FloatField(validators=[MinValueValidator(0.1) , MaxValueValidator(5.0)])
    is_best_seller = models.BooleanField(default=False) # best seller or not
    publication_date = models.DateField(null = True) # publication date of the book
    slug = models.SlugField(default="" , null=False , db_index=True , blank= True )  
    
    
    
    def __str__(self):
        if self.is_best_seller:
            return f"{self.title} by {self.author} with rating {self.rating} (Best Seller)"
        return f"{self.title} by {self.author} with rating {self.rating} , {self.slug} "
    



    def get_absolute_url(self):
        return reverse("book_detail" , args=[self.slug])
    


    
    def save (self , *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args , **kwargs) # this will save data to db
    # this method is used to return a string representation of the object
    # when we call the object in the shell or admin panel

class bookdetails(models.Model):
    book = models.OneToOneField(book_values, on_delete = models.CASCADE , null = True , related_name = "details")
    language = models.CharField(max_length=50)
    # category = 
    pages = models.PositiveIntegerField(null = True)
    description = models.TextField()


class category(models.Model):
    pass