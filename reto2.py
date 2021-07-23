#letra1=chr(77)
#letra2=chr(101)
#print(letra1,letra2)

mensaje="771013210311711511697115321099711532113117101321081111153211211711011610111411111546"

lista=mensaje.split("32")
i=0
while i< len(lista):
    palabra=str.split(lista[i])
    print(palabra)
    for character in palabra:
      if character[i]=="1":
          print(chr(int(character[0]+character[1]+character[2])))
      elif character[i]!="1":
          print(chr(int(character[0]+character[1])))    
    i=i+1