
def compra_electro():
   imp_heladera=60000
   imp_lavarropa=45000
   imp_cocina=25000
   print("1.Disponemos de una heladera por $",imp_heladera,"2.Lavarropas por $",imp_lavarropa, "3.Cocinas por $",imp_cocina)
   select=int(input())
   if select==1:
      return(imp_heladera)
   elif select==2:
      return(imp_lavarropa)
   elif select==3:
      return(imp_cocina)
   else:
     print("No ingreso la opción correcta por favor seleccione la opción deseada")
     select=int(input())

def compra_tvaudio():
   
   imp_minicomponente=30000
   imp_led=45000
   imp_smarttv=125000
   print("1.Disponemos de Minicomponentes por $",imp_minicomponente,"2.Un TV Led por $",imp_led,"3.Equipos de Smart TV por $",imp_smarttv)
   select=int(input())
   if select==1:
      return(imp_minicomponente)
   elif select==2:
      return(imp_led)
   elif select==3:
      return(imp_smarttv)
   else:
     print("No ingreso la opción correcta por favor seleccione la opción deseada")
     select=int(input())  

def facturacion():
   
   num_tarjeta=input("Ingrese los 12 digitos de la tarjeta de credito")
   if len(num_tarjeta)==12:
      promo=input("¿Tienen un código de promoción disponible SI o NO").lower()
      if promo=="si":
         cod_promo=int(input("Ingrese el código de promoción que posee"))
         if cod_promo==1234:
          descuento=compra-5000
          print("Posee un descuento de $5000 pesos del total de su compra, se debitará de su tarjeta",descuento)
          print("Gracias por su compra")
          exit() 
         else:
          print("El código ingresado no posee ningún descuento disponible, se debitará de su tarjeta",compra)
          print("Gracias por su compra")
          exit()   
   else:
    print("ingreso un numero inferior a 12 digitos de su tarjeta de credito, por reingrese los numeros")
    facturacion()
      
            
print("Bienvenidos a Garbarino Compras")
ingreso=int(input("1. Para la compra de electrodomesticos\n 2. Audio/TV\n 3. Ambos productos\n"))
primer_compra=0.0
segunda_compra=0.0
tercer_compra=0.0
if ingreso==1:
 primer_compra=compra_electro()
elif ingreso==2:
 segunda_compra=compra_tvaudio()     
elif ingreso==3:
  opcion=int(input("Si desea Electrodomesticos indique 1 en caso que sea TV/audio indique 2"))
  if opcion==1:
     tercer_compra=compra_electro()
     
  elif opcion==2:
     tercer_compra=compra_tvaudio()
else:
   print("No ingreso ninguna de las opciones sugeridas, gracias por su visita")
   exit()

compra=primer_compra+segunda_compra
facturacion()



    

