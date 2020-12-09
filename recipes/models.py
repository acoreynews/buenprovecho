from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User

# Create your models here.
class Type_of_food(models.Model):
    """Model representing a type of food (genre of food?)."""
    name = models.CharField(max_length=500, help_text='Enter a type of food (e.g. Mexican, Pasta)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    def get_absolute_url(self):
        return reverse('type_of_food_list', kwargs={'type_of_food': self.type_of_food})
    
    #def get_absolute_url(self):
    #    return reverse('index')


class Recipe(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)

    photo = models.ImageField(null=True, blank=True, upload_to='images/')
    
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the dish')
    ingredients = models.TextField(max_length=1000, help_text='Enter the ingredients', default='ingredients here')
    instructions = models.TextField(max_length=1000, help_text='Detail the cooking steps', default='steps here')
    
    # ManyToManyField used because Type_of_food can contain many recipes. Recipes can cover multiple Type_of_food(s).
    # Type_of_food class has already been defined so we can specify the object above.
    #type_of_food = models.ManyToManyField(Type_of_food, help_text='Select what kind of dish this is')
    type_of_food = models.CharField(max_length=500, help_text='Select what kind of dish this is', default="other")
    
    
    class Meta:
         permissions = (("can_update", "can_delete"),)   
    
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    
    #def get_absolute_url(self):
        """Returns the url to access a detail record for this recipe."""
    #    return reverse('recipe-detail', args=[str(self.id)])
    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'slug': self.slug}) # new
        
        
    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
        
class Author(models.Model):
    """Model representing an author."""
    username = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000, help_text='Tell us about yourself!', default='Enter bio here')

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.username}'
        
        
    
        
        