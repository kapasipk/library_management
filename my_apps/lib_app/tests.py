from django.test import TestCase

from .models import Book, Author
from faker import Faker
from random import randint

class BookViewSetTestCase(TestCase):
    def test_create_book(self):
       self.fake = Faker()
       params = {
            'name' : self.fake.first_name(),
            'isbn' : str(randint(1, 10)),
            'number_of_pages' : randint(1, 100),
            'publisher' : self.fake.name(),
            'country' : self.fake.country(),
            'release_date' : self.fake.date()
       }
       book = Book.objects.create(**params)
       name1 = self.fake.name()
       name2 = self.fake.name()
       book.authors.create(name=name1)
       book.authors.create(name=name2)
       self.assertEqual(book.authors.count(), 2)
       self.assertEqual(Book.objects.count(), 1)

