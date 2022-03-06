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
listainicial =  [12, 96, 11, 53, 157, 118, 40, 198, 200, 113, 85, 125, 138, 109, 141, 102, 167, 128, 114, 168]
print(listainicial)
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

def generarsegmento(p,n, i):
  while (n+i+1)<len(listainicial) and listainicial[n+i+1]<=listainicial[n+i] and p<=20:
    resultado[p].append(listainicial[indicemax+i+1])
    i += 1
    print(resultado)
  else:
    p = 2
    while  p <= n:
      resultado[p].append(listainicial[indicemax+i+1])
      i += 1
      p +=1 
    
    listainicial.index(max(listainicial))
    
  print(resultado)

    
generarsegmento(1, indicemax, 0)