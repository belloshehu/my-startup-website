# Generated by Django 3.0.1 on 2020-03-05 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('content', models.TextField(max_length=2000, verbose_name='Content')),
                ('video_link', models.URLField(max_length=50, verbose_name='Tutiral video link')),
                ('images', models.FileField(upload_to='', verbose_name='Tutorial images')),
            ],
        ),
        migrations.CreateModel(
            name='Tutors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.FileField(upload_to='', verbose_name="Tutor's Picture")),
                ('about', models.TextField(verbose_name='About Tutor')),
                ('phone_number', models.CharField(max_length=14, verbose_name="Tutor's phone number")),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='embeddedsite.Tutors')),
                ('tutorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='embeddedsite.Tutorials')),
            ],
        ),
        migrations.AddField(
            model_name='tutorials',
            name='tutor',
            field=models.ManyToManyField(through='embeddedsite.Tutorships', to='embeddedsite.Tutors', verbose_name='Tutor(s)'),
        ),
    ]
