from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from .models import Todo

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    return render(request, 'index.html', {'todos': todos})

class TodoCreate(CreateView):
  model = Todo
  fields = "__all__"

# def delete_todo(request, id):
#     Todo.objects.get(id=id).delete()
#     return redirect('/')

