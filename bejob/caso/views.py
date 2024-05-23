from django.shortcuts import render, redirect
from .models import Tarea
# Create your views here.


def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'caso/lista_tareas.html', {'tareas': tareas})

def anadir_tarea(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion')
        Tarea.objects.create(titulo=titulo, descripcion=descripcion)
        return redirect('lista_tareas')
    return render(request, 'caso/anadir_tarea.html')

def completada(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.completada = True
    tarea.save()
    return redirect('lista_tareas')

def eliminar_tarea(request, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.delete()
    return redirect('lista_tareas')