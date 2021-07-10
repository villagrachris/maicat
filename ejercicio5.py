#Listas Ejericio de Python
infantiles=["Blanca Nieve","Los Tres Chanchitos","Cenicienta"]
novelas=["Don Quijote","La Novicia Rebelde"]
policiales=["Sherlok Holmes","Muerte en el Nilo"]

def ver_libros():
      categoria=input("ingrese la categoria deseada entre infantiles, novelas, policiales y todas:")
      if categoria=="infantiles":
          print(infantiles)
      elif categoria=="novelas":
          print(novelas)
      elif categoria=="policiales":
          print(policiales)
      elif categoria=="todas":
          print(infantiles,novelas,policiales)
    
                            
    

def menu():
    
    print("Bienvenido al sistema de gestión online de la biblioteca Nacional")
    seleccion=int(input("Ingrese que la selección que desea realizar. 1. Ver los libros disponibles 2. Eliminar libros 3. Agregar libros 4. Consultat el Stock"))
    if seleccion==1:
        ver_libros()
    #elif seleccion==2:
    ##    agregar_libros()
    ##elif seleccion==3:
    ##    eliminar_libros():
    ##elif seleccion==4:
    ##    consultar_stock():            
    else: menu() 

menu()
