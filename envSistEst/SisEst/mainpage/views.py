from django.shortcuts import render
from django.http import HttpResponse


def view_home(request):
    return render(request,'home.html')

def view_contato(request):
    return render(request, 'contato.html')
