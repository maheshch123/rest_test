# Generated by Django 3.1.5 on 2021-05-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0002_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='products',
        ),
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(to='rest_app.Product'),
        ),
    ]
