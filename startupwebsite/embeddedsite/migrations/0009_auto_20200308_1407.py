# Generated by Django 3.0.1 on 2020-03-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('embeddedsite', '0008_auto_20200307_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=2000, verbose_name='Description'),
        ),
    ]
