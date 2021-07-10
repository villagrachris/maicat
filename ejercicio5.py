#Listas Ejericio de Python
infantiles=["Blanca Nieve","Los Tres Chanchitos","Cenicienta"]
novelas=["Don Quijote","La Novicia Rebelde"]
policiales=["Sherlok Holmes","Muerte en el Nilo"]

def ver_libros():
      categoria=input("ingrese la categoria deseada entre infantiles, novelas, policiales y todas:")
      if categoria=="infantiles":
          print(infantiles)
          menu()
      elif categoria=="novelas":
          print(novelas)
          menu()
      elif categoria=="policiales":
          print(policiales)
          menu()
      elif categoria=="todas":
          todos=infantiles+novelas+policiales
          print(todos)
          menu()
      else:
        print("Ingreso una categoria incorrecta por favor ingrese las correctas")
        ver_libros()

def eliminar_libros():

    seleccion=input("Ingrese el titulo del libro a eliminar")

    if seleccion in infantiles:
      infantiles.remove(seleccion)
      print("El titulo",seleccion,"que ingreso ha sido removido de la lista de infantiles")
      print(infantiles)
      menu()
    
    elif seleccion in policiales:
      infantiles.remove(seleccion)
      print("El titulo",seleccion,"que ingreso ha sido removido de la lista de infantiles")
      print(policiales)
      menu()
    elif seleccion in novelas:
      infantiles.remove(seleccion)
      print("El titulo",seleccion,"que ingreso ha sido removido de la lista de infantiles")
      print(novelas)
      menu()
    else:
     print("No existe el titulo ingreso por favor ingresar otro nuevamente\n") 
     eliminar_libros()    
 
def menu():
    
    print("Bienvenido al sistema de gestión online de la biblioteca Nacional")
    seleccion=int(input("1. Ver los libros disponibles\n 2. Eliminar libros \n 3. Agregar libros \n 4. Consultat el Stock \n 5. Salir" ))
    if seleccion==1:
        ver_libros()
    elif seleccion==2:
       eliminar_libros()
    #elif seleccion==2:
    ##    agregar_libros()
    ##elif seleccion==4:
    ##    consultar_stock():
    elif seleccion==5:
      print("Gracias por su visita a la Biblioteca Nacional")
      exit()             
    else: menu() 

menu()
