# --- INTERFAZ DE USUARIO ---
# Este archivo implementa el Requisito 5: Menú interactivo en consola.
from producto import Producto
from inventario import Inventario


def mostrar_menu():
    sistema = Inventario()

    # Bucle principal para mantener el programa en ejecución
    while True:
        # Menú visual solicitado en la tarea (Semana 11)
        print("\n" + "=" * 40)
        print("  SISTEMA DE GESTIÓN DE INVENTARIO (S11)")
        print("=" * 40)
        print("1. Agregar Producto")
        print("2. Eliminar Producto por ID")
        print("3. Actualizar Cantidad/Precio")
        print("4. Buscar Producto por Nombre")
        print("5. Mostrar Todo el Inventario")
        print("6. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            id_p = input("ID único: ")
            nom = input("Nombre: ")
            can = int(input("Cantidad: "))
            pre = float(input("Precio: "))
            sistema.añadir(Producto(id_p, nom, can, pre))

        elif opcion == "2":
            id_p = input("Ingrese el ID a eliminar: ")
            sistema.eliminar(id_p)

        elif opcion == "3":
            id_p = input("ID del producto: ")
            c = input("Nueva cantidad (vacío para no cambiar): ")
            p = input("Nuevo precio (vacío para no cambiar): ")
            sistema.actualizar(id_p, int(c) if c else None, float(p) if p else None)

        elif opcion == "4":
            nom = input("Nombre a buscar: ")
            resultados = sistema.buscar_por_nombre(nom)
            for r in resultados: print(r)

        elif opcion == "5":
            for p in sistema.productos.values(): print(p)

        elif opcion == "6":
            print("Saliendo y guardando datos...")
            break
        else:
            print("Opción no válida.")

# Requisito 5: Punto de entrada del programa
if __name__ == "__main__":

    # Inicia la ejecución del menú principal
    mostrar_menu()
