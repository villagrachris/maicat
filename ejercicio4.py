
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



print("Bienvenidos a Garbarino Compras")
ingreso=int(input("1. Para la compra de electrodomesticos.2 Audio/TV.3 Ambos productos"))
if ingreso==1:
 primer_compra=compra_electro()
elif ingreso==2:
 segunda_compra=compra_tvaudio()
 print(segunda_compra)      

    

