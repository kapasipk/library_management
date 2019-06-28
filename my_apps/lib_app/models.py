from django.db import models
import uuid
from django.contrib.auth.models import User

def generate_id():
    return str(uuid.uuid4()).split("-")[-1] 

class Book(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name            = models.CharField(max_length=255)
    number_of_pages = models.CharField(max_length=255)
    release_date    = models.DateTimeField()
    isbn            = models.CharField(max_length=50)
    publisher       = models.CharField(max_length=255)
    country         = models.CharField(max_length=100)
    created         = models.DateTimeField(auto_now=True)
    modified        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.id)

    def save(self, *args, **kwargs):
        if len(self.id.strip(" "))==0:
            self.id = generate_id()

        super(Book, self).save(*args, **kwargs) # Call the real   save() method

    class Meta:
        ordering = ["-created"]
