def es_primo(numero):
    Contador = 0
    
    for i in range(1, numero+1):
        if i == 1 or i == numero:
            continue
        
        #verifica que la division con los numeros hasta el
        # numero ingresado sea igual a 0
        if numero % i == 0:
            Contador += 1
            
    if Contador == 0:
        return True
    else:
        return False

def main():
    numero = int(input("ingrese un numero:"))
    
    if es_primo(numero):
        print("es primo")
    else:
        print("no es primo")     
if __name__ == "__main__":
    main()