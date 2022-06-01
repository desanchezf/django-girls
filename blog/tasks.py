
from celery import shared_task

"""
    Hay que implementar para celery la funcionalidad que 
    está desarrollada en la vista para que sea desempeñada por
    por el worker de Celery.
"""

@shared_task(name="Suma 3 mas 2")
def add(x, y) -> int: 
    
    print("Se ha añadido una nueva entrada al blog")
    print(x+y)

    return x + y


