from django.contrib import auth
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.shortcuts import redirect, render

from .utils import password_is_valid


def register(request):
    if request.method == 'GET':
        return render(request, 'authentication/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            print('usuario já existe.')
            return render(request, 'authentication/register.html')

        if not password_is_valid(request, password=password, confirm_password=confirm_password):
            print('Senha invalida.')
            return render(request, 'authentication/register.html')

        try:
            validate_email(email)
        except:
            print('email inválido.')
            return render(request, 'authentication/register.html')

        if len(username) < 6:
            print('usuario menor que 6 caracteres.')
            return render(request, 'authentication/register.html')

        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            user.save()
            print('Usuario salvo com sucesso.')
        except:
            print('Erro interno do sistema.')
            return render(request, 'authentication/register.html')

        return redirect('/auth/login')


def login(request):
    if request.method == 'GET':
        return render(request, 'authentication/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if not user:
            print('Usuario ou senha inválido.')
            return render(request, 'authentication/login.html')
        else:
            print('Bem vindo')
            return redirect('/')
