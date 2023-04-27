
class Persona:
   
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
        
    def mostrar_datos(self):
        print("nombre:", self.nombre)
        print("edad:", self.edad)
        
    def __str__(self):
        return f"nombre: {self.nombre} \nedad: {self.edad}"