# Generated by Django 3.1.5 on 2021-05-20 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]