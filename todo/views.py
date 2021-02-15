from django.shortcuts import render
from .models import TodoModel
from django.views.generic import ListView,CreateView,DeleteView,UpdateView, DetailView
from django.urls import reverse_lazy

class TodoView(ListView):
    model = TodoModel
    template_name = "todo/list.html"

class TododetailView( DetailView):
    model = TodoModel
    template_name = "todo/tododetail.html"

class TodoCreateView(CreateView):  
    model = TodoModel 
    template_name = "todo/create.html"
    fields = ['title', 'content', 'pic']
    success_url = reverse_lazy('list')

class TodoDeleteView(DeleteView):
    model = TodoModel
    template_name = "todo/delete.html"
    success_url = reverse_lazy('list')

class TodoUpdateView(UpdateView):
    model = TodoModel
    template_name = "todo/update.html"
    fields = ['title', 'content', 'pic']
    success_url = reverse_lazy('list')
