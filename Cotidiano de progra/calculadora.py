monto = float(input("Digite el monto de la factura:"))
if monto >= 100:
    descuento = monto * 0.10
    preciocondescuento= monto - descuento
    print("felicidades obtienes un descuento del 10%", descuento)
    print("descuento aplicado:", descuento)
    print("Precio con descuento:", preciocondescuento)
else: 
  total_pagar=monto
  print("no aplica descuento")
  print("total a pagar:", total_pagar)