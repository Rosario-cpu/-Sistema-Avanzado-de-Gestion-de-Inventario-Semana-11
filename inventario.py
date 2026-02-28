# --- CLASE INVENTARIO (Lógica de Negocio) ---
# Este archivo cumple con el Requisito 2 y 3: Uso de Colecciones.
# Se utiliza un DICCIONARIO para almacenar los productos porque permite
# una búsqueda rápida por ID, optimizando el manejo de los datos.

import os
from producto import Producto

class Inventario:
    def __init__(self):
        # El diccionario almacena objetos Producto usando su ID como clave.
        self.productos = {}

        # Requisito 4: Nombre del archivo para persistencia de datos.
        self.archivo = "inventario_datos.txt"
        self.cargar_desde_archivo()

    def añadir(self, producto):
        """Añade un producto al diccionario y actualiza el archivo."""
        if producto.get_id() in self.productos:
            print("Error: El ID ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            self.guardar_en_archivo()
            print("Producto añadido correctamente.")

    def eliminar(self, id_producto):
        """Elimina por ID y actualiza el archivo."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado.")
        else:
            print("Error: ID no encontrado.")

    def actualizar(self, id_producto, cantidad=None, precio=None):
        """Modifica cantidad o precio y guarda cambios."""
        if id_producto in self.productos:
            if cantidad is not None: self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None: self.productos[id_producto].set_precio(precio)
            self.guardar_en_archivo()
            print("Producto actualizado.")
        else:
            print("Error: No se encontró el producto.")

    def buscar_por_nombre(self, nombre):
        """Busca coincidencias en el nombre dentro de la colección."""
        return [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]

    # --- PERSISTENCIA EN ARCHIVOS (Requisito 4) ---
    def guardar_en_archivo(self):
        """Escribe la colección en el archivo de texto (Serialización)."""
        with open(self.archivo, "w") as f:
            for p in self.productos.values():
                f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")

    def cargar_desde_archivo(self):
        """Lee el archivo al iniciar el programa (Deserialización)."""
        if os.path.exists(self.archivo):
            with open(self.archivo, "r") as f:
                for linea in f:
                    datos = linea.strip().split(',')
                    if len(datos) == 4:
                        self.productos[datos[0]] = Producto(datos[0], datos[1], int(datos[2]), float(datos[3]))