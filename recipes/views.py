from rest_framework.generics import (
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
)

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer, ChefSerializer


class CreateChef(ListCreateAPIView):
    """
    View for creation of Chef object
    """

    serializer_class = ChefSerializer


class ListCreateRecipes(ListCreateAPIView):
    """
    View for creation of Recipe object
    """

    serializer_class = RecipeSerializer

    def get_queryset(self):
        """
        Overriding the method get_queryset for adding a custom filter using query_params
        :param: name, difficulty, chef
        :return: queryset
        """
        params = self.request.query_params
        queryset = Recipe.objects.filter(
            name__icontains=params.get("name", ""),
            difficulty__icontains=params.get("difficulty", ""),
            chef__name__icontains=params.get("chef", ""),
        ).order_by("created")
        return queryset


class DetailRecipe(RetrieveUpdateDestroyAPIView):
    """
    View who shows the details of a recipe, and make his update and delete
    """

    serializer_class = RecipeSerializer
    queryset = Recipe
