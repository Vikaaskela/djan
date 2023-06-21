
from django.urls import path
from .views import books_all, books_2003, books_year, books_year_month

urlpatterns = [
    path('', books_all),
    path('2003', books_2003),
    path('<int:year>/', books_year),
    path('<int:year>/<int:month>',books_year_month)
]
