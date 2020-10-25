from django.shortcuts import render, get_object_or_404, redirect
from .models import rent
from userapp.models import CustomUser
# Create your views here.

def home(request):
    return render(request, 'rent/home.html')

def detail(request):
    return render(request, 'detail/detail.html')

def create(request):
    if request.method == 'POST' and request.session.get('user',False):
        machine = request.POST['machine']
        category = request.POST['category']
        inventory = request.POST['inventory']
        provider = request.POST['provider']

        Rent = rent(
            machine = machine,
            category = category,
            inventory = inventory,
            provider = provider,
        ) 
        Rent.save()

        return redirect('home')
    else:
        return render(request, 'rent/detail.html')

def rentbtn(request):
    return render(request, 'detail/detail.html')