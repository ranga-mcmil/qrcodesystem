from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, UserRegistrationForm, UserUpdateForm, AddUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from .models import User
from students.models import Student

# Create your views here.
@login_required()
def dashboard(request):

    if request.user.department != 'Admin':
        return redirect('accounts:scan_code')

    context = {
        'students': Student.objects.all().count,
        'users': User.objects.all().count
    }
    
    return render(request, 'accounts/dashboard.html', context)


class PasswordChangeView(PasswordChangeView):
    form_class = MyPasswordChangeForm
    template_name = "registration/password_change_form.html"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Password updated successfully")
        return super(PasswordChangeView, self).form_valid(form)

def login_view(request):
    if request.POST:
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You are now logged in as {user.get_full_name()}')
            return redirect('accounts:dashboard')
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'registration/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, f'Registration Successful. You are now logged in as {user.get_full_name()}')
            return redirect('accounts:dashboard')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})



def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, f'User Added Successfully.')
            return redirect('accounts:dashboard')
    else:
        form = AddUserForm()

    return render(request, 'registration/add_user.html', {'form': form})

def scan_code(request):
    
    context = {

    }

    return render(request, 'accounts/scan_code.html', context)

@login_required()
def users(request):
    
    users = User.objects.all().exclude(id=request.user.id)

    context = {
        'users': users
    }

    return render(request, 'accounts/users.html', context)



@login_required
def profile_edit(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Changes Saved Successfully")
            return redirect('accounts:dashboard')
        messages.warning(request, "Something happened")
    else:
        form = UserUpdateForm(instance=user)

    context = {
        'form': form,
    }

    return render(request, 'accounts/profile_edit.html', context)


def my_logout(request):
    logout(request)
    messages.success(request, "You have successfully signed out")
    return redirect('accounts:dashboard')
