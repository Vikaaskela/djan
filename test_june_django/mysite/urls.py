"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authors.views import authors_all
from books.views import books_all, books_2003, books_year, books_year_month
from menu.views import category_list,  menu_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authors/', authors_all),

    path('books/', include('books.urls')),
    path('category/', category_list),
    path('menu/', menu_list),
]
