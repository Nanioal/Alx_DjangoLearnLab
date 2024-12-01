from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

def home_view(request):
    return HttpResponse("Welcome to the Advanced API Project")
def example_view(request): 
    return render(request, 'example_template.html')
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# Create your views here.
