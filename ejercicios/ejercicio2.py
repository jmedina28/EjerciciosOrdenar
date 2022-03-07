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
  listavalores = list(resultado.values())
  def asociacion(n):
    if n<len(listatareas):
      listavalores[n].append(listatareas[n])
      asociacion(n+1)
  asociacion(0)
  listaordenada = sorted(listavalores, reverse= True)
  print(listaordenada)
else:
  exit()
                         
