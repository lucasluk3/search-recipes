from django.db import models


class Chef(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome do Chefe')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Chefe'
        verbose_name_plural = 'Chefes'


class Recipe(models.Model):
    DIFFICULTY_LEVELS = [
        ('1', 'Iniciante'),
        ('2', 'Experiente'),
        ('3', 'Avançado')
    ]
    name = models.CharField(max_length=50, verbose_name='Nome da Receita')
    short_description = models.CharField(max_length=100, verbose_name='Descrição breve')
    ingredients = models.TextField(verbose_name='Ingredientes')
    method = models.TextField(default='', verbose_name='Modo de Preparo')
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_LEVELS, default='1', verbose_name='Dificuldade')
    chef = models.ForeignKey(Chef, on_delete=models.PROTECT, verbose_name='Chefe')
    time = models.IntegerField(verbose_name='Tempo de preparo (em minutos)', default=0)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
