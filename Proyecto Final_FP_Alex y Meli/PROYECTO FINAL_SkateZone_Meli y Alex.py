#Librerias
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog # Día 2 agregamos simpledialog
from datetime import datetime

# Inventario Inicial incluye 10 productos
inventario = [
    {"id": "001", "modelo": "Skate - Screaming Hand", "marca": "Santa Cruz", "precio": 2200.00, "talla": "8.0", "stock": 4, "descripcion": "Skate completo de arce, completamente equipado"},
    {"id": "002", "modelo": "Tabla - Logo Red", "marca": "Baker", "precio": 1200.00, "talla": "8.0, 8.25, 8.5", "stock": 6, "descripcion": "Tabla clásica, perfecta para street"},
    {"id": "003", "modelo": "Tabla - Sean Malto Pro Model", "marca": "Girl", "precio": 1250.00, "talla": "8.0, 8.125, 8.5", "stock": 6, "descripcion": "Tabla ligera, ideal para trucos técnicos"},
    {"id": "004", "modelo": "Trucks - Stage 11 Standard", "marca": "Independent Truck Co.", "precio": 1050.00, "talla": "139, 144, 149", "stock": 8, "descripcion": "Trucks duraderos y de gran estabilidad"},
    {"id": "005", "modelo": "Trucks - Hollow Lights", "marca": "Thunder", "precio": 1150.00, "talla": "145, 147, 148", "stock": 7, "descripcion": "Estructura hueca que reduce el peso, ideales para street y trucos de impacto"},
    {"id": "006", "modelo": "Ruedas - Formula Four 99a Classic", "marca": "Spitfire", "precio": 720.00, "talla": "50 mm, 52mm, 54mm", "stock": 10, "descripcion": "Compuesto anti-flatspot, con excelente agarre y control"},
    {"id": "007", "modelo": "Ruedas - Super Juice 78a", "marca": "OJ Wheels", "precio": 850.00, "talla": "60mm", "stock": 4, "descripcion": "Ruedas suaves para cruising o terrenos irregulares"},
    {"id": "008", "modelo": "Rodamientos - Swiss Bearings", "marca": "Bones", "precio": 1200.00, "stock": 12, "descripcion": "Rodamientos premium reconocidos por su alta velocidad y calidad"},
    {"id": "009", "modelo": "Lija - Stamp Logo", "marca": "Grizzly Griptape", "precio": 220.00, "talla": "9'x 33", "stock": 6, "descripcion": "Lija con mayor durabilidad y diseño impreso"},
    {"id": "010", "modelo": "Tenis - Skate Old Skool", "marca": "Vans", "precio":1400.00, "talla": "24 - 30 MX", "stock": 6, "descripcion": "Suela Waffle mejorada y refuerzos Duracap"},  
]

historial_ventas = []
STOCK_MINIMO = 3

#Funciones
def mostrar_bienvenida():
    """Muestra la pantalla de bienvenida con estadísticas rápidas"""
    global boton_activo 
    texto.delete(1.0, tk.END)
    activar_boton(btn_home)

    total_modelos = len(inventario)
    total_articulos = sum(t['stock'] for t in inventario)
    ventas_hoy = sum(1 for v in historial_ventas if datetime.strptime(v['fecha'], "%d/%m/%Y %H:%M").date() == datetime.now().date())
    productos_stock_bajo = sum(1 for t in inventario if t['stock'] > 0 and t['stock'] <= STOCK_MINIMO)

    texto.insert(tk.END, "==O       ==O_/    ==O_/ \n  /|\/       /\      \/\ _                 / \n  / |\       / |\        | \       \   / / /o \n  _/__|_     _/__|_     _/____    ==O__\/ /o \n  o  o       o  o       o  o      \/ \n\n")
    texto.insert(tk.END, "-----------------------------------------------------\n\n")
    texto.insert(tk.END, "  🛹 BIENVENIDO@ A SKATE ZONE STORE 🛹\n\n")
    texto.insert(tk.END, "-----------------------------------------------------\n\n")

    texto.insert(tk.END, "RESUMEN RÁPIDO:\n\n", "titulo")
    texto.insert(tk.END, f"Modelos Únicos: {total_modelos}\n")
    texto.insert(tk.END, f"Total de Articulos en Stock: {total_articulos}\n")
    texto.insert(tk.END, f"Ventas Registradas (Hoy): {ventas_hoy}\n")

    if productos_stock_bajo > 0:
        texto.insert(tk.END, f"¡ALERTA DE STOCK BAJO!: {productos_stock_bajo} productos necesitan reabastecimiento.\n", "alerta")
    else:
        texto.insert(tk.END, "¡Inventario en buen estado!\n")
    
    texto.insert(tk.END, "\nSelecciona una opción del menú para comenzar...\n")

