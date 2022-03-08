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