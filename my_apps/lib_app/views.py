from lib_app.models import Book, Author, ExternalBook
from django.shortcuts import render
from lib_app.serializers import BookSerializer, ExternalBookSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

import requests

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

    def create(self, request):
        authors_data = request.data.pop('authors')
        bookObj = Book.objects.create(**request.data)
        for author_data in authors_data:
            bookObj.authors.create(name=author_data)
        serializer = self.get_serializer(bookObj, many=False)
        return Response(serializer.data)

    def get_object(self):
        obj = super(BookViewSet, self).get_object()
        # if obj.deleted is not None:
        #     return Response(status=status.HTTP_404_NOT_FOUND)
        return obj

class ExternalBookViewSet(viewsets.ModelViewSet):
    queryset = ExternalBook.objects.all()
    serializer_class = ExternalBookSerializer

    def list(self, request):
        query_data = {}
        filter_attrs = ['name', 'country', 'publisher', 'release_date']
        for attr in filter_attrs:
            val = self.request.query_params.get(attr, None)
            if val is not None:
                query_data[attr] = val
        r = requests.get('https://www.anapioficeandfire.com/api/books', query_data)
        books = r.json()
        public_attrs_map = {
            'name'          : 'name',
            'isbn'          : 'isbn',
            'authors'       : 'authors',
            'numberOfPages' : 'number_of_pages',
            'publisher'     : 'publisher',
            'country'       : 'country',
            'released'      : 'release_date'
        }
        data = []
        for book in books:
            bookData = {}
            for k, v in public_attrs_map.items():
                bookData[v] = book[k]
            data.append(bookData)
        return Response(data)
