# Ejercicio 1
# SALIDA - Bienvenida
print("=" * 45)
print("BIENVENIDO A GAME STORE")
print("=" * 45)
print("El paraiso de los gamers")

# ENTRADA - Datos del cliente
nombre = input("Ingresa tu nombre:")
edad = int(input("Ingresa tu edad:"))
# PROCESAMIENTO - Precios fijos de los juegos
precio_fifa = 899.00
precio_cod = 1299.00
precio_gow = 1399.00
precio_gta = 1119.00

# SALIDA - Catalogo de productos
print("------- CATALOGO DE PRODUCTOS -------")
print("1. FC 2025 - $"+ str(precio_fifa))
print("2. Call of Duty - $"+ str(precio_cod))
print("3. God of War: Ragnarok - $" + str(precio_gow))
print("4. Grand Theft Auto V - $" + str(precio_gta))

# ENTRADA - Cantidad de cada juego
cantidad_fifa = float(input("Cuantos FC 2025 quieres? "))
cantidad_cod = float(input("Cuantos Call of Duty quieres? "))
cantidad_gow = float(input("Cuantos God of War: Ragnarok quieres? "))
cantidad_gta = float(input("Cuantos Grand Theft Auto V quieres? "))

# PROCESAMIENTO - Calculos por juego
total_fifa = precio_fifa * cantidad_fifa
total_cod = precio_cod * cantidad_cod
total_gow = precio_gow * cantidad_gow
total_gta = precio_gta * cantidad_gta

# PROCESAMIENTO - Calculos totales
subtotal = total_fifa + total_cod + total_gow + total_gta
iva = subtotal * 0.16
total = subtotal + iva

# PROCESAMIENTO - Cantidad total de juegos
cantidad_total = cantidad_fifa + cantidad_cod + cantidad_gow + cantidad_gta

# PROCESAMIENTO - Crear ticket
print("TICKET DE COMPRA")
print("=" * 45)
print("Cliente: " + nombre)
print("Edad: " + str(edad) + "anios")
print("=" * 45)
print("DETALLE DE COMPRA")
print("FC 2025")
print(" Cantidad: " + str(cantidad_fifa))
print(" Precio unitario: $" + str(precio_fifa))
print(" Total: $" + str(precio_fifa))
print("Call of Duty")
print(" Cantidad: " + str(cantidad_cod))
print(" Precio unitario: $" + str(total_cod))
print(" Total: $" + str(total_cod))
print("God of War: Ragnarok")
print(" Cantidad: " + str(cantidad_gow))
print(" Precio unitario: $" + str(precio_gow))
print(" Total: $" + str(total_gow))
print("Grand Theft Auto V")
print(" Cantidad: " + str(cantidad_gta))
print(" Precio unitario: $" + str(precio_gta))
print(" Total: $" + str(total_gta))
print("=" * 45)
print("Cantidad total de juegos: " + str(cantidad_total))
print("Subtotal: $" + str(subtotal))
print("IVA (16%): $" + str(iva))
print("=" * 45)
print("TOTAL A PAGAR: $" + str(total))
print("GAME STORE")
# SALIDA - Mensaje de despedida
print("Gracias por tu compra, " + nombre + "!")

# Ejercicio 1. Control de acceso a videojuego
print("Ejercicio 1. Control de acceso a videojuego\n")

edad = input(" Cuantos anios tienes?: ")
print("Tienes",edad,"anios")

if edad >= 16:
    print("Puedes jugar :) \n")
else:
    print("Eres muy joven para este juego :( \n")

# Ejercicio 2. Calculadora de promedio escolar
print("Ejercicio 2. Calculadora de promedio escolar \n")
