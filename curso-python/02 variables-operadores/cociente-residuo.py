"""
practica 01: calcular cociente y residuo
enunciado:halar el cociente y el residuo
(resto) de dos numeros enteros.
analisis:para la solucion de este problema,
se require que el usuario ingrese dos
numeros enteros y el sistema realice el 
calculo respectivo para hallar el cociente
y residuo.
"""

print("calcular cociente y residuo")

a = input("ingrese el primer numero:")
b = input("ingrese el segundo numero:")

a = int(a)
b = int(b)
 
cociente = a // b 
residuo = a % b

print("el cociente es:", cociente)
print("el residuo es:", residuo)