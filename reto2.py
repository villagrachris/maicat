
mensaje="771013210311711511697115321099711532113117101321081111153211211711011610111411111546"

lista=mensaje.split("32")
i=0
while i< len(lista):
    
    cod=[ele for sub in lista[i] for ele in sub]
    
    print(cod)
      
    i=i+1

   