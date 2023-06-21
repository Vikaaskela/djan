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

def books_year(request, year: int):
    res = f"""
            <h1>Книжки за {year} рік</h1>
            """
    return HttpResponse(res)
  

def books_2003(request):
    res = """
    <h1>Книжки за 2003 рік!</h1>
    """
    return HttpResponse(res)

def books_year_month(request, year: int, month: int):
    res = f"""
            <h1>Книжки за {year} рік та {month} місяць</h1>
            """
    return HttpResponse(res)


    
