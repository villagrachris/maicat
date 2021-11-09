
mensaje="771013210311711511697115321099711532113117101321081111153211211711011610111411111546"

lista=mensaje.split("32")

print(lista)

i=0

while i< len(lista):
    palabra=str.split(lista[i])
    silaba=str(palabra)
    valor=silaba.find("1")
    print(valor) 
    if silaba[2]!="1":
     print(chr(int(silaba[2]+silaba[3])))
    elif silaba[2]=="1":
     print(chr(int(silaba[2]+silaba[3]+silaba[4])))    
    i=i+1



   