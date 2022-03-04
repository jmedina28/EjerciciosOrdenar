variable = int(input("Seleccione que ejercicio desea ejecutar(1-3): "))
if variable == 1:
    from ejercicios import ejercicio1
elif variable == 2:
    from ejercicios import ejercicio2
elif variable == 3:
    from ejercicios import ejercicio3
else:
    print("Introduzca valores entre 1 y 3.")