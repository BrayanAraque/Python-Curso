
def sumar(*args, **kwargs):
    suma = 0
    for n in args:
        suma += n
    return suma
    
    
sumar_total, datos = sumar(10,20,3,100,nombre = "brayan", edad = 20)
print("la suma total es:", sumar_total) 
print(datos)   