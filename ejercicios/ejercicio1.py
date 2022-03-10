# Ordenación por inserción dicotómica:
import random

listainicial = []

def generarlista(n, i):
    j = i.split("-")
    while len(listainicial) < n:
        listainicial.append(random.randint(int(j[0]), int(j[1])))


generarlista(int(input("Introduzca cuántos elementos desea que tenga su lista: ")),
             str(input("""Introduzca el intervalo que desea que abarque la lista generada. 
Para ello escríbalo tal y como se muestra en el ejemplo dado.
- Ejemplo: 0-100
- Introduzca su intervalo: """)))
print("Tu lista inicial es la siguiente: " + str(listainicial))

listadicotomia, lista, orden, retroceso = [], [], len(listainicial), 0

def ordenarlista(l):
  if len(listainicial) > 0:
    minimo = l.index(min(l))
    lista.append(listainicial.pop(minimo))
    ordenarlista(listainicial)


ordenarlista(listainicial)
print("Tu lista inicial ordenada es la siguiente: " + str(lista))

def dicotomia(longitud, retroceso):
    if len(listadicotomia) < orden//2:
        retroceso += 1
        listadicotomia.append(lista.pop(round(longitud / 2)-retroceso))
        dicotomia(orden, retroceso)
    elif len(listadicotomia) >= orden // 2 and len(lista) > 0:
        listadicotomia.append(lista.pop(0))
        dicotomia(longitud, retroceso)


dicotomia(orden, retroceso)
print("Esta es la lista obtenida mediante la dicotomía: " + str(listadicotomia))