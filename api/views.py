from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book
from .serializers import BookSerializer

class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "status": "ok",
            "message": "API is running smoothly"
        })

health_view = HealthView.as_view()


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "status": "ok",
            "message": "Simple test update"
        })

test_view = TestView.as_view()


#
# /api/books - All methods (GET, POST)
#
class BookView(APIView):
    def get(self, request, *args, **kwargs):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = BookSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


book_view = BookView.as_view()

class BookDetailView(APIView):
    def get(self, request, id, *args, **kwargs):
        try:
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book)
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, *args, **kwargs):
        try:
            book = Book.objects.get(id=id)
            serializer = BookSerializer(book, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id, *args, **kwargs):
        try:
            book = Book.objects.get(id=id)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

book_detail_view = BookDetailView.as_view()
