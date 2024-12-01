from django.db import models
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Create your models here.


# The Author model represents an author with a name field
class Author(models.Model):
    name = models.CharField(max_length=100)  # A string field to store the author’s name

    def __str__(self):
        return self.name

# The Book model represents a book with a title, publication year, and a foreign key to the Author model
class Book(models.Model):
    title = models.CharField(max_length=200)  # A string field for the book’s title
    publication_year = models.IntegerField()  # An integer field for the year the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Foreign key linking to the Author model

    def __str__(self):
        return self.title

