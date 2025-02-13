from django.contrib import admin
from .models import Book, Author, Genre

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'copies_available')  # Show copies in admin list
    search_fields = ('title', 'isbn')
    list_filter = ('genre',)
    fieldsets = (
        ('Book Details', {'fields': ('title', 'author', 'summary', 'isbn', 'genre', 'copies_available')}),
    )

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    search_fields = ('first_name', 'last_name')
    fieldsets = (
        ('Author Details', {'fields': ('first_name', 'last_name', 'date_of_birth', 'date_of_death')}),
    )

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
