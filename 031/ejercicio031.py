def calcularIVA(cantidadSinIVA,IVA):
    if(int(IVA)!=21 or int(IVA)!=10 or int(IVA)!=4):
        IVA = int(21)
    cantidadIVA = int(cantidadSinIVA) * (int(IVA)/100)
    sumaTotal = int(cantidadSinIVA) + cantidadIVA
    print("El IVA calculado da : ",cantidadIVA)
    print("El total calculado da: ",sumaTotal)

