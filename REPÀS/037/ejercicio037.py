#introduce 100 sale 121.0

def amb_iva(ftotal, iva):
    cantidadIva = int(ftotal) * int(iva)/100
    return int(ftotal)+cantidadIva

ftotal = input('Introdueix el preu de tot el carrito: ')
print(amb_iva(ftotal, iva = 21))
