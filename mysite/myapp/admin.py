from django.contrib import admin
from .models import City, Author, Book
from .models import Person

admin.site.register(Person)
admin.site.register(City)
admin.site.register(Author)
admin.site.register(Book)
