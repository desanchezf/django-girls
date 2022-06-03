
from celery import shared_task
from .models import Post

"""
    Hay que implementar para celery la funcionalidad que 
    está desarrollada en la vista para que sea desempeñada por
    por el worker de Celery.

    El decorador @shared_task no necesita de una instancia
    de Celery para la ejecución de la tarea. 

"""

@shared_task(name="add_task()")
def add_task(): 

    print("Se ha ejecutado una shared task a la hora de crear un post")

