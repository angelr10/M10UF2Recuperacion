def muestraYSuma(a,b):
    posicion = int(a)
    suma = 0
    while(int(posicion) <= int(b)):
        print(posicion)
        suma += posicion
        posicion +=1
    print(suma)