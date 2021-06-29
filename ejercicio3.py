print("Bienvenidos a Automotores Carlitos")
nombre=input("Ingrese su nombre:")
monto=float(input(nombre+"Ingrese su monto disponible"))
if monto < 1000000 :
      print("Con ese ", monto, " no se poseen autos de ese rango de precios por favor reingresar el monto")
      monto=float(input("Ingrese un nuevo monto disponible"))
      if monto < 1000000 :
         print( "Sigue siendo un monto inferior graciasy no podrá realizar ninguna compra, Gracias")
         exit()
      
marca=input("ingrese la marca del auto:").lower()

if marca!="fiat" and marca!="chevrolet" and marca!="ford":
        marca=input("Por favor ingresar una nueva marca: ").lower()
        if marca!="fiat" and marca!="chevrolet" and marca!="ford":
           print("Ustde ingreso una marca que no tenemos a la venta")
           exit()   
