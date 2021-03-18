from django.shortcuts import render, redirect
from .models import User

def index(request):
    context = {
        "all_users": User.objects.all()
    }
    return render(request, 'index.html', context)

def process_new_user(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    age = request.POST['age']
    User.objects.create(first_name = first_name, last_name = last_name, email_address = email, age = age)
    return redirect('/')
