#entrada
consumo = float(input("ingrese el consumo del cliente:"))

if consumo >= 0:
    #proceso
    if consumo <= 100:
        #descuento de 10%
        dato_descuento = "10%"
        descuento = consumo * 0.10
    elif consumo > 100 and  consumo <= 200:
        #descuento de 20%
        dato_descuento = "20%"
        descuento = consumo + 0.20
    elif consumo > 200:
        #descuento del 30%
        dato_descuento = "30%"
        descuento = consumo * 0.30
        
        
    monto_descuento = consumo - descuento
    igv = monto_descuento * 0.19
    total_pagar = monto_descuento + igv
    #salida de datos
    print("=" * 30)
    print("--------factura de consumo---------")
    print("descuento que se aplica:", dato_descuento)
    print("="* 30)
    print("consumo:", consumo)
    print("descuento", descuento)
    print("monto con descuento", monto_descuento)
    print("IGV", igv)
    print("total a pagar", total_pagar)
    print("="* 30)
else:
    print("error al ingresar el consumo")
