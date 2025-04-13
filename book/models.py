from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class book_values (models.Model):
    title = models.CharField(max_length=100) # title of the book
    author = models.CharField(max_length=100) # author of the book
    rating = models.FloatField(validators=[MinValueValidator(0.1) , MaxValueValidator(5.0)]) # rating of the book , make sure u dont use reserved words
    # django automatically creates a primary key field called id
    is_best_seller = models.BooleanField(default=False) # best seller or not
    
    
    def __str__(self):
        if self.is_best_seller:
            return f"{self.title} by {self.author} with rating {self.rating} (Best Seller)"
        return f"{self.title} by {self.author} with rating {self.rating} "
    # this method is used to return a string representation of the object
    # when we call the object in the shell or admin panel