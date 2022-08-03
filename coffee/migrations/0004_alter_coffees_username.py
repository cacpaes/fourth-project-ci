# Generated by Django 3.2.14 on 2022-08-03 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coffee', '0003_rename_coffee_coffees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffees',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coffees_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
