from django.shortcuts import render, redirect
from .forms import BookForm, BookBorrowedForm
from django.contrib.auth.decorators import login_required
from .models import Book, BookBorrowed
from django.contrib import messages


# Create your views here.
@login_required()
def books(request):
    if request.user.department != 'Admin' and request.user.department != 'Library':
        return redirect('accounts:scan_code')
        
    if request.method == 'POST':
        form = BookForm(data=request.POST)

        if form.is_valid():
            new_book = form.save()
            messages.success(request, "Saved successfully")
            return redirect('library:books')
        messages.error(request, 'Form not valid')
    else:
        form = BookForm()
        books = Book.objects.all().order_by('-id')

    context = {
        'form': form,
        'books': books
    }

    return render(request, 'library/books.html', context)

@login_required()
def borrow_list(request):
    if request.user.department != 'Admin' and request.user.department != 'Library':
        return redirect('accounts:scan_code')

    borrowed_books = BookBorrowed.objects.all().order_by('-id')
    
    context = {
        'borrowed_books': borrowed_books
    }

    return render(request, 'library/borrow_list.html', context)


@login_required()
def borrow_new(request):
    if request.user.department != 'Admin' and request.user.department != 'Library':
        return redirect('accounts:scan_code')

    if request.method == 'POST':
        form = BookBorrowedForm(data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Saved successfully")
            return redirect('library:borrow_list')
        messages.error(request, 'Form not valid')
    else:
        form = BookBorrowedForm()

    context = {
        'form': form,
    }

    return render(request, 'library/borrow_new.html', context)

@login_required()
def borrow_edit(request, id):
    if request.user.department != 'Admin' and request.user.department != 'Library':
        return redirect('accounts:scan_code')

    book_borrowed = BookBorrowed.objects.get(id=id)

    if request.method == 'POST':
        form = BookBorrowedForm(request.POST, instance=book_borrowed)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes saved')
            return redirect('library:borrow_list')
        messages.error(request, 'Error saving changes')
    else:
        form = BookBorrowedForm(instance=book_borrowed)

    context = {
        'form': form,
    }
    return render(request, 'library/borrow_edit.html', context)