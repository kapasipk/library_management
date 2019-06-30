from rest_framework import serializers
from lib_app.models import Book

# Serializers define the API representation.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'isbn', 'authors', 'number_of_pages', 'publisher', 'country', 'release_date')
