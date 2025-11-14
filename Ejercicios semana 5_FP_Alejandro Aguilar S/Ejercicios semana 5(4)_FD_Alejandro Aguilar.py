# Ejercicio 1: Tu primera lista ordenada
print("Ejercicio 1: Ordenar una lista pequeña\n")

numeros_lista = [6, 3, 2, 10, 13, 5]
print("Lista original:", numeros_lista)

# Ordenar con Bubble Sort
n = len(numeros_lista)  # n = 7 elementos en numeros_lista

for i in range(n):
    for j in range(0, n - i - 1):
        # Comparar vecinos
        if numeros_lista[j] > numeros_lista[j + 1]:
            # Intercambiar
            numeros_lista[j], numeros_lista[j + 1] = numeros_lista[j + 1], numeros_lista[j]
print("Lista ordenada:", numeros_lista)

# Ejercicio 2: Cambia los números
print("\nEjercicio 2: Cambia los numeros\n")

numeros_ej2 = [11, 34, 67, 17, 8, 24] # <-CAMBIA ESTOS NÚMEROS POR LOS TUYOS
print("Lista original:", numeros_ej2)

n = len(numeros_ej2)

for k in range(n):
    for l in range(0, n - i - 1):
        if numeros_ej2[l] > numeros_ej2[l + 1]:
            numeros_ej2[l], numeros_ej2[l + 1] = numeros_ej2[l + 1], numeros_ej2[l]
print("Lista ordenada:", numeros_ej2) 
