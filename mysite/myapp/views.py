from django.shortcuts import render
from django.http import HttpResponse
from .models import City, Author, Book
def city_list(request):
    cities = City.objects.all()
    return render(request, 'city_list.html', {'cities': cities})

def author_list(request, city_id):
    city = City.objects.get(pk=city_id)
    authors = Author.objects.filter(city=city)
    return render(request, 'author_list.html', {'city': city, 'authors': authors})

def book_list(request, author_id):
    author = Author.objects.get(pk=author_id)
    books = Book.objects.filter(author=author)
    return render(request, 'book_list.html', {'author': author, 'books': books})
