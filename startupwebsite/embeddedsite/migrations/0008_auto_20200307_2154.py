# Generated by Django 3.0.1 on 2020-03-07 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('embeddedsite', '0007_auto_20200307_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='picture_buttom',
            field=models.FileField(default='image.png', upload_to='', verbose_name='Buttom view'),
        ),
        migrations.AddField(
            model_name='product',
            name='picture_left',
            field=models.FileField(default='image.png', upload_to='', verbose_name='Side view(Right)'),
        ),
        migrations.AddField(
            model_name='product',
            name='picture_right',
            field=models.FileField(default='image.png', upload_to='', verbose_name='Right view(Left)'),
        ),
        migrations.AddField(
            model_name='product',
            name='picture_top',
            field=models.FileField(default='image.png', upload_to='', verbose_name='Top view'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.FileField(default='image.png', upload_to='', verbose_name="Product's Picture"),
        ),
    ]
