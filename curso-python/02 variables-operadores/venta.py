"""
practica 02:  calcular precio de venta
enunciado: dado el valor de venta de 
productos, hallar el IGV (18%) y el 
precio de venta.
analisis: para la solucion de este problema,
se requiere que el usuario ingrese el valor
de venta del producto y el sistema realice el 
calculo respectivo para hallar el IGV y el
precio de venta, para esto use la siguiente expresion.

igv = vv * 0.18

pv = vv + igv
"""

#mensaje de la aplicacion
print("----REALIZAR UNA VENTA----")

#   entrada de datos
vv = float(input("ingrese valor de venta:"))

#operaciones
igv = vv * 0.18
pv = vv + igv

#salida de datos
print("=" * 25)
print("----FACTURA DE VENTA----")
print("=" * 25)
print("valor  de venta:" , vv)    
print("IGV:", igv)
print("precio de venta: ", pv)
print("=" * 25)