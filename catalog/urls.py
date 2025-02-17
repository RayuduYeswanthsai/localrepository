from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='book_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),  # Book Detail
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),  # Author Detail
    path('genres/', views.GenreListView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', views.GenreDetailView.as_view(), name='genre_detail'),  # Genre Detail
]
