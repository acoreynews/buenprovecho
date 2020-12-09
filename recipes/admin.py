from django.contrib import admin

from .models import Recipe, Author, Type_of_food

admin.site.register(Recipe)
admin.site.register(Author)
admin.site.register(Type_of_food)
