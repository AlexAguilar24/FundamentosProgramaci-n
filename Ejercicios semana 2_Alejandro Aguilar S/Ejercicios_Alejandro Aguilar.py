#Ejercicio 1 con print.py>

print("Ejercicio 1\n")

# Instrucción 1
nombre = "Alex"

# Instrución 2
edad = 18

# Instrucción 3
print("Hola,soy",nombre)

# Instrucción 4
print("Tengo",edad,"años")


#Ejercicio 2 con print
#2. Nueva Línea (\n)
print("\nEjercicio 2\n")

# Sin \n (todo en una línea)
print("Hola Mundo")
# Salida: Hola Mundo

# Con \n (salto de línea)
print("Hola\nMundo")

# Múltiples \n
print("Línea 1\nLínea 2\nLínea 3")



#Ejercicio 3 con tabulación
print("\nEjercicio 3\n")

print ("Nombre:\tAlejandro")
print("Edad:\t18")
print("Ciudad:\tSaltillo")

#Ejercicio 4 con tabulación
print("\nEjercicio 4\n")

# Crear una conversación de chat
print("Meli:\tHola, ¿cómo estás?")
print("Alex:\tBien, ¿y tú?")
print("Meli:\t¡Genial!\n")
print("===== Chat guardado en =====")
print("C:\\Usuarios\\asagu\\Documents\\chat.txt")


# Ejercicio 5
print("\nEjercicio 5\n")

# Dos argumentos
print("Hola","Mundo")
# Salida: Hola Mundo
#             ↑
#           espacio automático

# Tres argumentos
print("Me","gusta","mucho","hacer ejercicio")

# Mezclando tipos de datos
print("Tengo",2,"mascotas en mi casa",",un perro y una tortuga")

# Con variables
nombre = "Alex"
cantidad_hermanos = 2
print("Me dicen", nombre,"y tengo",cantidad_hermanos,"hermanos",", Majo y León")


#Ejercicio 6. OPERADORES ARITMÉTICOS
print("\nEjercicio 6. OPERADORES ARITMÉTICOS\n")
# SUMA (+): vamos a sumar dos números
numero1 = 67
numero2 = 41
suma = numero1 + numero2
print("Operador suma:", suma)

# RESTA (-): ahora vamos a restar 
resta = numero1 - numero2
print("Operador resta:", resta)

# MULTIPLICACIÓN (*): multiplícamos dos números
multiplicacion = numero1 * numero2
print("Operador multiplicación:", multiplicacion)

# DIVISIÓN (/): dividimos y obtenemos resultado con decimales
division = numero1 / numero2
print("Operador división:", division)

# DIVISIÓN ENTERA (//): dividimos pero solo queremos la parte entera
division_entera = 10 // 3
print("Operador división entera:", division_entera)

# (%): obtiene el residuo (lo que sobra) de una división
residuo = 10 % 3
print("Operador residuo:", residuo)

# POTENCIA (**): elevar un número a una potencia
potencia = 2 ** 3
print("Operador potencia:", potencia)


#Ejercicio 7. Operadores de comparación
print("\nEjercicio 7. Operadores de comparación\n")

print("¿He aprobado o no la materia")
# MAYOR O IGUAL (>=): La calificación mínima para pasar es 70
calificacion = 70
resultado5 = calificacion >= 70
print("¿Aprobé:", resultado5)

# MAYOR (>): La calificación mínima para pasar es 70
resultado6 = calificacion > 70
print("¿Aprobé?:", resultado6)

# Vamos a comparar estos dos números
mi_edad = 18
edad_minima = 18

# IGUAL A (==): Pregunta: ¿Los números son iguales?
resultado1 = mi_edad == 15
print("\n¿Soy mayor de edad? (==):", resultado1)

# DIFERENTE DE (!=): Pregunta: ¿Los números son diferentes?
resultado2 = mi_edad != 20
print("¿Tengo 18 años? (!=):", resultado2)

# MENOR QUE (<): Pregunta: ¿El primer número es menor?
resultado3 = mi_edad < 18
print("¿Mi edad es menor que 18? (<):", resultado3)

# MENOR O IGUAL (<=): Pregunta: ¿Es menor o igual?
resultado4 = mi_edad <= 10
print("¿Mi edad es menor o igual a 10? (<=):", resultado4)


#Ejercicio 8. Operadores lógicos
print("\nEjercicio 8. Operadores lógicos\n")
# Imaginemos que queremos entrar a un juego online
tengo_internet = True  # Sí tengo internet
tengo_cuenta = True    # Sí tengo cuenta

# AND (y): Las DOS condiciones deben ser verdaderas
puedo_jugar = tengo_internet and tengo_cuenta
print("¿Puedo jugar? (ambas True):", puedo_jugar)

# Probemos cuando falta algo
tengo_internet2 = True
tengo_cuenta2 = False
puedo_jugar2 = tengo_internet2 and tengo_cuenta2
print("¿Puedo jugar? (una es False):", puedo_jugar2)

# OR (o): Al menos UNA condición debe ser verdadera
tengo_celular = True
tengo_tablet = False
tengo_dispositivo = tengo_celular or tengo_tablet
print("¿Tengo dispositivo? (al menos una True):", tengo_dispositivo)

# NOT (no): Invierte el valor: True se vuelve False y viceversa
esta_lloviendo = False
puedo_salir = not esta_lloviendo
print("¿Puedo salir? (NOT False = True):", puedo_salir)


#Ejercicio 9. Operadores de asignación
print("\nEjercicio 9. Operadores de asignación")

# ASIGNACIÓN SIMPLE (=): Guardamos un valor en una variable
puntos = 0
print("Puntos iniciales:", puntos)

# SUMA Y ASIGNA (+=): Es lo mismo que escribir: puntos = puntos + 20
puntos += 20
print("Ganaste 20 puntos (+=):", puntos)

# RESTA Y ASIGNA (-=): Es lo mismo que escribir: puntos = puntos - 10
puntos -= 10
print("Perdiste 10 puntos (-=):", puntos)

# MULTIPLICA Y ASIGNA (*=): Es lo mismo que escribir: puntos = puntos * 2
puntos *= 2
print("¡Puntos x2! (*=):", puntos)

# DIVIDE Y ASIGNA (/=): Es lo mismo que escribir: puntos = puntos / 4
puntos /= 4
print("Dividir puntos (/=):", puntos)


#Ejercicio 10. Operadores de identidad
print("\nEjercicio 10. Operadores de identidad\n")

# Programa que compara objetos
print("=== ¿SON LA MISMA COSA? ===")
# Creamos dos listas que se ven iguales
lista1 = ["manzana","pera"]
lista2 = ["manzana","pera"]
lista3 = lista1  # lista3 es la MISMA que lista1

# IS (es): Pregunta ¿Son el mismo objeto en la memoria?
print("¿lista1 es lista2? (is):", lista1 is lista2)  # False (diferentes objetos)
print("¿lista1 es lista3? (is):", lista1 is lista3)  # True (mismo objeto)

# IS NOT (no es): Pregunta ¿NO son el mismo objeto?
print("¿lista1 No es lista2? (is not):", lista1 is not lista2)  # True

