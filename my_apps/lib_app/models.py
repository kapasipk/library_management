import uuid
from django.db import models
from datetime import datetime

def generate_id():
    return str(uuid.uuid4()).split("-")[-1] 

class Author(models.Model):
    id    = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name  = models.CharField(max_length=255)
 
    def __str__(self):
        return "{}".format(self.id)

class Book(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name            = models.CharField(max_length=255)
    number_of_pages = models.CharField(max_length=255)
    release_date    = models.DateField()
    isbn            = models.CharField(max_length=50)
    publisher       = models.CharField(max_length=255)
    country         = models.CharField(max_length=100)
    authors         = models.ManyToManyField(Author)
    created         = models.DateTimeField(auto_now=True)
    modified        = models.DateTimeField(auto_now_add=True)
    deleted         = models.DateTimeField(default=None, null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.deleted = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.save()

    def __str__(self):
        return "{} - {}".format(self.name, self.id)

    class Meta:
        ordering = ["-created"]
