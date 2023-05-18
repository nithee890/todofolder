from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import task1
from .models import todo
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import UpdateView

class tasklistview(ListView):
    model = todo
    template_name = 'home.html'
    context_object_name = 'task1'


class taskdetailview(DetailView):
    model = todo
    template_name = 'detail.html'
    context_object_name = 'task'


class taskupdateview(UpdateView):
    model = todo
    template_name = 'update.html'
    context_object_name = 'task1'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})


class taskdeleteview(DeleteView):
    model = todo
    template_name = 'delete.html'
    context_object_name = 'task1'
    success_url = reverse_lazy('cbvhome')


# Create your views here.
def home(request):
    obj = todo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = todo(name=name, priority=priority, date=date)
        task.save()

    return render(request, 'home.html', {'task1': obj})


def delete(request, task_id):
    task = todo.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = todo.objects.get(id=id)
    form = task1(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'task': task1, 'form': form})
