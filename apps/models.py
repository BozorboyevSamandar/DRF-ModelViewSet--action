from django.db import models


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year_birth = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    year_writing = models.DateField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title

