#Cosmeticos
ventas={}
precioF=0
respuestaW=1
respuesta=1
yellow = '\033[33m'
white = '\033[37m'
green = '\033[32m'

while respuesta==1:
    print(green)
    print("||| Bienvendio al Menú |||")
    print(white)
    print("¿Que accion vas a realizar?")
    print("1-Registrar ventas")
    print("2-Consultar ventas")
    print("3-Salir del programa")
    seleccion=int(input("Ingrese una accion: \n"))
    
    if seleccion==1:
        while respuestaW==1:
            if ventas:
                NumVenta = max(ventas) + 1
            else:
                NumVenta = 1
        
            Articulo=input("¿Que cosmetico se ha vendido?: \n")
            pcs=int(input("¿Cuantas piezas fueron vendidas?: \n"))
            price=int(input(f"¿A que precio fue vendido el {Articulo}?: \n"))
            Recibo=[Articulo,pcs,price]
            ventas[NumVenta]=Recibo
            PrecioFinal=(precioF+price*pcs)
            print(yellow)
            print(f"El precio a pagar es de: ${PrecioFinal}")
            print(white)
            respuestaW=int(input("Quiere realizar otra venta?:  1 - SI o 0 - NO\n"))
        
    if seleccion==2:
        BuscarVenta=int(input("Que venta quieres buscar?: \n"))
        if BuscarVenta in ventas.keys():
            print(ventas[BuscarVenta])
            respuestaW=int(input("Quiere realizar otra busqueda?: 1 - SI o 0 - NO\n"))
        else:
            print("No se ha realizado alguna venta con ese numero de venta")
            respuestaW=int(input("Quiere realizar otra venta?:\n  1 - SI o 0 - NO \n" ))
            
        
    if seleccion==3:
        print("Ha finalizado correctamente el programa")
        break
        
        
        
                       