def saludar(nombre):
    #global nombre
    edad = 20
    return f"hola,{nombre} desde la funcion saludar"

def sumar( a ,b):
    return a + b

def restar(a=None,b=None):
    if a == None or b == None:
        print("error: debes enviar dos numeros a la funcion")
        return
    return a - b

saludo = saludar("brayan")
print(saludo)

suma = sumar(10,20)
print("la suma es", suma)

#resta = restar(b = 20, a = 40)
resta = restar()
print("la resta es", resta)



#print("hola desde fuera de la funcion", nombre)