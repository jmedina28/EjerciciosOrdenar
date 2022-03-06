# Una ordenación topológica:
# uso la función de generar j listas dentro de un diccionario del ejercicio 3:
import random

listatareas = ["Limpiar el suelo", "Doblar ropa","Lavar ropa", "Dejar la comida preparada", "Dar de comer a la mascota", "Estudiar","Ir a comprar", "Sacar a la calle a la mascota"]

def diccionariolistas(j):
    diccionario = {}
    for i in range(1, j + 1):
        diccionario[i] = []
    return diccionario
resultado = diccionariolistas(len(listatareas))
print(resultado)
def rellenarlistas(n):
  while n<=len(listatareas):
    resultado[n].append(random.randint(0,10))
    n+=1
rellenarlistas(1)
print(resultado)
print(list(resultado.values()))
print(listatareas)