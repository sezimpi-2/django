from django.shortcuts import render
from django.http import HttpResponse

def news_blog_view(request):
    if request.method == 'GET':
        return HttpResponse ("Hello word")

def about_me_view(request):
    if request.method == 'GET':
        return HttpResponse ("Всем привет")

# Create your views here.
