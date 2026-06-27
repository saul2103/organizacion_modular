class Cliente:
    
    def __init__(self, nombre: str, email: str, telefono: str, activo: bool, visitas: int):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.activo = activo
        self.visitas = visitas

    def __str__(self) -> str:
        estado = "Activo" if self.activo else "Inactivo"
        return f"{self.nombre} | {self.email} | {self.telefono} | {estado} | Visitas: {self.visitas}"