# Ejercicio 5: Orden desdendente
print("\nEjercicio 5: Orden descendente (mayor a menor)\n")
numeros_ej5 = [52, 24 , 88, 17, 16]
print("Original:\n", numeros_ej5)
n = len(numeros_ej5)

for i in range(n):
    for j in range(0, n - i - 1):
        # CAMBIO: < en lugar de >
        if numeros_ej5[j] < numeros_ej5[j + 1]:
            numeros_ej5[j], numeros_ej5[j + 1] = numeros_ej5[j + 1], numeros_ej5[j]

print("Ordenado (mayor a menor):\n", numeros_ej5)

# Ejercicio 6: Desafío
print("\nEjercicio 6: Desafío\n")

numeros_ej6 = [13, 6, 10, 3, 16]
print("Original:\n", numeros_ej6)
n = len(numeros_ej6)

for k in range(n):
    for l in range(0, n - k - 1):
        if numeros_ej6[l] > numeros_ej6[l + 1]:  # ¿Qué va aquí?
            numeros_ej6[l], numeros_ej6[l + 1] = numeros_ej6[l + 1], numeros_ej6[l] # Completa

print("Ordenado:\n", numeros_ej6)
