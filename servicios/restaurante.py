from modelos.cliente import Cliente
from modelos.producto import Producto

class Restaurante:

    def __init__(self,nombre: str):
        self.nombre=nombre
        self.clientes:list[Cliente]=[]
        self.productos:list[Producto]=[]

    def agregar_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def mostrar_clientes(self):
        print(f"\n    Clientes registrados en {self.nombre}   ")
        for cliente in self.clientes:
            print(cliente)

    def mostrar_productos(self):
        print(f"\n    Productos disponibles en {self.nombre}    ")
        for producto in self.productos:
            print(producto)

    def buscar_producto(self, nombre: str) -> Producto | None:
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
    
    def buscar_cliente(self, nombre: str) -> Cliente | None:
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre.lower():
                return cliente
        return None