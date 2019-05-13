"""
juego de adivinar el numero, todos juntos adivinar un numero generado aleatoriamente e ir introducciendo
por teclado el dato a adivinar

"""
from random import randint
generado=randint(0,10)
print(generado)
condicion=True
intento=10
while condicion:
    if intento>0:
        numero=intento-1
        if generado==int(numero):
            print("Ganaste una anvorguesa que Lore paga")
            condicion=False
        else:
            print("El perdedor compra pizza a Lore")
            print("Te quedan",intento"intentos")
        else:
            condicion=False
            print("perdiste")