
def calcularCuadrado(valor):
    return valor **2

def añadirNumeroALista(funcion,valor):
    nuevaLista = []
    for i in valor:
        calculado = funcion(i)
        nuevaLista += [calculado]
    return nuevaLista