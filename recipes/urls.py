from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from recipes import views

urlpatterns = [
    path("recipes", views.ListCreateRecipes.as_view(), name="list_create_recipes"),
    path("recipes/<int:pk>", views.DetailRecipe.as_view(), name="detail_recipe"),
    path("recipes/chef/", views.CreateChef.as_view(), name="create_chef"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
