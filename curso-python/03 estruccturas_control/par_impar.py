
n = int(input("ingrese un numero entero:"))

if n != 0:
    if n > 0:
        if n % 2 == 0:
            print(f"el numero {n} es PAR POSITIVO")
        else:
            print(f"el numero {n} es IMPAR POSITIVO")
    else:
        if n % 2 == 0:
            print(f"el numero {n} es PAR NEGATIVO")
        else:
            print(f"el numero {n} es IMPAR NEGATIVO")
else:
    print(f"el numero {n} es NEUTRO")



