# Generated by Django 3.2.7 on 2021-09-13 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20210911_2226'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chef',
            options={'verbose_name': 'Chefe', 'verbose_name_plural': 'Chefes'},
        ),
        migrations.AddField(
            model_name='recipe',
            name='time',
            field=models.IntegerField(default=0, verbose_name='Tempo de preparo (em minutos)'),
        ),
        migrations.AlterField(
            model_name='chef',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome do Chefe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='chef',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipes.chef', verbose_name='Chefe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='difficulty',
            field=models.CharField(choices=[('1', 'Iniciante'), ('2', 'Experiente'), ('3', 'Avançado')], default='1', max_length=1, verbose_name='Dificuldade'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(verbose_name='Ingredientes'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='method',
            field=models.TextField(default='', verbose_name='Modo de Preparo'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nome da Receita'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='short_description',
            field=models.CharField(max_length=100, verbose_name='Descrição breve'),
        ),
    ]