# --- CLASE PRODUCTO ---
# Este archivo define la estructura de los objetos que guardaremos en el inventario.
# Cumple con el requisito de atributos: ID, nombre, cantidad y precio.

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        """
        Constructor que inicializa los atributos del producto.
        Se usan prefijos de guion bajo para respetar el encapsulamiento.
        """
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Métodos para obtener y establecer atributos
    def get_id(self): return self._id
    def get_nombre(self): return self._nombre
    def get_cantidad(self): return self._cantidad
    def get_precio(self): return self._precio

    # Métodos Setter para actualizar atributos específicos
    def set_cantidad(self, cantidad): self._cantidad = cantidad
    def set_precio(self, precio): self._precio = precio

    def __str__(self):
        """Devuelve una representación en texto del objeto para mostrar al usuario."""

        return f"ID: {self._id} | Producto: {self._nombre} | Stock: {self._cantidad} | Precio: ${self._precio}"
