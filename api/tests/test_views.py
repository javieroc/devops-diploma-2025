from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book
from datetime import date

class BookViewTest(APITestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title="Demo",
            author="Author",
            isbn="1234567890123",
            published_date=date.today()
        )

    def test_get_books(self):
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        body = response.json()
        returned_book = body[0]
        self.assertEqual(returned_book["title"], self.book.title)
        self.assertEqual(returned_book["author"], self.book.author)
        self.assertEqual(returned_book["isbn"], self.book.isbn)
        self.assertEqual(returned_book["published_date"], self.book.published_date.strftime('%Y-%m-%d'))

    def test_create_book(self):
        url = reverse('api:books')
        data = {
            "title": "New Book",
            "author": "New Author",
            "isbn": "9876543210987",
            "published_date": "2025-07-30"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        new_book = Book.objects.get(isbn="9876543210987")
        self.assertEqual(new_book.title, "New Book")


class HealthViewTest(APITestCase):

    def test_response_is_correct(self):
        url = reverse('api:health')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        body = response.json()
        self.assertEqual(body['status'], 'ok')
