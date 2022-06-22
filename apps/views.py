from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


# Create your views here.

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @action(['GET'], detail=False)
    def find_author(self, request):
        data = self.queryset.filter(last_name='Ahmad')
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(['GET'], detail=False)
    def isbn_book(self, request):
        data = self.queryset.filter(isbn='8465498456549')
        serializer = self.serializer_class(data, many=True)
        return Response(serializer.data)
