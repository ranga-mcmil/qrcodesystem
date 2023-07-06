from django import forms
from .models import STATUS, Book, BookBorrowed
from students.models import Student

class BookForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'name',
        }
    ))

    class Meta:
        model = Book
        fields = ('name', )


class BookBorrowedForm(forms.ModelForm):
    book = forms.ModelChoiceField(queryset=Book.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    student = forms.ModelChoiceField(queryset=Student.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    status = forms.ChoiceField(choices=STATUS, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = BookBorrowed
        fields = ('book', 'student', 'status')
