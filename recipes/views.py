from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
from recipes.models import Type_of_food, Author, Recipe
from .forms import RecipeForm

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_recipes = Recipe.objects.all().count()

    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    
    
 # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_recipes': num_recipes,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
    
from django.views import generic


class RecipeListView(generic.ListView):
    model = Recipe

    
class RecipeDetailView(generic.DetailView):
    model = Recipe

    
class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author
    
    
class Type_of_foodListView(generic.ListView):
    model = Type_of_food
    template_name = 'type_of_food_list.html'    
    
    
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

#recipe add/delete
class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    #form_class = RecipeForm
    #template_name = 'recipe_form.html'
    fields = '__all__'
    fields = ['name', 'photo', 'author', 'summary', 'ingredients', 'instructions', 'type_of_food', 'slug']
    initial = {'summary': 'Summary of recipe here', 'slug': 'Enter a title for the webpage'}

class RecipeUpdate(UpdateView):
#class RecipeUpdate(PermissionRequiredMixin, UpdateView):
    model = Recipe
    #permission_required = 'cookbook.change_recipe'
    
    template_name = 'recipe_update.html'
    #fields = ['name', 'photo', 'author', 'summary', 'ingredients', 'instructions', 'type_of_food', 'slug']
    fields = '__all__' # Not recommended (potential security issue if more fields added)
    

class RecipeDelete(DeleteView):
#class RecipeDelete(PermissionRequiredMixin, DeleteView):
    model = Recipe
    #permission_required = 'cookbook.delete_recipe'
    
    success_url = reverse_lazy('recipes')

#author add/delete
class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['username', 'summary' ]
    initial = {'summary': 'Author bio here'}

class AuthorUpdate(UpdateView):
    model = Author
    fields = '__all__' # Not recommended (potential security issue if more fields added)


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('recipes')






