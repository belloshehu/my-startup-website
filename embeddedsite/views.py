from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import *
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.urls import reverse
from .forms import LoginForm, RegistrationForm, CommentForm, UserRegistration
from datetime import datetime

# Create your views here.
def home(request):
    products = Product.objects.all()
    projects = Project.objects.all()
    services = Service.objects.all()
    tutorials = Tutorial.objects.all()
    team_members = TeamMember.objects.all()
    circuits = Circuit.objects.all()
    events = Event.objects.all()
    context = {'products':products, 'projects':projects, 'team_members':team_members, 'tutorials':tutorials,
     'services':services, 'circuits':circuits, 'events':events}
    return render(request, 'startupwebsite/home2.html',context)

def products(request):
    products = Product.objects.all()
    projects = Project.objects.all()
    services = Service.objects.all()
    tutorials = Tutorial.objects.all()
    team_members = TeamMember.objects.all()
    context = {'products':products, 'projects':projects, 'team_members':team_members, 'tutorials':tutorials,
     'services':services,}
    return render(request, 'startupwebsite/products.html',context)


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        user = authenticate(
                username=request.POST['username'], 
                password=request.POST['password']
            )
        if user is not None:
            login(request, user)
            return redirect('embeddedsite:home')
        else:
            messages.error(request, 'Wrong username or password.')
            redirect(reverse('embeddedsite:login'))
    team_members = TeamMember.objects.all()
    context = {'form':form, 'team_members':team_members}
    return render(request,'startupwebsite/login.html',context)


def user_logout(request):
    logout(request)
    return redirect('embeddedsite:home')


def tutorials(request):
    products = Product.objects.all()
    projects = Project.objects.all()
    services = Service.objects.all()
    tutorials = Tutorial.objects.all()
    team_members = TeamMember.objects.all()
    tutorships = Tutorship.objects.all()
    context = {'products':products, 'projects':projects, 'team_members':team_members, 'tutorials':tutorials,
     'services':services,'tutorships':tutorships}
    return render(request, 'startupwebsite/tutorials.html', context)

def tutorial(request, tutorial_id):
    tutorial_id = int(tutorial_id)
    tutorial = Tutorship.objects.get(tutorial_id=tutorial_id)
    tutorials = Tutorial.objects.all()
    products = Product.objects.all()
    projects = Project.objects.all()
    team_members = TeamMember.objects.all()
    comments = Comment.objects.filter(tutorial_id=tutorial_id)
    form = CommentForm
    context = {
        'tutorship':tutorial,'products':products,
        'projects':projects,'tutorials':tutorials,'comments':comments,
        'team_members':team_members,'form':form
        }    
    return render(request, 'startupwebsite/tutorial.html', context)

def handle_comment_submission(request, tutorial_id):
    email = request.POST['email']
    content = request.POST['comment']
    try:
        user = User.objects.get(email=email)
        tutorial_id = int(tutorial_id)
        date_of_comment = datetime.now()
        comment = Comment(tutorial_id=tutorial_id, content=content, user_id=user.id, date_of_comment=date_of_comment)
        comment.save()
        return redirect('tutorial',tutorial_id)
    except User.DoesNotExist:
        messages.info(request, 'Error: Check your email or you should sign up')
        return redirect('tutorial',tutorial_id)

def sign_up(request):
    form = UserRegistration()
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        form = UserRegistration(request.POST)
        if form.is_valid: 
            print(request.POST.keys())
            if User.objects.filter(username=username).exists() and User.objects.filter(email=email).exists():
                messages.error(request, 'Error occured!')
                redirect(reverse('embeddedsite:signup'))
            elif request.POST['password1'] != request.POST['password2']:
                messages.error(request, 'Error occured !')
                redirect(reverse('embeddedsite:signup'))
            else:
                form.save()
                redirect('embeddedsite:signup_success')
    team_members = TeamMember.objects.all()
    context = {'team_members':team_members, 'form':form}
    return render(request, 'startupwebsite/signup.html', context)


def signup_success(request):
    context = {}
    return render(request, 'startupwebsite/signup_success.html', context)


