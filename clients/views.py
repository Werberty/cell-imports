from django.shortcuts import render


def clients(request):
    return render(request, 'clients.html')
