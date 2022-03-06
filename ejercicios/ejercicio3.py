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



# Este programa va a extraer segmentos decrecientes de la lista generada.

orden = len(listainicial)
maximo = max(listainicial)
indicemax = listainicial.index(maximo)
segmento1= []
def generarsegmento1(n, i):
  segmento1.append(listainicial[n])
  if listainicial[n+i]<listainicial[n] and ((n+len(segmento1)))<=len(listainicial):
    segmento1.append(listainicial[n+1])
    print(segmento1)
    generarsegmento1(n+len(segmento1), 1)
   
  
generarsegmento1(indicemax, 1)




    