def product(request,product_id):
    product_id = int(product_id)
    product =Product.objects.get(id=product_id)
    team_members = TeamMember.objects.all()
    context = {'product':product, 'team_members':team_members,}
    return render(request, 'startupwebsite/product.html',context)


def show_cart(request):
    """ Show all cusomer's shopping cart items. """
    carts = None
    if request.user.is_authenticated:
        try:
            carts = Cart.objects.filter(customer=request.user.id)
        except Cart.DoesNotExist:
            redirect('embeddedsite:home')
        context = {'carts':carts,}
        return render(request, 'startupwebsite/cart.html',context)
    redirect('embeddedsite:login')


def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product_id = int(product_id)
        product = Product.objects.get(id=product_id)
        team_members = TeamMember.objects.all()
        if Cart.objects.filter(customer=request.user.id ,product=product_id).exists() is None:
            cart = Cart(product=product, customer=request.user,date=datetime.now())
            cart.save()
        carts = Cart.objects.filter(customer=request.user.id)
        context = {'carts':carts, 'team_members':team_members,}
        return render(request, 'startupwebsite/cart.html',context)
    else:
        return redirect('login')


def remove_from_cart(request, product_id):
    """ Remove a product from customer's shopping cart. """
    if request.user.is_authenticated:
        try:
            Cart.objects.get(customer=request.user.id, product=product_id).delete()
        except Cart.DoesNotExist:
            pass
    return redirect('embeddedsite:show_cart')




    
def enquiry(request):
    return render(request, 'startupwebsite/enquiry.html', )


def circuits(request):
    return render(request, 'startupwebsite/circuits.html', )


def about_us(request):
    return render(request, 'startupwebsite/aboutus.html',)


def services(request):
   return render(request, 'startupwebsite/services.html',)


def projects(request):
    return render(request, 'startupwebsite/projects.html',)


def search_products(request):
    search_key = request.GET.get('searchKey', None)
    result = None
    try:
        result = Product.objects.filter(name__icontains=search_key).values()
        if not result:
            result = Product.objects.filter(description__icontains=search_key).values()    
    except Product.DoesNotExist:
        pass
    data = {
        'result': list(result),
    }
    return JsonResponse(data)

    
def search_tutorials(request):
    search_key = request.GET.get('searchKey', None)
    result = None
    try:
        result = Tutorial.objects.filter(title__icontains=search_key).values()
        if not result:
            result = Tutorial.objects.filter(content__icontains=search_key).values()    
    except Tutorial.DoesNotExist:
        pass
    data = {
        'result': list(result),
    }
    return JsonResponse(data)


def search_projects(request):
    search_key = request.GET.get('searchKey', None)
    result = None
    try:
        result = Project.objects.filter(title__icontains=search_key).values()
        if not result:
            result = Project.objects.filter(description__icontains=search_key).values()    
    except Project.DoesNotExist:
        pass
    data = {
        'result': list(result),
    }
    return JsonResponse(data)


def search_services(request):
    search_key = request.GET.get('searchKey', None)
    result = None
    try:
        result = Service.objects.filter(title__icontains=search_key).values()
        if not result:
            result = Service.objects.filter(description__icontains=search_key).values()    
    except Service.DoesNotExist:
        pass
    data = {
        'result': list(result),
    }
    return JsonResponse(data)


def search_circuits(request):
    search_key = request.GET.get('searchKey', None)
    result = None
    try:
        result = Circuit.objects.filter(title__icontains=search_key).values()
        if not result:
            result = Circuit.objects.filter(description__icontains=search_key).values()    
    except Circuit.DoesNotExist:
        pass
    data = {
        'result': list(result),
    }
    return JsonResponse(data)


def check_username(request):
    "check if username is already in use"
    username = request.GET.get('username', None)
    result = False
    try:
        if User.objects.get(username=username):
            result = True
    except User.DoesNotExist:
        pass
        
    data = {
        'result': result
    }
    return JsonResponse(data)


def check_email(request):
    "check if email is already in use."
    email = request.GET.get('email', None)
    result = False
    try:
        if User.objects.get(email=email):
            result = True
    except User.DoesNotExist:
        pass
        
    data = {
        'result': result
    }
    return JsonResponse(data)
