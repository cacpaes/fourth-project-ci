# Generated by Django 3.2.14 on 2022-08-24 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0007_commentcoffee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentcoffee',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='commentcoffee',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]