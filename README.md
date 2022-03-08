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
        listainicial.append(random.randint(int(j[0]), int(j[1])))


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
```

## Ejercicio 2: Una ordenación topológica

El código empleado para resolverlo es el siguiente:
 
 ```python
# Una ordenación topológica:
# uso la función de generar j listas dentro de un diccionario del ejercicio 3:
import random

listatareas = ["Limpiar el suelo", "Doblar ropa", "Lavar ropa", "Dejar la comida preparada",
               "Dar de comer a la mascota", "Estudiar", "Ir a comprar", "Sacar a la calle a la mascota"]
print("A continuación se le va a mostrar la lista de tareas pendientes: " + str(listatareas))
variable = int(input("¿Desea que le coloque la lista en orden de prioridad aleatoriamente? En caso afirmativo pulse 1, en caso contrario cualquier otro número: "))

if variable == 1:
    def diccionariolistas(j):
        diccionario = {}
        for i in range(1, j + 1):
            diccionario[i] = []
        return diccionario
    resultado = diccionariolistas(len(listatareas))

    def rellenarlistas(n):
        while n <= len(listatareas):
            resultado[n].append(random.randint(0, 10))
            n += 1
    rellenarlistas(1)
    listavalores = list(resultado.values())

    def asociacion(n):
        if n < len(listatareas):
            listavalores[n].append(listatareas[n])
            asociacion(n+1)
    asociacion(0)
    listaordenada = sorted(listavalores, reverse=True)
    print(listaordenada)
else:
    exit()

```
## Ejercicio 3: Completar las especificaciones

El código empleado para resolverlo es el siguiente:
 
 ```python
# Completar las especificaciones:
# Para la realización de este ejercicio voy a reutilizar una parte del código del primero.
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
x = len(listainicial)


def diccionariolistas(j):
    diccionario = {}
    for i in range(1, j + 1):
        diccionario[i] = []
    return diccionario


resultado = diccionariolistas(len(listainicial))
# Este programa va a extraer segmentos decrecientes de la lista generada.
resultado[1].append(listainicial.pop(0))


def generarsegmento(n, p):
    if n <= x and p < x and resultado[n][p] >= listainicial[0]:
        resultado[n].append(listainicial.pop(0))
        if n < x and p < x and len(listainicial) > 0:
            generarsegmento(n, p+1)
        else:
            print("El resultado es el siguiente: "+str(resultado))
    elif n < x and p <= x and resultado[n][p] < listainicial[0]:
        resultado[n+1].append(listainicial.pop(0))
        if n < x and p < x and len(listainicial) > 0:
            generarsegmento(n+1, 0)
        else:
            print("El resultado es el siguiente: "+str(resultado))


generarsegmento(1, 0)
```
