Ahorro_actual=0
while Ahorro_actual<100:
    deposito=int(input("Cuanto dinero vas a depositar hoy?"))
    Ahorro_actual+=deposito
    print("llevas:", Ahorro_actual)

if Ahorro_actual>100:
    print("Lo haz logrado!")
