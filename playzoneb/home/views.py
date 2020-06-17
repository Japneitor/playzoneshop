from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .models import Juego
# Create your views here.
def home(request):
    lista_juegos = Juego.objects.all()
    return render(request, 'home.html', {
    'lista_juegos': lista_juegos,
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html', {
        
    })