from django.db import models
from django.contrib.auth.models import User, auth
#
from django_countries.fields import CountryField

# Create your models here.
TITLES =[
    ('MR','Mr.'),
    ('MRS','Mrs'),
    ('ENGR','Engineer'),
    ('DR','Doctor'),
    ('PROF','Professor'),
]

CURRENCIES = [
    ('NAIRA','#'),
    ('US DOLLAR','$'),
    ('POUNDS','P')
]
STATES =('Abuja','Abia','Adamawa','Akwa-Ibom','Anambra','Bauchi','Bayelsa',
'Benue','Borno','Cross-River','Delta','Ebonyi','Edo','Ekiti','Enugu','Gombe',
'Ibadan','Imo','Jigawa','Kaduna','Kano','Katsina','Kebbi','Kogi','Kwara',
'Lagos','Nasarawa','Niger','Ogun','Ondo','Osun','River','Sokoto','Taraba',
'Yobe','Zamfara')
POSITIONS = [
    ('CEO','CEO'),
    ('AUTHOR','Author'),
    ('TUTOR','Tutor'),
    ('SELLS MANAGER','Sells manager'),
    ('DEVELOPER','Developer'),
    ('INTERN', 'Internship Student')
]


class Product(models.Model):
    name = models.CharField(verbose_name='Product name', max_length=50)
    description = models.TextField(verbose_name="Description", max_length=150)
    price = models.FloatField(verbose_name="Price", max_length=10)
    manual = models.FileField(verbose_name="Manual", blank=True)
    currency = models.CharField(choices=CURRENCIES, max_length=10)

    def __str__(self):
        return '{} at {}{}'.format(self.name,self.currency,self.price)


class ShippingAddress(models.Model):
    destination_country = CountryField(verbose_name="Destination country")
    state_province = models.CharField(max_length=50, verbose_name='State/Province')
    city = models.CharField(max_length=50, verbose_name='City')
    zip_code = models.IntegerField(verbose_name='Zip Code')
    street_name = models.CharField(max_length=100, verbose_name='Street name', blank=True)

    def __str__(self):
        return '{}, {}, {}. {}'.format(self.street_name,self.city,self.state_province,self.destination_country)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='Shipped on')
    currency = models.CharField(choices=CURRENCIES, max_length=10)
    Shipping_method = models.CharField(verbose_name='Shipped through', max_length=50)
    customer = models.ForeignKey(User, blank=True, max_length=50, on_delete=models.CASCADE, default='No customer details')

    def __str__(self):
        return '{} to {} on {}'.format(self.product.name, self.address,self.date)


class Shipping(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    ShippingAddress = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='Shipped on')

    def __str__(self):
        return '{} shipped on {} to {}'.format(self.order,self.date,self.ShippingAddress)


class Author(models.Model):
    title = models.CharField(max_length=15, choices=TITLES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.FileField(verbose_name="Author's Picture")
    about = models.TextField(verbose_name='About author')
    phone_number = models.CharField(verbose_name="Author's phone number", max_length=14)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)


class Tutorial(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    content = models.TextField(verbose_name='Content', max_length=2000)
    video_link = models.URLField(verbose_name='Tutorial video link',max_length=50)
    images = models.FileField(verbose_name='Tutorial images')
    tutor = models.ManyToManyField(Author, verbose_name="Tutor(s)",through='Tutorship')
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
    author = models.ManyToManyField(Author, verbose_name='Author', through='Projectship')
    date_published = models.DateTimeField()
    
    def __str__(self):
        return self.title


class Projectship(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return '{} by {}, {}'.format(self.project.title,self.author.user.first_name, self.author.user.last_name)
    
class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    content = models.TextField(max_length=2000, verbose_name='Your comment')
    date_of_comment = models.DateTimeField()

    def __str__(self):
        return 'Comment by {}'.format(self.user.username)


class Service(models.Model):
    title = models.CharField(verbose_name='Title', max_length=100)
    description = models.TextField(verbose_name='Content', max_length=600)
    cost = models.FloatField(max_length=10, blank=True)
    currency = models.CharField(max_length=10, choices=CURRENCIES)

    def __str__(self):
        if not self.cost:
            return self.title
        else:
            return '{}, {}{}'.format(self.title,self.currency,self.cost)

class TeamMember(models.Model):
    title = models.CharField(max_length=15, choices=TITLES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    about = models.TextField(verbose_name='About team member')
    phone_number = models.CharField(verbose_name="Member's phone number", max_length=14)
    position = models.CharField(verbose_name='Position', max_length=20, choices=POSITIONS)
    picture = models.FileField(verbose_name="Member's Picture") 
    twitter_handle = models.URLField(blank=True)   
    instagram_handle = models.URLField(blank=True)

    def __str__(self):
        return '{} {},{}'.format(self.title,self.user.first_name,self.last_name)

    
class Enquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(verbose_name='Equiry body', max_length=600)

    def __str__(self):
        return '{} from {} {}'.format(self.title, self.user.first_name, self.user.last_name)

class Circuit(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(verbose_name='Equiry message', max_length=600)
    diagram = models.FileField(verbose_name='Circuit diagram')
    designer = models.ForeignKey(Author, on_delete=models.CASCADE)  

    def __str__(self):
        return '{} by {} {}'.format(self.title, self.designer.user.first_name, self.designer.user.last_name)


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.TextField(verbose_name='Customer Review', max_length=600)
    rating = models.FloatField(verbose_name='Rating', max_length=1)

    def __str__(self):
        return '{} reviewed by {} {}'.format(self.product.name, self.user.first_name, self.user.last_name)


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(verbose_name='Event discription', max_length=600)
    event_picture = models.FileField(verbose_name="Event's Picture") 
    date = models.DateTimeField()
    venue = models.CharField(verbose_name='Venue', max_length=100)

    def __str__(self):
        return'{} by {}'.format(self.title,self.venue)