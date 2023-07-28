from django.contrib import admin
from .models import Student, GateLog

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

@admin.register(GateLog)
class GateLogAdmin(admin.ModelAdmin):
    list_display = ('student', 'arrival', 'departure')