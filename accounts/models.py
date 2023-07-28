from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

DEPARTMENT = (
    ("Library", "Library"),
    ("Gate", "Gate"),  
    ("Examinations", "Examinations"),  
    ("Admin", "Admin"),  
)

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    department = models.CharField(max_length=20, choices=DEPARTMENT, default='Admin')

    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)

