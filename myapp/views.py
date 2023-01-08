from django.shortcuts import render, redirect
from .models import BusData1
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')


def lilist(request):
    jojos = BusData1.objects.all()
    return render(request, 'buslists.html', {'jojos': jojos})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('admin/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    return render(request, 'login.html')


def display(request, pk):
    posts = BusData1.objects.get(id=pk)
    return render(request, 'busData.html', {'posts': posts})
