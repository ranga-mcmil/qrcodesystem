from django import forms
from .models import Student, SEX, LEVEL, STATUS

# Custom widget
class DateInput(forms.DateInput):
    input_type = 'date'

    
class StudentForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'first_name',
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'last_name',
        }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'name': 'email',
        }
    ))

    address = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'address',
        }
    ))

    programme = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'name': 'programme',
        }
    ))

    date_of_birth = forms.DateField(widget=DateInput)

    sex = forms.ChoiceField(choices=SEX, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    status = forms.ChoiceField(choices=STATUS, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    level = forms.ChoiceField(choices=LEVEL, widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))

    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'email', 'address', 'programme', 'date_of_birth', 'sex', 'status', 'level')


class AddFeesForm(forms.Form):
    amount = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'type': 'number'
        }
    ))

    student = forms.ModelChoiceField(queryset=Student.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control',
        }
    ))




    def get_info(self):
        """
        Method that returns formatted information
        :return: subject, msg
        """
        # Cleaned data
        cl_data = super().clean()
        amount = cl_data.get('amount')
        student = cl_data.get('student')

        return amount, student
