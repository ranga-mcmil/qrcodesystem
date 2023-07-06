from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
   path('', views.books, name='books'),   

   path('new/borrow/', views.borrow_new, name='borrow_new'), 
   path('list/borrow/', views.borrow_list, name='borrow_list'),
   path('edit/borrow/<int:id>', views.borrow_edit, name='borrow_edit'), 
]