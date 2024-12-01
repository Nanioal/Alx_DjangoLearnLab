from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet, BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookListView.as_view(), name='book-list'), # ListView 
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'), # DetailView 
    path('books/new/', BookCreateView.as_view(), name='book/create'), # CreateView 
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book/update'), # UpdateView 
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book/delete'), # DeleteView 
    ]

