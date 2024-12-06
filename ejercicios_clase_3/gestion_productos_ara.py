# Sistema de Gestión de Productos - TIENDAS ARA: By Samuelito+IA

# Inventario inicial vacío
inventario = {}

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE PRODUCTOS - TIENDAS ARA ---")
    print("1. Agregar un nuevo producto")
    print("2. Eliminar un producto")
    print("3. Actualizar cantidad y precio de un producto")
    print("4. Mostrar inventario")
    print("5. Mostrar productos por agotarse (menos de 5 unidades)")
    print("6. Salir")
    return input("Seleccione una opción: ")

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ").strip().lower()
    if nombre in inventario:
        print("El producto ya existe.")
    else:
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
        print(f"Producto '{nombre}' agregado exitosamente.")

def eliminar_producto():
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip().lower()
    if nombre in inventario:
        del inventario[nombre]
        print(f"Producto '{nombre}' eliminado exitosamente.")
    else:
        print("El producto no existe.")

def actualizar_producto():
    nombre = input("Ingrese el nombre del producto a actualizar: ").strip().lower()
    if nombre in inventario:
        cantidad = int(input("Ingrese la nueva cantidad: "))
        precio = float(input("Ingrese el nuevo precio: "))
        inventario[nombre] = {"cantidad": cantidad, "precio": precio}
        print(f"Producto '{nombre}' actualizado exitosamente.")
    else:
        print("El producto no existe.")

def mostrar_inventario():
    if inventario:
        print("\n--- INVENTARIO ---")
        for nombre, datos in inventario.items():
            print(f"Producto: {nombre.capitalize()}, Cantidad: {datos['cantidad']}, Precio: ${datos['precio']:.2f}")
    else:
        print("El inventario está vacío.")

def mostrar_por_agotarse():
    print("\n--- PRODUCTOS POR AGOTARSE (menos de 5 unidades) ---")
    por_agotarse = [nombre for nombre, datos in inventario.items() if datos['cantidad'] < 5]
    if por_agotarse:
        for nombre in por_agotarse:
            print(f"Producto: {nombre.capitalize()}, Cantidad: {inventario[nombre]['cantidad']}")
    else:
        print("No hay productos por agotarse.")

# Programa principal
while True:
    opcion = mostrar_menu()
    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        eliminar_producto()
    elif opcion == "3":
        actualizar_producto()
    elif opcion == "4":
        mostrar_inventario()
    elif opcion == "5":
        mostrar_por_agotarse()
    elif opcion == "6":
        print("Saliendo del sistema. ¡Gracias por usar TIENDAS ARA!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")