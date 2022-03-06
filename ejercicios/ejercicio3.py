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

def diccionariolistas(j):
    diccionario = {}
    for i in range(1, j + 1):
        diccionario[i] = []
    return diccionario
resultado = diccionariolistas(len(listainicial))
print(resultado)
# Este programa va a extraer segmentos decrecientes de la lista generada.
indicemax = listainicial.index(max(listainicial))
resultado[1].append(listainicial[indicemax])
print(resultado[1])

def generarsegmento1(n, i):
  if (n+i+1)<len(listainicial) and listainicial[n+i+1]<=listainicial[n+i]:
    resultado[1+i].append(listainicial[indicemax+i+1])
    generarsegmento1(n, i +1)
  else:
    print(resultado)
    

generarsegmento1(indicemax, 0)