areas_pis = ["Menjador", 10.15, "Rebedor", 9.56, "Habitació1", 12.34, "Terrassa", 15.55, "Lavabo", 7.98, "Cuina", 12, "Habitació2", 12.23]

print("Imprimimos el segundo elemento: ",areas_pis[1])
#2
print("Imprimimos el ultimo elemento: ",areas_pis[-1])
#3
index_terrassa = areas_pis.index("Terrassa")
print("Imprimimos el area de la terraza: ",areas_pis[index_terrassa+1])
#4
print("Imprimimos el primer elemento al tercer elemento: ",areas_pis[:3])
#5
print("Imprimimos del tercer elemento al ultimo: ",areas_pis[3:])
#6
habitacion1 = areas_pis.index("Habitació1")
habitacion2 = areas_pis.index("Habitació2")
areahabitacion1 = areas_pis[habitacion1 + 1]
areahabitacion2 = areas_pis[habitacion2 + 1]
sumaDosHabitaciones = areahabitacion1+areahabitacion2
print("Imprimimos del total del area de las dos habitaciones: ",sumaDosHabitaciones)
#7
areas_pis[areas_pis.index("Lavabo") + 1] = 8.50
print("Modifica camps el area del lavabo y imprimimos la nueva lista area",areas_pis)
#8
print("Añadimos el area de \"paitio interior\" y 2.78 de las ultimas posiciones. imprimimos la nueva lista de area")
areas_pis.append("patio interior")
areas_pis.append(2.78)
print("Nueva list area con patio: ",areas_pis)
#9
totalAreaPiso = 0
for i in range(1,len(areas_pis),2):
    totalAreaPiso += areas_pis[i]
print("Imprimimos el total de la area del piso: ",totalAreaPiso)

