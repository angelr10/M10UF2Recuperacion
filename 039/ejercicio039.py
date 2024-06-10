def formaTriangulo():
    n = int(input("Introdueix l’alçada del triangle (enter positiu): "))
    for i in range(1, n+1, 2):#Delimita el numero mas grande que llegara cada fila
        for j in range(i, 0, -2):#Comenzara por el final de .2 en -2
            print(j,end="")
        print("")
