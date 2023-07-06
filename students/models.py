from django.db import models

STATUS = (
    ("Enrolled", "Enrolled"),
    ("Completed", "Completed"),
    ("Deferred", "Deferred"),
)

SEX = (
    ("Male", "Male"),
    ("Female", "Female"),    
)


LEVEL = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
)

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    programme = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    sex = models.CharField(max_length=10, choices=SEX)
    status = models.CharField(max_length=50, choices=STATUS)
    level = models.CharField(max_length=10, choices=LEVEL)
    balance = models.DecimalField(default=0, decimal_places=2, max_digits=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'