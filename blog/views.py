from django.shortcuts import render
import requests


def home_view(request):
    return render(request, 'index.html')
