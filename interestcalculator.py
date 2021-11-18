capital=input("Capital ($): ")
capital=float(capital)
tasa=input("Tasa de interes (%): ")
tasa=float(tasa)/100
intereses=tasa*capital
intereses=round(intereses)
intereses=str(intereses)
print("Los intereses generados son: "+intereses+" pesos colombianos")
