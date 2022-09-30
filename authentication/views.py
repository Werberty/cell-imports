from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.shortcuts import redirect, render

from .utils import password_is_valid


def register(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'authentication/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR,
                                 'Usuário já existe.')
            return render(request, 'authentication/register.html')

        if len(username) < 6:
            messages.add_message(request, messages.ERROR,
                                 'Usuário precisa ter mais de 6 caracteres.')
            return render(request, 'authentication/register.html')

        if not password_is_valid(
                request, password=password,
                confirm_password=confirm_password):
            return render(request, 'authentication/register.html')

        try:
            validate_email(email)
        except:
            messages.add_message(request, messages.ERROR,
                                 'Email inválido.')
            return render(request, 'authentication/register.html')

        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Cadastro feito com sucesso.')
        except:
            messages.add_message(request, messages.ERROR,
                                 'Erro interno do sistema.')
            return render(request, 'authentication/register.html')

        return redirect('/auth/login')


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'authentication/login.html')

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if not user:
            messages.add_message(request, messages.ERROR,
                                 'Usuario ou senha inválido.')
            return render(request, 'authentication/login.html')
        else:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS,
                                 'Login com sucesso.')
            return redirect('/stock/')


def logout(request):
    auth.logout(request)
    return redirect('/auth/login')
