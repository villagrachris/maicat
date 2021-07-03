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
           print("Usted ingreso una marca que no tenemos a la venta")
           exit()
puertas=int(input("Ingrese la cantidad de puertas del vehiculo que desea comprar:"))

if puertas!=3 and puertas!=5:
    puertas=int(input(" Solo disponemos de autos con 3 y 5 puertas cual desea comprar:"))
    if puertas!=3 and puertas!=5:
      print("No disponemos del vehiculo de su preferencia de puertas, Gracias por su visita!")
      exit()

if marca=="ford" and monto==1500000:
  print("Disponemos del modelo Ford K para su preferencia de compra")
  respuesta=input("Desea realizar la compra del vehiculo que le ofrecemos SI o NO:").lower()
  if respuesta=="si":
     print("Espere el llamado de un representante de ventas, Gracias por su visita")
     exit()
  else:
     print("Lo esperamos en otra oportunidad, gracias por su visita")
     exit()   
elif marca=="fiat" and (puertas==3 or puertas==5):
  print("Disponemos del modelo Punto para su preferencia de compra")
  respuesta=input("Desea realizar la compra del vehiculo que le ofrecemos SI o NO:").lower()
  if respuesta=="si":
     print("Espere el llamado de un representante de ventas, Gracias por su visita")
     exit()
  else:
     print("Lo esperamos en otra oportunidad, gracias por su visita")
     exit()
elif marca=="chevrolet" and puertas==5 and monto>2000000:
  print("Disponemos del modelo Zafira para su preferencia de compra")
  respuesta=input("Desea realizar la compra del vehiculo que le ofrecemos SI o NO:").lower()
  if respuesta=="si":
     print("Espere el llamado de un representante de ventas, Gracias por su visita")
     exit()
  else:
     print("Lo esperamos en otra oportunidad, gracias por su visita")
     exit()
else:
  print ("Le agradecemos la visita a nuestro sitio de compras y los esperamos para su proxima compra, Gracias!")   




