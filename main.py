from modelos.cliente import Cliente
from modelos.producto import Producto
from servicios.restaurante import Restaurante

def main()->None:

    #crear restaurante
    restaurante = Restaurante("Restaurante Recetas de mi Sierra")

    # crear productos
    producto1 = Producto("Caldo de Pata", 4.99, True, "Comida Latacungueña", 50)
    producto2 = Producto("Seco de Pollo", 2.99, True, "Comida Quiteña", 30)
    producto3 = Producto("Papas con cuero", 2.50, False, "Comida Latacungueña", 0)
    producto4 = Producto("Hornado", 5.99, True, "Comida Ambateña", 20)

    #agregar productos al restaurante
    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)
    restaurante.agregar_producto(producto3)
    restaurante.agregar_producto(producto4)

    #crear clientes
    cliente1 = Cliente("Juan Perez", "jperez@gmail.com", "0983702256", True, 6)
    cliente2 = Cliente("Maria Lopez", "mlopez@gmail.com", "0936705569", True, 3)
    cliente3 = Cliente("Carlos Sanchez", "csanchez@gmail.com", "0998442256", False, 0)

    #agregar clientes al restaurante
    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)
    restaurante.agregar_cliente(cliente3)

    #mostrar información registrada
    restaurante.mostrar_clientes()
    restaurante.mostrar_productos()

    #mostrar búsquedas
    print("\n   Búsquedas   ")
    producto_buscado = restaurante.buscar_producto("Seco de Pollo")
    if producto_buscado:
        print(f"Producto encontrado: {producto_buscado}")
        
    cliente_buscado = restaurante.buscar_cliente("Maria Lopez")
    if cliente_buscado:
        print(f"Cliente encontrado: {cliente_buscado}")
    
if __name__ == "__main__":
    main()