"""
creamos un archivo nuevo 
Gguardamos en la carpeta del repositorio con la extension .py
uso de numeros aleatorios

#importamos la libreria randint
"""

from random import randint #random es el modulo y randint la libreria
aleatorio=randint(0,20) #creamos una variable y generamos un numero al azar
print(aleatorio)


#ejercicio
#escribir una funcion sorteo() que reciba una lista de participantes y elegir a uno de los participantes
#aleatoriamente y retornar esa persona aelgida
#desafio: no volver a retornar una persona ya sorteada
"""
from random import randint   #
def sorteo(lista):
    cant_part=len(lista)
    ganadores=randint(0,cant_part-1)
    return lista[ganadores]
    print(lista[ganadores])

lista=["Vale","Kami","Sara","Ale","Dulce"]
sorteo(lista)

"""
from random import randint   
def sorteo(lista):
    cant_part=len(lista)
    ganador=randint(0,cant_part-1)
    return lista[ganador]
    print(lista[ganador])


lista=["Vale","Kami","Sara","Ale","Dulce"]
sorteo(lista)







from random import randint
