listainicial =  [12, 96, 11, 53, 157, 118, 40, 198, 200, 113, 85, 125, 138, 109, 141, 102, 167, 128, 114, 168]
print(listainicial)
def diccionariolistas(j):
    diccionario = {}
    for i in range(1, j + 1):
        diccionario[i] = []
    return diccionario
resultado = diccionariolistas(len(listainicial))
print(resultado)
def colocarelementos(i, j):
  resultado[j].append(listainicial[i])
  if i<len(listainicial) and listainicial[i]>= listainicial[i+1]:
    resultado[j].append(listainicial[i+1])
    
    colocarelementos(i+1,j+1)
  elif listainicial[i]< listainicial[i+1] and i<len(listainicial):
    colocarelementos(i,j+1)
colocarelementos(0,1)
print(resultado)

  