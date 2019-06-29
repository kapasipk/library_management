from lib_app.models import Book
from django.shortcuts import render
from lib_app.serializers import BookSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

# ViewSets define the view behavior.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        books = Book.objects.filter(deleted=None)
        filter_attrs = ['name', 'country', 'publisher', 'release_date']
        for attr in filter_attrs:
            val = self.request.query_params.get(attr, None)
            if val is not None:
                books = books.filter(**{attr: val})
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
