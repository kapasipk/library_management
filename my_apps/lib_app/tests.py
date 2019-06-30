import json
from faker import Faker
from random import randint
from .models import Book, Author
from django.test import TestCase
from rest_framework.test import APIClient

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

    def test_crud_apis(self):
      self.fake = Faker()    
      client = APIClient()

      # Test create API 
      response = client.post(
                  '/api/v1/books/', 
                  {
                        'name' : self.fake.first_name(),
                        'isbn' : str(randint(1, 10)),
                        'number_of_pages' : randint(1, 100),
                        'publisher' : self.fake.name(),
                        'country' : self.fake.country(),
                        'authors': [
                              self.fake.name(),
                              self.fake.name(),
                        ],
                        'release_date' : self.fake.date()
                  }, 
                  format='json')
      self.assertEqual(response.status_code, 200)
      response = json.loads(response.content)
      serializer_attrs = ['id', 'name', 'isbn', 'authors', 'number_of_pages', 'publisher', 'country', 'release_date']
      for attr in serializer_attrs:
            self.assertIn(attr, response)
      id = response['id']

      # Test get_object API
      response = client.get('/api/v1/books/' + id + '/')
      self.assertEqual(response.status_code, 200)
      response = json.loads(response.content)
      for attr in serializer_attrs:
            self.assertIn(attr, response)

      # Test list API
      response = client.get('/api/v1/books/')
      self.assertEqual(response.status_code, 200)
      response = json.loads(response.content)
      self.assertEqual(len(response), 1)
      response = response[0]
      for attr in serializer_attrs:
            self.assertIn(attr, response)

      # Test list API with filters
      response = client.get('/api/v1/books/', {'name': response['name'], 'publisher': response['publisher']})
      self.assertEqual(response.status_code, 200)
      response = json.loads(response.content)
      self.assertEqual(len(response), 1)
      response = response[0]
      for attr in serializer_attrs:
            self.assertIn(attr, response)

      # Test list API with filters
      response = client.get('/api/v1/books/', {'name': 'Hello world'})
      self.assertEqual(response.status_code, 200)
      response = json.loads(response.content)
      self.assertEqual(len(response), 0)

      # Test PUT API
      new_name = self.fake.name()
      response = client.patch(
                  '/api/v1/books/' + id + '/',
                  {
                        'name' : new_name
                  }, 
                  format='json'
            )
      self.assertEqual(response.status_code, 200)
      response = json.loads(response.content)
      for attr in serializer_attrs:
            self.assertIn(attr, response)
      self.assertEqual(response['name'], new_name)

      # Test DELETE API
      response = client.delete('/api/v1/books/' + id + '/')
      self.assertEqual(response.status_code, 204)

    def test_external_api(self):
      client = APIClient()
      response = client.get('/api/external-books/')
      self.assertEqual(response.status_code, 200)
      response = json.loads(response.content)
      self.assertEqual(len(response), 10)
      
      response = client.get('/api/external-books/', {'name': 'A Game of Thrones'})
      self.assertEqual(response.status_code, 200)
      response = json.loads(response.content)
      self.assertEqual(len(response), 1)

      response = response[0]
      serializer_attrs = ['name', 'isbn', 'authors', 'number_of_pages', 'publisher', 'country', 'release_date']
      for attr in serializer_attrs:
            self.assertIn(attr, response)
