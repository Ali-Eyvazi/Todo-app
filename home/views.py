from django.shortcuts import render
from .models import Todo

# Create your views here.


def say_hello(request):

    print(type(request.user))
    return render(request, 'hello.html', {'user': str(request.user)})


def home(request):
    todos = Todo.objects.all()
    return render(request, 'home.html', {'todos': todos})
