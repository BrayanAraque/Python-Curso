from sys import argv

if len(argv) == 3:
    nombre = argv[1]
    edad = int(argv[2])
    altura = float(argv[3])

    print(f"nombre: {nombre} \nedad: {edad} \naltura: {altura}")
    
else:
    print("error, ingrese los argumentos correctamente")
    