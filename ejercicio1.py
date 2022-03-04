# Ordenación por inserción dicotómica:
import random
listainicial = []
def generarlista(n):
  while len(listainicial) < n:
    listainicial.append(random.randint(0,100))
generarlista(int(input("Introduzca cuántos elementos desea que tenga su lista: ")))
print("Tu lista inicial es la siguiente: " + str(listainicial))
lista = sorted(listainicial)
orden = len(lista)
listadicotomia = []
print("Tu lista inicial ordenada es la siguiente: " + str(lista))
retroceso = 0
def dicotomia(longitud,retroceso):
  if  len(listadicotomia) <= orden//2:
    retroceso += 1  
    listadicotomia.append(lista.pop(round(longitud / 2)-retroceso))
    dicotomia(orden, retroceso)
  elif len(listadicotomia) > orden // 2 and len(lista) > 0:
    listadicotomia.append(lista.pop(0))
    dicotomia(longitud, retroceso)
dicotomia(orden,retroceso)
print("Esta es la lista obtenida mediante la dicotomía: " + str(listadicotomia))