import random

def jugar(vidas):
    numero_random = random.randint(1,100)
    numero_elegido = None
    
    while numero_random != numero_elegido:
        numero_elegido = int(input("ingrese jun numero entre 1 y 100:"))
        
        if numero_random < numero_elegido:
            print("elige un numero mas pequeño:")
            vidas -=1
        elif numero_random > numero_elegido:
            print("elige un numero mas grande:")
            vidas -= 1
        
        if vidas == 0:
            print("GAME OVER")
            break
        print(f"te quedan {vidas} vidas")
        
    if numero_elegido == numero_random:
        print("FELICIDADES GANASTE EL JUEGO")

def main():
    while True:
        menu = """
        ADIVINA EL NUMERO ALEATORIO
        1 - Nivel facil
        2 - Nivel intermedio
        3 - Nivel dificil
        4 - Salir
        INGRESE UNA OPCION: """
        
        opcion = input(menu)
        
        if opcion == "1":
            jugar (10)
        elif opcion == "2":
            jugar(7)
        elif opcion == "3":
            jugar (5)
        elif opcion == "4":
            print("CERRANDO JUEGO")
            break
        else:
            print("opcion incorrecta vuelve a ingresar")
        
        
if __name__ == "__main__":
    main()