from django.shortcuts import render
from django.views import generic
from .models import Book, Author, Genre

def index(request):
    """Home Page"""
    num_books = Book.objects.count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
        'num_genres': num_genres
    }
    return render(request, 'catalog/index.html', context)

class BookListView(generic.ListView):
    model = Book
    template_name = 'catalog/book_list.html'

class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'  # Book Detail Template

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'catalog/author_list.html'

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'catalog/author_detail.html'  # Author Detail Template

class GenreListView(generic.ListView):
    model = Genre
    template_name = 'catalog/genre_list.html'

class GenreDetailView(generic.DetailView):
    model = Genre
    template_name = 'catalog/genre_detail.html'  # Genre Detail Template
