from lib_app.models import Book
from django.shortcuts import render
from lib_app.serializers import BookSerializer
from rest_framework import routers, serializers, viewsets

# ViewSets define the view behavior.
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
