<h1 align="center">Ordenar</h1>

<h3 align="center">Perfil de GitHub del autor de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)

---
En este [repositorio](https://github.com/jmedina28/EjerciciosOrdenar) quedan resueltos los ejercicios de ordenar. Para llevar a cabo el proyecto me he documentado a través de los ejemplos dados y la teoría que se encuentra en el campus virtual.
***
## Índice
1. [Ordenación por inserción dicotómica.](#id1)
3. [Una ordenación topológica.](#id2)
3. [Completar las especificaciones.](#id3)
***

## Ejercicio 1: Ordenación por inserción dicotómica<a name="id1"></a>

En este ejercicio, he creado un programa que genera una lista aleatoria de n valores y de cierto rango introducido por el usuario, la ordena de menor a mayor y posteriormente la recoloca empleando la dicotomía.

Este es su [Milestone](https://github.com/jmedina28/EjerciciosOrdenar/milestone/1).

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

listadicotomia, lista, orden, retroceso = [], [], len(listainicial), 0

def ordenarlista(l):
  if len(l) > 0:
    minimo = l.index(min(l))
    lista.append(l.pop(minimo))
    ordenarlista(l)


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
```
El diagrama de flujo es el siguiente:

<br>
<img height="600" src="flowcharts/Ejer1Flowchart.drawio.jpg" />
<br>

## Ejercicio 2: Una ordenación topológica<a name="id2"></a>

En este ejercicio, he creado un programa que coloca una serie de tareas en orden de prioridad con el uso de diccionarios, asignando a cada tarea u número aleatorio y dando mayor prioridad a la tarea cuanto mayor es el número asignado.

Este es su [Milestone](https://github.com/jmedina28/EjerciciosOrdenar/milestone/2).

El código empleado para resolverlo es el siguiente:
 
 ```python
# Una ordenación topológica:
# uso la función de generar j listas dentro de un diccionario del ejercicio 3:
import random

listatareas = ["Limpiar el suelo", "Doblar ropa","Lavar ropa", "Dejar la comida preparada", "Dar de comer a la mascota", "Estudiar","Ir a comprar", "Sacar a la calle a la mascota"]
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
    while n<=len(listatareas):
      resultado[n].append(random.randint(0,10))
      n+=1
  rellenarlistas(1)
  listavalores, listaordenada = list(resultado.values()), []
  
  def ordenarlista(l):
    if len(l) > 0:
      maximo = l.index(max(l))
      listaordenada.append(l.pop(maximo))
      ordenarlista(l)
    
  
  def ordenprioridad(n):
    if n<len(listatareas):
      listavalores[n].append(listatareas[n])
      ordenprioridad(n+1)
  ordenprioridad(0)
  ordenarlista(listavalores)
  print(listaordenada)
else:
  exit()

```

El diagrama de flujo es el siguiente:

<br>
<img height="600" src="flowcharts/Ejer2Flowchart.drawio.jpg" />
<br>

## Ejercicio 3: Completar las especificaciones<a name="id3"></a>

En este ejercicio, he creado un programa que de una lista aleatoria de n números y de cierto rango introducidos por el usuario extrae todas las sublistas de la misma decrecientes.

Este es su [Milestone](https://github.com/jmedina28/EjerciciosOrdenar/milestone/3).

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
El diagrama de flujo es el siguiente:

<br>
<img height="550" src="flowcharts/Ejercicio3Flowchart.drawio.jpg" />
<br>
