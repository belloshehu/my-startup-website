from django.shortcuts import render
from django.http import HttpResponse
from .models import *

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
    return render(request, 'startupwebsite/home.html',context)



