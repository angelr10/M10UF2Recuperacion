def listaDeCompra(contenido):
    iva = float(input("Por favor introduce el IVA: "))
    total = 0
    vuelta = 0
    print("\nDetalles de la compra:")
    for precio, descuento in contenido.items():
        descuento_aplicado = precio * (descuento / 100)
        precio_con_descuento = precio - descuento_aplicado
        iva_aplicado = precio_con_descuento * (iva / 100)
        total_con_iva = precio_con_descuento + iva_aplicado
        print("producto num",vuelta,":",total_con_iva)
        total += total_con_iva
        vuelta+=1

    print(f"Total de la compra con IVA: {total:.2f} unidades monetarias")



