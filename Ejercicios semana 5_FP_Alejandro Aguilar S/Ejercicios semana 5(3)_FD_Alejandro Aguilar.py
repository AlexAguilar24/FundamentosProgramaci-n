# Ejercicio 4: Encuentra un elemento mayor
print("Ejercicio 4\n")
matriz = [
    [24, 10],
    [8, 29]
]
#Empezamos asumiendo que el primero es el mayor
mayor = matriz[0][0]  # Empieza con 15
#Recorremos toda la matriz
for fila in matriz:
    for elemento in fila:
        if elemento > mayor:  # Sí encuentro uno más grande
            mayor = elemento  # Lo guardo como el numero mayor

#Mostramos resultado
print("La matriz es:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()
print(f"\nEl número mayor es: {mayor}")

