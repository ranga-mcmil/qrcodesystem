from django.db import models
from students.models import Student

# Create your models here.
STATUS = (
    ("Borrowed", "Borrowed"),
    ("Returned", "Returned"),
)

class Book(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BookBorrowed(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrowed")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="borrowed")
    date_borrowed = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS, default='Borrowed')
    

