a = int(input("Introduce un valor en Euros : "))
b = int(input("Introduce un IVA : "))
bPorcentaje = b/100
resultado = a* bPorcentaje
print("La cantidad inserida es ",a," aplicando el IVA de ",b," da como resultado : ",resultado)