# Día 2
def validar_numero_positivo(valor, nombre_campo):
    """Valida que el valor sea un número positivo."""
    try:
        num = float(valor)
        if num < 0:
            messagebox.showerror("Error de Validación", f"El campo '{nombre_campo}' no puede ser negativo")
            return None
        return num
    except ValueError:
        messagebox.showerror("Error de Validación", f"El campo '{nombre_campo}' debe ser un número válido.")
        return None

# Día 2
def generar_nuevo_id():
    """Genera un nuevo ID consecutivo basado en el ID numérico más alto actual."""
    if not inventario:
        return "001"
    
    max_id = 0
    for articulo in inventario:
        try:
            num_id = int(articulo['id'])
            if num_id > max_id:
                max_id = num_id
        except ValueError:
            continue
    
    return str(max_id + 1).zfill(3)

# Día 2
def mostrar_inventario():
    """Muestra el listado completo del inventario."""
    texto.delete(1.0, tk.END)
    texto.insert(tk.END, "= INVENTARIO COMPLETO =\n\n")
    activar_boton(btn1)

    if not inventario:
        texto.insert(tk.END, "X No hay articulos en el inventario\n")
    else:
        texto.insert(tk.END, f"{'ID':<4} | {'MODELO':<25} | {'PRECIO':<10} | {'TALLA':<6} | {'MARCA':<10} | {'STOCK':<5}\n")
        texto.insert(tk.END, "-"*70 + "\n")

        for articulo in inventario:
            linea = f"{articulo['id']:<4} | {articulo['modelo']:<25} | ${articulo['precio']:<9,.0f} | {articulo['talla']:<6} | {articulo['marca']:<10} | {articulo['stock']:<5}"
            texto.insert(tk.END, linea)

            if articulo['stock'] > 0 and articulo['stock'] <= STOCK_MINIMO:
                texto.insert(tk.END, "STOCK BAJO", "alerta")
            elif articulo['stock'] == 0:
                texto.insert(tk.END, "AGOTADO", "agotado")
            
            texto.insert(tk.END, "\n")
        
        texto.insert(tk.END, "\nUsa el botón 'AGREGAR' para incorporar nuevos productos\n")

# Día 2
def agregar_articulo():
    """Agrega un nuevo articulo al inventario."""
    activar_boton(btn2)
    new_id = generar_nuevo_id()

    modelo = simpledialog.askstring("Agregar Articulo", "1. Nombre del modelo (Obligatorio):", parent=ventana)
    if not modelo: return

    marca = simpledialog.askstring("Agregar Articulo", "2. Marca (Obligatorio):", parent=ventana)
    if not marca: return

    precio_str = simpledialog.askstring("Agregar Articulo", "3. Precio unitario (Obligatorio):", parent=ventana)
    if not precio_str: return
    precio_validado = validar_numero_positivo(precio_str, "precio")
    if precio_validado is None: return

    talla = simpledialog.askstring("Agregar Articulo", "4. Talla/Medida (Obligatorio):", parent=ventana)
    if not talla: return

    stock_str = simpledialog.askstring("Agregar Articulo", "5. Cantidad inicial (Stock) (Obligatorio):", parent=ventana)
    if not stock_str: return
    stock_validado = validar_numero_positivo(stock_str, "Cantidad inicial")
    if stock_validado is None: return

    descripcion = simpledialog.askstring("Agregar Articulo", "6. Descripción adicional (Opcional):", parent=ventana)

    nuevo_articulo = {
        "id": new_id,
        "modelo": modelo,
        "marca": marca,
        "precio": float(precio_validado),
        "talla": talla
    }

