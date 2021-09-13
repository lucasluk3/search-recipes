from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from recipes import views

urlpatterns = [
    path('recipes', views.SearchRecipes.as_view(), name='search_recipes'),
    path('recipes/chef/', views.CreateChef.as_view(), name='create_chef'),
    path('recipes/chef/recipe/', views.CreateRecipe.as_view(), name='create_recipe'),
    path('recipes/chef/recipe/<int:pk>', views.DetailRecipe.as_view(), name='detail_recipe'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
