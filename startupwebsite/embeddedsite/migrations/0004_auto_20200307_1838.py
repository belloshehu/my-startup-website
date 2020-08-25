# Generated by Django 3.0.1 on 2020-03-07 17:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('embeddedsite', '0003_auto_20200305_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=600, verbose_name='Event discription')),
                ('event_picture', models.FileField(upload_to='', verbose_name="Event's Picture")),
                ('date', models.DateTimeField()),
                ('venue', models.CharField(max_length=100, verbose_name='Venue')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Shipped on')),
                ('currency', models.CharField(choices=[('NAIRA', '#'), ('US DOLLAR', '$'), ('POUNDS', 'P')], default='#', max_length=10)),
                ('Shipping_method', models.CharField(max_length=50, verbose_name='Shipped through')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Product name')),
                ('description', models.TextField(max_length=150, verbose_name='Description')),
                ('price', models.FloatField(max_length=10, verbose_name='Price')),
                ('manual', models.FileField(blank=True, upload_to='', verbose_name='Manual')),
                ('currency', models.CharField(choices=[('NAIRA', '#'), ('US DOLLAR', '$'), ('POUNDS', 'P')], default='#', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_country', django_countries.fields.CountryField(max_length=2, verbose_name='Destination country')),
                ('state_province', models.CharField(max_length=50, verbose_name='State/Province')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('zip_code', models.IntegerField(verbose_name='Zip Code')),
                ('street_name', models.CharField(blank=True, max_length=100, verbose_name='Street name')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='currency',
            field=models.CharField(choices=[('NAIRA', '#'), ('US DOLLAR', '$'), ('POUNDS', 'P')], default='#', max_length=10),
        ),
        migrations.AlterField(
            model_name='service',
            name='currency',
            field=models.CharField(choices=[('NAIRA', '#'), ('US DOLLAR', '$'), ('POUNDS', 'P')], default='#', max_length=10),
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Shipped on')),
                ('ShippingAddress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='embeddedsite.ShippingAddress')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='embeddedsite.Order')),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(max_length=600, verbose_name='Customer Review')),
                ('rating', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], verbose_name='Rating')),
                ('date', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='embeddedsite.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='embeddedsite.ShippingAddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(blank=True, default=000, max_length=50, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='embeddedsite.Product'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Shipped on')),
                ('customer', models.ForeignKey(blank=True, default='No customer details', max_length=50, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='embeddedsite.Product')),
            ],
        ),
    ]