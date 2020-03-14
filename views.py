from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import LoginForm, RegistrationForm, CommentForm
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
    return render(request, 'home.html',context)

def products(request):
    products = Product.objects.all()
    projects = Project.objects.all()
    services = Service.objects.all()
    tutorials = Tutorial.objects.all()
    team_members = TeamMember.objects.all()
    context = {'products':products, 'projects':projects, 'team_members':team_members, 'tutorials':tutorials,
     'services':services,}
    return render(request, 'products.html',context)

def login(request):
    form = LoginForm
    context = {'form':form}
    return render(request,'login.html',context)

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
    comments = Comment.objects.all()
    form = CommentForm
    context = {'tutorship':tutorial,'products':products, 'projects':projects,'tutorials':tutorials,'comments':comments,'form':form}
    return render(request, 'startupwebsite/tutorial.html', context)

def handle_comment_submission(request, tutorial_id):
    email = request.POST['email']
    content = request.POST['comment']
    user = User.objects.get(email=email)
    if user is not None:
        tutorial_id = int(tutorial_id)
        date_of_comment = datetime.now()
        comment = Comment(tutorial_id=tutorial_id, content=content, user_id=user.id, date_of_comment=date_of_comment)
        comment.save()
        return redirect('tutorial',tutorial_id)
    else:
        messages.info(request, 'Error: Check your email or you should sign up')
        return redirect('tutorial',tutorial_id)
    



