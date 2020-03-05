from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
'''class Shipping(models.Model):
    departure = models.CharField(verbose_name="Depart from")

class Products(models.Model):
    description = models.TextField(verbose_name="Description", max_length=150)
    price = models.FloatField(verbose_name="Price", max_length=5)
    manual = models.FileField(verbose_name="Manual")
    shipping = models.ForeignKey(Shipping,verbose_name="Shipping",on_delete=models.CASCADE)
'''

class Tutors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.FileField(verbose_name="Tutor's Picture")
    about = models.TextField(verbose_name='About Tutor')
    phone_number = models.CharField(verbose_name="Tutor's phone number", max_length=14)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class Tutorials(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    content = models.TextField(verbose_name='Content', max_length=2000)
    video_link = models.URLField(verbose_name='Tutiral video link',max_length=50)
    images = models.FileField(verbose_name='Tutorial images')
    tutor = models.ManyToManyField(Tutors, verbose_name="Tutor(s)",through='Tutorships')

    def __str__(self):
        return self.title


class Tutorships(models.Model):
    tutorial = models.ForeignKey(Tutorials, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutors, on_delete=models.CASCADE)

    def __str__(self):
        return '{} by {}, {}'.format(self.tutorial.title,self.tutor.user.first_name, self.tutor.user.last_name)

