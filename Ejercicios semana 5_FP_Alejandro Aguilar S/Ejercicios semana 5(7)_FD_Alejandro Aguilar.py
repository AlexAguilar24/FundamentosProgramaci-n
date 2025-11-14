# Ejemplo 1: Mostrar el menú de un restaurante
print("\nEjemplo 1 mostrar el menú\n")

def mostrar_menu():
    print("=== MENÚ ===")
    print("1. Hamburguesa")
    print("2. Pizza")
    print("3. Tacos")

# La usas así y ya no tienes que escribir todo el menu
mostrar_menu()

# Ejemplo 2: Reproducir tu canción favorita
print("\nEjemplo 2 la fav canción\n")

def reproducir_favorita():
    print("🎵 Reproduciendo: `Timeless` de The Weeknd ft. Playboi Carti")

# La usas así:
reproducir_favorita()

# Ejemplo 3: Mostrar las reglas de un juego
print("\nEjemplo 3 reglas del juego\n")

def mostrar_reglas():
    print("REGLAS DEL JUEGO:")
    print("- No hacer trampa")
    print("- Respetar turnos")
    print("- Divertirse")

# La usas así:
mostrar_reglas()

# Ejemplo 4: Reproducir cualquier canción (con parámetros)
#FUNCIONES  CON PAREMTROS
print("\nEjemplo 4\n")

def reproducir_canción(nombre_cancion):
    print(f" 🎵 Reproduciendo: {nombre_cancion}")

# La usas así (cada vez es DIFERENTE):
reproducir_canción("Bad Bunny - Titi Me Preguntó")
reproducir_canción("Travis Scott ft. Drake - Sicko Mode")
reproducir_canción("Maluma - Borro Cassete")

# Ejemplo 5: Calcular impuestos (con parámetros)
print("\nEjemplo 5\n")

def calcular_impuesto(precio):
    total = precio * 1.16  #16%
    return total

# La usas así (cada precio es DIFERENTE):
print(calcular_impuesto(110))
print(calcular_impuesto(500))
print(calcular_impuesto(1200))

# Ejercicio 1
print("\nEjercicio 1\n")

# Escribe tu función aquí
def mostrar_perfil():
    print("👤 Usuario: @taylorswift")
    print("👥 Seguidores: 1.2b")
    print("📄 Bio: Cantante")

# Pruébala (llámala 2 veces)
mostrar_perfil()
print()  # Línea en blanco para separar
mostrar_perfil()

# Ejercicio 2
print("\nEjercicio 2\n")

#Escribe tu función aqui
def calcular_horas_tiktok(minutos_por_dia):
    minutos_totales = minutos_por_dia * 7
    horas_totales = minutos_totales / 60
    return horas_totales

# Pruébala con diferentes valores
horas = calcular_horas_tiktok(30)  # 30 minutos por día
print(f"Ves {horas} horas de Tiktok a la semana ")

horas2 = calcular_horas_tiktok(60)  # 60 minutos por día
print(f"Ves {horas2} horas de Tiktok a la semana ")

# Ejercicio 3
print("\nEjercicio 3\n")

# Escribe tu función aqui
def puedo_comprar(dinero_que_tengo, precio_producto):
    if dinero_que_tengo >= precio_producto:
        return "✅ Si puedes comprarlo"
    else:
        return "❌ No te alcanza"

# Pruébala con diferentes casos
resultado1 = puedo_comprar(500, 300)  # Tengo $500, cuesta $300
print(f"Tenís nuevos: {resultado1}")

resultado2 = puedo_comprar(150, 800)  # Tengo $150, cuesta $800
print(f"Celular nuevo: {resultado2}")

resultado3 = puedo_comprar(100, 100)  # Tengo $100, cuesta $100
print(f"Audífonos: {resultado3}")

# Ejercicio 4: Likes de Instagram
print("\nEjercicio 4\n")

def calcular_likes_totales(likes_foto1, likes_foto2, likes_foto3):
    total = likes_foto1 + likes_foto2 + likes_foto3
    return total

total = calcular_likes_totales(150, 230, 89)
print(f"Tienes {total} likes en total ❤")

total2 = calcular_likes_totales(800, 420, 300)
print(f"Tienes {total2} likes en total ❤")

# Ejercicio 5
print("\nEjercicio 5\n")

def aplicar_descuento(precio_original, porcentaje_descuento):
    descuento = precio_original * porcentaje_descuento / 100
    precio_final = precio_original - descuento
    return precio_final

precio_final = aplicar_descuento(1000, 20) # $1000 con 20% de descuento
print(f"Precio final: ${precio_final} 💰")

precio_final2 = aplicar_descuento(500, 10) # $500 con 10% de descuento
print(f"Precio final: ${precio_final2} 💰")

# Ejercicio 6: Promedio de calificaciones
print("\nEjercicio 6\n")

def calcular_promedio(cal1, cal2, cal3):
    suma = cal1 + cal2 + cal3
    promedio = suma / 3
    return promedio

promedio = calcular_promedio(85, 90, 78)
print(f"Tu promedio es: {promedio}")

promedio2 = calcular_promedio(100, 95, 88)
print(f"Tu promedio es: {promedio2}")

