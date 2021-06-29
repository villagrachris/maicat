print("Sistema de registros deportivos")
Genero=input("Ingrese su genero:").lower()
TipoGenero=Genero=="hombre"
print("Hombre:",TipoGenero)

Edad=int(input("Ingrese su edad:")) 
MEdad=Edad>=18
print("Es Mayor de edad:",MEdad)

Altura=float(input("Ingresa la altura:"))
Alto=Altura>1.8
print("Es Alto:",Alto)

print("Asignación de deporte")

Hockey=TipoGenero=Genero=="hombre"
print("Puede jugar al hockey:",Hockey)

Volley=TipoGenero=Genero=="mujer" and Alto
print("Puede jugar al volley:",Volley)

Rugby=MEdad>18 and MEdad<55

print("Puede jugar al Rugby")

print("Gracias por completar el registro")

exit()



