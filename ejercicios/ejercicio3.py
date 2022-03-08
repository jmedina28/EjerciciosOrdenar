# Completar las especificaciones:
# Para la realización de este ejercicio voy a reutilizar una parte del código del primero.

listainicial =  [12, 11, 10, 53, 157, 118, 40, 198, 200, 113, 85, 125, 138, 109, 141, 102, 167, 128, 114, 168]
print(listainicial)

def diccionariolistas(j):
    diccionario = {}
    for i in range(1, j + 1):
        diccionario[i] = []
    return diccionario
resultado = diccionariolistas(len(listainicial))
print(resultado)
# Este programa va a extraer segmentos decrecientes de la lista generada.
resultado[1].append(listainicial.pop(0))
def generarsegmento(n,p):
  if n<=20 and p<20 and resultado[n][p] >= listainicial[0]:
    resultado[n].append(listainicial.pop(0))
    print(resultado)
    print(n,p)
    if n<20 and p<20 and len(listainicial)>0:
      generarsegmento(n,p+1)
    else:
      print(resultado)
  elif n<20 and p<=20 and resultado[n][p] < listainicial[0]:
    resultado[n+1].append(listainicial.pop(0))

    if n<20 and p<20 and len(listainicial)>0:
      generarsegmento(n+1,0)
    else:
      print(resultado)

  
generarsegmento(1,0)