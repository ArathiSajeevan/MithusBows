# Generated by Django 5.0.3 on 2024-04-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mithusbows', '0003_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.CharField(max_length=20),
        ),
    ]
