
Este proyecto implementa un sistema básico de gestión para un restaurante utilizando Programación Orientada a Objetos (POO) en Python. El sistema permite administrar productos (platos, bebidas, postres) y clientes registrados, demostrando los principios fundamentales de la programación modular.

### Funcionalidades principales:
- Registro y administración de productos del restaurante
- Registro y administración de clientes
- Búsqueda de productos y clientes
- Visualización organizada de la información

## Estructura del Proyecto
restaurante_app/
├── modelos/
│ ├── init.py
│ ├── producto.py # Clase Producto
│ └── cliente.py # Clase Cliente
├── servicios/
│ ├── init.py
│ └── restaurante.py # Clase Restaurante (servicio principal)
└── main.py # Punto de entrada del programa
### Responsabilidad de cada módulo:

- **modelos/producto.py**: Define la clase `Producto` con atributos que representan un artículo disponible en el restaurante.
- **modelos/cliente.py**: Define la clase `Cliente` con atributos que representan a una persona registrada en el sistema.
- **servicios/restaurante.py**: Define la clase `Restaurante` que actúa como contenedor y gestor de productos y clientes.
- **main.py**: Punto de entrada donde se crean objetos, se agregan al servicio y se muestra la información.

## Tipos de Datos Utilizados

### Clase Producto
| Atributo      | Tipo   | Descripción                                    |
|---------------|--------|------------------------------------------------|
| `nombre`      | `str`  | Nombre del producto                            |
| `precio`      | `float`| Precio en dólares (con decimales)              |
| `disponible`  | `bool` | Indica si el producto está disponible          |
| `categoria`   | `str`  | Categoría (ej: "Plato Principal", "Bebida")    |
| `stock`       | `int`  | Cantidad disponible en inventario              |

### Clase Cliente
| Atributo      | Tipo   | Descripción                                    |
|---------------|--------|------------------------------------------------|
| `nombre`      | `str`  | Nombre completo del cliente                    |
| `email`       | `str`  | Correo electrónico (identificador único)       |
| `telefono`    | `str`  | Número de contacto                             |
| `activo`      | `bool` | Estado de cuenta (activo/inactivo)             |
| `visitas`     | `int`  | Número de visitas al restaurante               |

### Clase Restaurante
| Atributo      | Tipo           | Descripción                                    |
|---------------|----------------|------------------------------------------------|
| `nombre`      | `str`          | Nombre del restaurante                         |
| `productos`   | `list[Producto]`| Lista de objetos `Producto`                   |
| `clientes`    | `list[Cliente]` | Lista de objetos `Cliente`                    |

Reflexión sobre Buenas Prácticas
La implementación de este sistema demuestra la importancia de aplicar principios fundamentales de programación en Python. El uso de identificadores descriptivos como "nombre", "precio" y "stock" en la clase Producto, o métodos como "agregar_producto()" y "mostrar_clientes()", permite que el código sea autoexplicativo y fácil de entender para cualquier desarrollador que lo lea. Esta claridad en los nombres reduce significativamente la necesidad de comentarios extensos y facilita el mantenimiento del código a largo plazo.

La selección adecuada de tipos de datos es otro aspecto crucial. Utilizar float para el precio permite manejar valores monetarios con decimales, int para el stock y las visitas asegura que solo se almacenen números enteros, bool para estados como disponible o activo representa claramente condiciones binarias, y str para texto permite operaciones como búsqueda y comparación. Además, las anotaciones de tipo añaden una capa adicional de documentación y permiten a las herramientas de desarrollo detectar posibles errores antes de la ejecución del programa.

El uso de listas como tipo compuesto en la clase Restaurante proporciona una solución elegante y flexible para almacenar múltiples objetos. Las listas permiten que el sistema crezca dinámicamente a medida que se agregan nuevos productos o clientes, facilitan la iteración para mostrar información, y simplifican la implementación de métodos de búsqueda. Esta estructura centraliza la gestión de múltiples objetos manteniendo el código ordenado y modular.

La organización modular del proyecto, separando el código en carpetas de modelos y servicios, ofrece beneficios significativos como la reutilización de código, facilidad de mantenimiento, escalabilidad y la posibilidad de probar cada módulo de forma independiente. Esta arquitectura sienta las bases para desarrollar aplicaciones más complejas y mantenibles en el futuro, demostrando que un diseño cuidadoso desde el inicio es fundamental para el éxito de cualquier proyecto de software.