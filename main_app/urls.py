from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtodo/', views.TodoCreate.as_view(), name='add_todo'),
    # path('deletetodo/<int:id>', views.delete_todo, name='delete_todo')
]