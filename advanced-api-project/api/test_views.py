from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.author = Author.objects.create(name='Author Test')
        self.book = Book.objects.create(title='Book Test', publication_year=2022, author=self.author)

        # Authenticate the user
        self.client.login(username='testuser', password='testpass')
    
    def test_create_book(self):
        url = reverse('book-create')
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, 'New Book')

    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Book Test')

    def test_update_book(self):
        url = reverse('book-update', kwargs={'pk': self.book.pk})
        data = {
            'title': 'Updated Book',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        url = reverse('book-delete', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        url = reverse('book-list')
        response = self.client.get(url, {'title': 'Book Test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        url = reverse('book-list')
        response = self.client.get(url, {'search': 'Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        Book.objects.create(title='Another Book', publication_year=2020, author=self.author)
        url = reverse('book-list')
        response = self.client.get(url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Another Book')

