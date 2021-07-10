#Listas Ejericio de Python
infantiles=["Blanca Nieve","Los Tres Chanchitos","Cenicienta"]
novelas=["Don Quijote","La Novicia Rebelde"]
policiales=["Sherlok Holmes","Muerte en el Nilo"]

def ver_libros():
      categoria=input("ingrese la categoria deseada entre infantiles, novelas, policiales y todas:")
      if categoria=="infantiles":
          print(infantiles)
          return(menu())
      elif categoria=="novelas":
          print(novelas)
          return(menu())
      elif categoria=="policiales":
          print(policiales)
          return(menu())
      elif categoria=="todas":
          print(infantiles,novelas,policiales)
          return(menu())
      else:
        print("Ingreso una categoria incorrecta por favor ingrese las correctas")
        ver_libros()

def eliminar_libros():

    seleccion=input("Ingrese el titulo del libro a eliminar")

    if seleccion in infantiles:
      infantiles.remove(seleccion)
      print("El titulo",seleccion,"que ingreso ha sido removido de la lista de infantiles")
      print(infantiles)
      return(menu())
    

def menu():
    
    print("Bienvenido al sistema de gestión online de la biblioteca Nacional")
    seleccion=int(input("Ingrese que la selección que desea realizar. 1. Ver los libros disponibles 2. Eliminar libros 3. Agregar libros 4. Consultat el Stock"))
    if seleccion==1:
        ver_libros()
    elif seleccion==3:
       eliminar_libros()
    #elif seleccion==2:
    ##    agregar_libros()
    ##elif seleccion==4:
    ##    consultar_stock():            
    else: menu() 

menu()
