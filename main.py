import pickle


class Producto:
    def _init_(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def _str_(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
    def _init_(self):
        self.productos = {}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].cantidad = cantidad
            if precio is not None:
                self.productos[id].precio = precio
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        for producto in self.productos.values():
            if producto.nombre == nombre:
                print(producto)

    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self.productos, f)

    def cargar_inventario(self, filename):
        with open(filename, 'rb') as f:
            self.productos = pickle.load(f)


def menu():
    print("\n1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar inventario")
    print("6. Guardar inventario en archivo")
    print("7. Cargar inventario desde archivo")
    print("8. Salir")


if _name_ == "_main_":
    inventario = Inventario()

    while True:
        menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad del producto (deje en blanco para no modificar): ")
            precio = input("Ingrese el nuevo precio del producto (deje en blanco para no modificar): ")
            if cantidad:
                cantidad = int(cantidad)
            if precio:
                precio = float(precio)
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            filename = input("Ingrese el nombre del archivo para guardar el inventario: ")
            inventario.guardar_inventario(filename)

        elif opcion == "7":
            filename = input("Ingrese el nombre del archivo para cargar el inventario: ")
            inventario.cargar_inventario(filename)

        elif opcion == "8":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
