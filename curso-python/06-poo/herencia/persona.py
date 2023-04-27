class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def detalle_persona(self):
        print(f"nombre: {self.nombre} \nedad: {self.edad}")
    
    def __str__(self):
        return f"nombre: {self.nombre} \nedad: {self.edad}"
    
class cliente(Persona):
    pass
    