# Generated by Django 3.1.5 on 2021-05-20 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0003_auto_20210520_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='products',
        ),
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='rest_app.product'),
            preserve_default=False,
        ),
    ]
