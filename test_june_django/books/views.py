from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def books_all(request):
    res = """
    <h1>Книга 1</h1>
    <h1>Книга 2</h1>
    <h1>Книга 3</h1>
    """
    return HttpResponse(res)
    
