from django.contrib import admin
from .models import Book, BookBorrowed

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(BookBorrowed)
class BookBorrowedAdmin(admin.ModelAdmin):
    list_display = ('book', 'student', 'date_borrowed', 'status')