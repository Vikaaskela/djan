from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def authors_all(request):
    res = """
    <h1>Автор 1</h1>
    <h1>Автор 2</h1>
    <h1>Автор 3</h1>
    """
    return HttpResponse(res)

    

