from django.shortcuts import render, redirect
from .models import Student, GateLog
from .forms import StudentForm, AddFeesForm
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
import qrcode
from django.utils import timezone


# Create your views here.
@login_required()
def students(request):
    if request.user.department != 'Admin':
        return redirect('accounts:scan_code')

    students = Student.objects.all().order_by('-id')
    
    context = {
        'students': students
    }

    return render(request, 'students/students.html', context)

@login_required()
def student(request, id):
    student = Student.objects.get(id=id)
    borrowed_books = student.borrowed.filter(status='Borrowed').count()

    if request.user.department == 'Gate':
        if not student.onCampus:
            GateLog.objects.create(
                student=student,
                arrival=timezone.now()
            )
            student.onCampus = True
            student.save()
        else:
            log = GateLog.objects.filter(student=student).order_by('-id').first()
            log.departure = timezone.now()
            log.save()
            student.onCampus = False
            student.save()
    

    logs = GateLog.objects.filter(student=student).order_by('-id')

    context = {
        'student': student,  
        'borrowed_books': borrowed_books,
        'logs': logs 
    }
    return render(request, 'students/student.html', context)

@login_required()
def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.success(request, 'Student successfully deleted')
    return redirect('students:students')

@login_required()
def edit(request, id):
    if request.user.department != 'Admin':
        return redirect('accounts:scan_code')

    student = Student.objects.get(id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Changes saved')
            return redirect('students:student', student.id)
        messages.error(request, 'Error saving changes')
    else:
        form = StudentForm(instance=student)

    context = {
        'form': form,
    }
    return render(request, 'students/edit.html', context)
    
@login_required()
def new(request):
    if request.user.department != 'Admin':
        return redirect('accounts:scan_code')

    if request.method == 'POST':
        form = StudentForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            new_student = form.save()
            messages.success(request, "Saved successfully")
            return redirect('students:student_qr_code', new_student.id)
        messages.error(request, 'Form not valid')
    else:
        form = StudentForm()

    context = {
        'form': form,
    }

    return render(request, 'students/new.html', context)


@login_required()
def add_fees(request):
    if request.user.department != 'Admin':
        return redirect('accounts:scan_code')

    if request.method == 'POST':
        form = AddFeesForm(request.POST)

        if form.is_valid(): 
            amount, student = form.get_info() 
            student.balance = float(student.balance) + float(amount)
            student.save()
            return redirect('students:student', student.id)
 
        messages.error(request, 'Form not valid')
    else:
        form = AddFeesForm()

    context = {
        'form': form,
    }

    return render(request, 'students/add_fees.html', context)



@login_required()
def student_qr_code(request, id):
    student = Student.objects.get(id=id)

    data = student.id
    img = qrcode.make(data)
    img.save(f'./static/qr_codes/qrCode{student.id}.png')

    target = f'qr_codes/qrCode1.png'
    
    context = {
        'student': student,
        'target': target
    }

    return render(request, 'students/student_qr_code.html', context)


@login_required()
def gate_logs(request):
    logs = GateLog.objects.all().order_by('-id')

    context = {
        'logs': logs 
    }
    return render(request, 'students/gate_logs.html', context)