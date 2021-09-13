from rest_framework import serializers

from recipes.models import Recipe, Chef


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = [
            'name',
            'short_description',
            'ingredients',
            'method',
            'difficulty',
            'chef',
            'time'
        ]


class ChefSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chef
        fields = ['name']
