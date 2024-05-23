from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('anadir_tarea/', views.anadir_tarea, name='anadir_tarea'),
    path('completada/<int:tarea_id>/', views.completada, name='completada'),
    path('delete/<int:tarea_id>/', views.eliminar_tarea, name='eliminar_tarea')
]