# Día 3
def buscar_articulos():
    """Buscar un producto en el inventario por ID, Modelo, Marca o Talla."""
    activar_boton(btn4)

    if not inventario:
        messagebox.showwarning("Sin inventario", "No hay articulos disponibles para buscar", parent=ventana)
        return
    
    criterio_busqueda = simpledialog.askstring("Buscar Articulos",
                                                "Busca por: ID, Modelo, Marca o Talla:",
                                                 parent=ventana)
    
    if not criterio_busqueda:
        return
    
    criterio = criterio_busqueda.lower()
    resultados = []

    for articulo in inventario:
        if (criterio in articulo['id'].lower() or
            criterio in articulo['modelo'].lower() or
            criterio in articulo['marca'].lower() or
            criterio in articulo['talla'].lower()):
            resultados.append(articulo)
    
    texto.delete(1.0, tk.END)
    texto.insert(tk.END, f"RESULTADOS DE BÚSQUEDA: '{criterio_busqueda}' ===\n\n")

    if not resultados:
        texto.insert(tk.END, "X No se encontraron resultados\n")
    else:
        texto.insert(tk.END, f"Se encontraron {len(resultados)} articulo(s):\n\n")
        texto.insert(tk.END, f"{'ID':<4} | {'MODELO':<25} | {'PRECIO':<10} | {'TALLA':<6} | {'MARCA':<10} | {'STOCK':<5}\n")
        texto.insert(tk.END, "-"*70 + "\n")

        for articulo in resultados:
            linea = f"{articulo['id']:<4} | {articulo['modelo']:<25} | ${articulo['precio']:<9,.0f} | {articulo['talla']:<6} | {articulo['marca']:<10} | {articulo['stock']:<5}"
            texto.insert(tk.END, linea)

            if articulo['stock'] > 0 and articulo['stock'] <= STOCK_MINIMO:
                texto.insert(tk.END, "STOCK BAJO", "alerta")
            elif articulo['stock'] == 0:
                texto.insert(tk.END, "AGOTADO", "agotado")
            
            texto.insert(tk.END, "\n")

# Día 3
def vender_articulo():
    """Registra una venta de productos y actualiza el inventario."""
    activar_boton(btn3)

    if not inventario:
        messagebox.showwarning("Sin inventario", "No hay productos disponibles para vender", parent=ventana)
        return
    
    opciones = "\n".join([f"{i+1}. ID:{t['id']} - {t['modelo']} ({t['marca']}) - Stock: {t['stock']}" for i, t in enumerate(inventario)])
    seleccion = simpledialog.askinteger("🤑 Vender Articulo 🤑", f"Selecciona el NÚMERO del producto a vender:\n\n{opciones}", parent=ventana)

    if not seleccion or seleccion < 1 or seleccion > len(inventario):
        if seleccion is not None: messagebox.showerror("Error", "Selección inválida o cancelada.")
        return
    
    articulo_a_vender = inventario[seleccion - 1]

    if articulo_a_vender['stock'] <= 0:
        messagebox.showwarning("Sin stock", "Este modelo está agotado.", parent=ventana)
        return
    
    cantidad_str = simpledialog.askstring("Vender Articulo", f"¿Cuántas unidades de '{articulo_a_vender['modelo']}' quieres vender?", parent=ventana)
    if not cantidad_str: return

    cantidad_validada = validar_numero_positivo(cantidad_str, "Cantidad a vender")
    if cantidad_validada is None: return
    cantidad = int(cantidad_validada)

    if cantidad > articulo_a_vender['stock']:
        messagebox.showerror("Error de Venta", f"Solo hay {articulo_a_vender['stock']} unidades disponibles. No se puede vender {cantidad}.", parent=ventana)
        return
    
    monto_total = cantidad * articulo_a_vender['precio']

    articulo_a_vender['stock'] -= cantidad

    registro_venta = {
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M"),
        "id_articulo": articulo_a_vender['id'],
        "modelo": articulo_a_vender['modelo'],
        "cantidad":cantidad,
        "precio_unitario": articulo_a_vender['precio'],
        "total": monto_total
    }

    historial_ventas.append(registro_venta)

    messagebox.showinfo("Venta Registrada",
                        f"Se vendieron {cantidad} unidades de '{articulo_a_vender['modelo']}'\n"
                        f"Monto Total: ${monto_total:,.2f}")
    
    mostrar_resumen_venta(registro_venta)

