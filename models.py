from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
TITLES =[
    ('MR','Mr.'),
    ('MRS','Mrs'),
    ('ENGR','Engineer'),
    ('DR','Doctor'),
    ('PROF','Professor'),
]
'''class Shipping(models.Model):
    departure = models.CharField(verbose_name="Depart from")

class Products(models.Model):
    description = models.TextField(verbose_name="Description", max_length=150)
    price = models.FloatField(verbose_name="Price", max_length=5)
    manual = models.FileField(verbose_name="Manual")
    shipping = models.ForeignKey(Shipping,verbose_name="Shipping",on_delete=models.CASCADE)
'''

class Author(models.Model):
    title = models.Model(max_length=15, choices=TITLES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.FileField(verbose_name="Tutor's Picture")
    about = models.TextField(verbose_name='About Tutor')
    phone_number = models.CharField(verbose_name="Tutor's phone number", max_length=14)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class Tutorial(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    content = models.TextField(verbose_name='Content', max_length=2000)
    video_link = models.URLField(verbose_name='Tutiral video link',max_length=50)
    images = models.FileField(verbose_name='Tutorial images')
    tutor = models.ManyToManyField(Author, verbose_name="Tutor(s)",through='Tutorships')
    date_published = models.DateTimeField()

    def __str__(self):
        return self.title


class Tutorship(models.Model):
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return '{} by {}, {}'.format(self.tutorial.title,self.author.user.first_name, self.author.user.last_name)

class Project(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    description = models.TextField(verbose_name='Content', max_length=2000)
    writeup = models.FileField(verbose_name='Project writeup')
    cost = models.FloatField(verbose_name='Cost')
    author = models.ForeignKey(Author, verbose_name='Author')
    date_published = models.DateTimeField()
    
    def __str__(self):
        return self.title


class Projectship(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return '{} by {}, {}'.format(self.project.title,self.author.user.first_name, self.author.user.last_name)
    
