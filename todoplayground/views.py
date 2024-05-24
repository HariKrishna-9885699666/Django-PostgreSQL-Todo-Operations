from django.http import HttpResponse
from django.template import loader
from .forms import TodoItemForm
from django.contrib import messages
from .models import TodoItem
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse

def todos(request, task_id=None):
    form = TodoItemForm()
    if task_id and request.method != 'POST' and '/delete/' in request.path:
      try:
          task = TodoItem.objects.get(pk=task_id)
          task.delete()
          messages.success(request, 'Task deleted successfully.')
          return redirect('todos')
      except TodoItem.DoesNotExist:
          messages.error(request, "The task you are trying to edit does not exist.")

    if task_id and '/edit/' in request.path:
        task = None
        if task_id:
            try:
                task = TodoItem.objects.get(pk=task_id)
                form = TodoItemForm(instance=task)
            except TodoItem.DoesNotExist:
                messages.error(request, "The task you are trying to edit does not exist.")

    if request.method == 'POST' and task_id == None:
      form = TodoItemForm(request.POST)
      if form.is_valid():
        task = request.POST['task']

        TodoItem.objects.create(task=task)
        messages.success(request, "Task created successfully.")
        return redirect('todos')
      
    if request.method == 'POST' and task_id and '/edit/' in request.path:
        form = TodoItemForm(request.POST)
        if form.is_valid():
            if task:
                # Update existing task
                task.task = form.cleaned_data['task']
                task.save()
                messages.success(request, 'Task updated successfully.')
                return redirect('todos')
    
    allTasks = TodoItem.objects.all().values().order_by('-id')
    template = loader.get_template('landing-page.html')
    context = {
       'form': form,
       'allTasks': allTasks,
       'is_edit_mode': task_id is not None,
    }
    return HttpResponse(template.render(context, request))
         

def complete_todo(request, task_id=None):
    if task_id and request.method == 'POST' and '/complete/' in request.path:
      try:
          todo = get_object_or_404(TodoItem, pk=task_id)
          todo.completed = not todo.completed
          todo.save()
      except TodoItem.DoesNotExist:
          messages.error(request, "The task you are trying to edit does not exist.")
    return JsonResponse({'success': True})

  
        