# Día 3
def mostrar_resumen_venta(venta):
    """Muestra el resumen detallado de la venta realizada."""
    texto.delete(1.0, tk.END)
    texto.insert(tk.END, "=VENTA REGISTRADA =\n\n")

    texto.insert(tk.END, "DETALLES DE LA VENTA:\n", "titulo")
    texto.insert(tk.END, f"Fecha y Hora: {venta['fecha']}\n")
    texto.insert(tk.END, f"Articulo ID: {venta['id_articulo']}\n")
    texto.insert(tk.END, f"Nombre: {venta['modelo']}\n")
    texto.insert(tk.END, f"Cantidad: {venta['cantidad']} unidades\n")
    texto.insert(tk.END, f"Precio Unitario: ${venta['precio_unitario']:,.2f}\n")
    texto.insert(tk.END, f"TOTAL: ${venta['total']:,.2f}\n", "total")

    texto.insert(tk.END, "\n¡La venta ha sido registrada exitosamente!\n")

#Botones
def activar_boton(boton):
    """Actualiza el color del botón activo"""
    global boton_activo

    for btn in [btn_home, btn1, btn2, btn3, btn4]:
        btn.config(bg="#000000")
    
    if boton:
        boton.config(bg="#3a0774")
        boton_activo = boton

def on_enter(e, boton):
    if boton != boton_activo:
        boton.config(bg="#3a0774")

def on_leave(e, boton):
    if boton != boton_activo:
        boton.config(bg="#000000")

#Parte grafica
ventana = tk.Tk()
ventana.title("🛹──💨 SKATE ZONE STORE 🛹──💨")
ventana.geometry("1200x800")
ventana.configure(bg="#f5f5f5")

boton_activo = None

titulo = tk.Label(ventana, text="🛹──💨 SKATE ZONE STORE 🛹──💨",
                  font=("Helvetica", 32, "bold"), bg="#f5f5f5", fg="#000000")
titulo.pack(pady=20)

subtitulo = tk.Label(ventana, text="SISTEMA DE GESTIÓN DE INVENTARIO Y VENTAS",
                     font=("Helvetica", 12), bg="#f5f5f5", fg="#3a0774")
subtitulo.pack()

frame_botones = tk.Frame(ventana, bg="#f5f5f5")
frame_botones.pack(pady=20)

btn_style = {"font": ("Albert Sans", 11, "bold"), "bg": "#000000", "fg": "white",
             "width": 12, "height": 2, "cursor": "hand2", "relief": tk.FLAT, "bd": 0}

# Día 2
btn_home = tk.Button(frame_botones, text="HOME", command=mostrar_bienvenida, **btn_style)
btn_home.grid(row=0, column=0, padx=8)

btn1 = tk.Button(frame_botones, text="INVENTARIO", command=mostrar_inventario, **btn_style)
btn1.grid(row=0, column=1, padx=8)

btn2 = tk.Button(frame_botones, text="AGREGAR", command=agregar_articulo, **btn_style)
btn2.grid(row=0, column=2, padx=8)

# Día 3
btn3 = tk.Button(frame_botones, text="VENDER", command=vender_articulo, **btn_style)
btn3.grid(row=0, column=3, padx=8)

btn4 = tk.Button(frame_botones, text="BUSCAR", command=buscar_articulos, **btn_style)
btn4.grid(row=0, column=4, padx=8)

for btn in [btn_home, btn1, btn2, btn3, btn4]:
    btn.bind("<Enter>", lambda e, b=btn: on_enter(e, b))
    btn.bind("<Leave>", lambda e, b=btn: on_leave(e, b))

texto = scrolledtext.ScrolledText(ventana,
                                     font=("Opens Sans", 11),
                                     bg="#ffffff", fg="#000000",
                                     height=18,
                                     padx=20, pady=20,
                                     relief=tk.SOLID, bd=1)
texto.pack(padx=30, pady=15, fill=tk.BOTH, expand=True)

texto.tag_config("titulo", font=("Open Sans", 11, "bold"), foreground="#000000")
texto.tag_config("alerta", background="#ffe5e5", foreground="#ff4500", font=("Open Sans", 11, "bold"))
texto.tag_config("agotado", background="#fddede", foreground="#cc0000", font=("Open Sans", 11, "bold"))
texto.tag_config("total", font=("Open Sans", 12, "bold"), foreground="#008000")

footer = tk.Label(ventana, text="© 2025 SKATE ZONE STORE 🛹 | DÍA 1 - 2 - 3 - COMPLETO ",
                  font=("Helvetica", 10), bg="#f5f5f5", fg="#999999")
footer.pack(pady=10)

mostrar_bienvenida()
ventana.mainloop()

