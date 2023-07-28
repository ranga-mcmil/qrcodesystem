from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
   path('', views.students, name='students'),   
   path('<int:id>/', views.student, name='student'),
   path('delete/<int:id>/', views.delete, name='delete'),
   path('edit/<int:id>/', views.edit, name='edit'),
   path('new/', views.new, name='new'), 
   path('add_fees/', views.add_fees, name='add_fees'), 
   path('student_qr_code/<int:id>/', views.student_qr_code, name='student_qr_code'), 
   path('gate_logs/', views.gate_logs, name='gate_logs')   
]