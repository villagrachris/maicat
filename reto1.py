largo=int(input ("Ingrese la longitud de la lista:" " "))
i=1
lista=[0,1]

while i<largo :
  
  suma=lista[i-1]+lista[i]
  lista.append(suma)
  i=i+1

print(lista)




