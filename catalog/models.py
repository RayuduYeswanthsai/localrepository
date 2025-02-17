from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")  # Ensure this exists
    isbn = models.CharField('ISBN', max_length=13)
    genre = models.ManyToManyField('Genre')
    copies_available = models.IntegerField(default=2, help_text="Number of copies available")

    def __str__(self):
        return self.title
