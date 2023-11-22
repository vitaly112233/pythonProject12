from django.urls import path
from .views import city_list, author_list, book_list

urlpatterns = [
    path('cities/', city_list, name='city_list'),
    path('authors/<int:city_id>/', author_list, name='author_list'),
    path('books/<int:author_id>/', book_list, name='book_list'),
]
