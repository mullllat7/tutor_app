# Generated by Django 4.0 on 2022-02-18 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_subcat', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('subcat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategory', to='category.category')),
            ],
        ),
        migrations.CreateModel(
            name='SubcategoryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_image', to='subcategory.subcategory')),
            ],
        ),
    ]
