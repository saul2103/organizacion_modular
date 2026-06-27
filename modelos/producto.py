class Producto:

    def __init__(self, nombre: str, precio: float, disponible: bool, categoria: str, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.disponible = disponible
        self.categoria = categoria
        self.stock = stock

    def __str__(self) -> str:
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.nombre} | {self.categoria} | ${self.precio:.2f} | {estado} | Stock: {self.stock}" 