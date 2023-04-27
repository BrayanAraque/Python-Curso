
def convertir(valor_dolar,pais):
    cantidad_moneda = float(input(f"ingrese cantidad de {pais}:"))
    
    dolares = cantidad_moneda / valor_dolar
    #10.4562 10.45
    dolares = round(dolares, 2)
    print(f"tienes ${dolares} dolares")

def main():
    while True:
        menu = """
        1 - soles peruanos a dolares
        2 - pesos mexicanos a dolares
        3 - pesos colombianos a dolares
        4-salir
        ingrese una opcion:"""
        
        opcion = input(menu)
        
        if opcion == "1":
            convertir(3.61, "soles peruanos")
        elif opcion == "2":
            convertir(20, "pesos mexicanos")
        elif opcion == "3":
            convertir(3471.27, "pesos colombianos")
        elif opcion == "4":
            print("cerrando conversor de monedas")
            break
        else:
            print("opcion incorrecta !!!")
            print("vuelva a ingresar la opcion correctau")
        
        
#punto de inicio de la aplicacion
if __name__ == "__main__":
    main()