meses = ("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","nomviembre","diciembre")

numero = int(input("Introduce un numero correspondiente al mes del año: "))
while True:
    if numero == 0:
        print("adio")
        break
    print("El mes del año indicado es : ",meses[numero-1])
    numero = int(input("Sigue introduciendo un numero correspondiente al mes del año: "))