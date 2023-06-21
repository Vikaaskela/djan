from django.shortcuts import render
from .models import Category, Menu
from django.http import HttpResponse

# Create your views here.
def category_list(request): 
    category = Category.objects.all()
    res = ""
    for item in category:
        res += f'<h1>{item}<h1>'
    return HttpResponse(res)

def menu_list(request):
    ...