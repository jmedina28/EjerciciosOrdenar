<h1 align="center">Ordenar</h1>

<h3 align="center">Perfil de GitHub del autor de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)

---
En este [repositorio](https://github.com/jmedina28/EjerciciosOrdenar) quedan resueltos los ejercicios de ordenar. Para llevar a cabo el proyecto me he documentado a través de los ejemplos dados y la teoría que se encuentra en el campus virtual.

## Ejercicio 1: Ordenación por inserción dicotómica

El código empleado para resolverlo es el siguiente:

```python

# Ordenación por inserción dicotómica:
import random
listainicial = []
def generarlista(n, i):
  j = i.split("-")
  while len(listainicial) < n:
    listainicial.append(random.randint(int(j[0]),int(j[1])))
generarlista(int(input("Introduzca cuántos elementos desea que tenga su lista: ")), 
str(input("""Introduzca el intervalo que desea que abarque la lista generada. 
Para ello escríbalo tal y como se muestra en el ejemplo dado.
- Ejemplo: 0-100
- Introduzca su intervalo: """)))
print("Tu lista inicial es la siguiente: " + str(listainicial))
lista = sorted(listainicial)
orden = len(lista)
listadicotomia = []
print("Tu lista inicial ordenada es la siguiente: " + str(lista))
retroceso = 0
def dicotomia(longitud,retroceso):
  if  len(listadicotomia) < orden//2:
    retroceso += 1  
    listadicotomia.append(lista.pop(round(longitud / 2)-retroceso))
    dicotomia(orden, retroceso)
  elif len(listadicotomia) >= orden // 2 and len(lista) > 0:
    listadicotomia.append(lista.pop(0))
    dicotomia(longitud, retroceso)
dicotomia(orden,retroceso)
print("Esta es la lista obtenida mediante la dicotomía: " + str(listadicotomia))
```

## Ejercicio 2: Una ordenación topológica

El código empleado para resolverlo es el siguiente:
 
 ```python
 
```
## Ejercicio 3: Completar las especificaciones

El código empleado para resolverlo es el siguiente:
 
 ```python

```
