from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/', views.RecipeListView.as_view(), name='recipes'),
    path('recipe/<slug:slug>', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('recipes/', views.Type_of_foodListView.as_view(), name='type_of_food_list'),
]


urlpatterns += [  
    path('recipe/create/', views.RecipeCreate.as_view(), name='recipe_create'),
    path('recipe/<slug:slug>/update/', views.RecipeUpdate.as_view(), name='recipe_update'),
    path('recipe/<slug:slug>/delete/', views.RecipeDelete.as_view(), name='recipe_delete'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
]