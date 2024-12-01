from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics, permissions
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated # Add these imports


# ListView for retrieving all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Use IsAuthenticatedOrReadOnly for ListView

# DetailView for retrieving a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Use IsAuthenticatedOrReadOnly for DetailView

# CreateView for adding a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create

# UpdateView for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update

# DeleteView for removing a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete


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



# ListView for retrieving all books
class BookListView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read-only access for unauthenticated users

# DetailView for retrieving a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Provides a get method handler.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read-only access for unauthenticated users

# CreateView for adding a new book
class BookCreateView(generics.CreateAPIView):
    """
    Provides a post method handler.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create

# UpdateView for modifying an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Provides put and patch method handlers.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can update

# DeleteView for removing a book
class BookDeleteView(generics.DestroyAPIView):
    """
    Provides a delete method handler.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can delete

# Create your views here.
