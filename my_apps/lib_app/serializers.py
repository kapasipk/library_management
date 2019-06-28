from rest_framework import serializers
from lib_app.models import Book

# Serializers define the API representation.
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'isbn', 'number_of_pages', 'publisher', 'country', 'release_date')
