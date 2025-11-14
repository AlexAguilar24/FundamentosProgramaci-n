# Ejercicio 3: Ordenar calificaciones
print("\nEjercicio 3: Calificaciones de la clase\n")

calificaciones = [89, 94, 79, 100, 83, 71]
print("Calificaciones desordenadas:\n", calificaciones)

n = len(calificaciones)

for i in range(n):
    for j in range(0, n - i - 1):
        if calificaciones[j] > calificaciones[j + 1]:
            calificaciones[j], calificaciones[j + 1] = calificaciones[j + 1], calificaciones[j]

print("Calificaciones oridenadas:\n", calificaciones)
print("Calificación más baja:\n", calificaciones[0])
print("Calificación más alta:\n", calificaciones[-1])

# Ejercicio 4: Ordenamiento paso a paso
print("\nEjercicio 4: Ver cada paso del ordenamiento\n")
numeros_ej4 = [24, 17, 33, 77, 81]
print("Inicio:", numeros_ej4)
print("-" * 30)
n = len(numeros_ej4)

for k in range(n):
    print(f"\nPasada {k + 1}:")
    for l in range(0, n - k - 1):
        print(f" Comparando {numeros_ej4[l]} y {numeros_ej4[l + 1]}")
        if numeros_ej4[l] > numeros_ej4[l + 1]:
            # Intercambiar
            numeros_ej4[l], numeros_ej4[l + 1] = numeros_ej4[l + 1], numeros_ej4[l]
            print(f" ✅ Intercambio → {numeros_ej4}")
        else:
            print(f" ❌ No cambiar → {numeros_ej4}")

print("\n" + "-" * 30)
print("Final:\n", numeros_ej4)
