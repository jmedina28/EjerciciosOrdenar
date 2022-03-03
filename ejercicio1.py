# Ordenación por inserción dicotómica:
"""Tengo que hacer lo siguiente:
- Respecto a la lista base crear otra que contenga los mismos elementos ordenador por dicotomia:
  - Cojo el elemento del medio y lo meto en una lista.
  - Avanzo cogiendo elementos hacia la izquierda de la lista.
  - Cuando acabe cogiendo las de la izquierda voy cogiendo las restantes que son las que quedaban a la derecha.
- Finalmente hay que reordenar la lista obtenida como la original.
"""
lista = ["1","2","3","4","5","6","7"]
listadicotomia = []
listadicotomia.append(lista.pop(len(lista)//2))
print(lista)
retroceso = 0
def dicotomia(longitud,retroceso):
  retroceso = retroceso + 1
  print(retroceso)
  print(listadicotomia)
  listadicotomia.append(lista[((longitud//2)-retroceso)-1])
if len(listadicotomia) < len(lista):
  dicotomia(len(lista),0)

dicotomia(len(lista),0)