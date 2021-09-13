from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView

from recipes.models import Recipe, Chef
from recipes.serializers import RecipeSerializer, ChefSerializer


class CreateChef(CreateAPIView):
    """
    View for creation of Chef object
    """
    model = Chef
    serializer_class = ChefSerializer


class CreateRecipe(CreateAPIView):
    """
    View for creation of Recipe object
    """
    model = Recipe
    serializer_class = RecipeSerializer


class DetailRecipe(RetrieveUpdateDestroyAPIView):
    """
    View who shows the details of a recipe, and make his update and delete
    """
    serializer_class = RecipeSerializer
    queryset = Recipe


class SearchRecipes(ListAPIView):
    """
    View responsible for search recipes based on the name and difficulty
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
            name__icontains=params.get('name', ''),
            difficulty__icontains=params.get('difficulty', ''),
            chef__name__icontains=params.get('chef', '')
        ).order_by('created')
        return queryset
