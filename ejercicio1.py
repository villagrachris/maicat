print ("Bienvenido al Supermercado La Ilusión")
print("Por Favor Ingrese su Nombre:")
Nombre = input()
print("Ingrese el monto de Carniceria:")
Gasto_Carniceria=float(input())
print("Ingrese el monto de Verduleria")
Gasto_Verduleria=float(input())
print("Ingrese el monto de Almacén")
Gasto_Almacen=float(input())

Consumo=Gasto_Carniceria+Gasto_Almacen+Gasto_Verduleria

print("Estimado",Nombre,"Su consumo en pesos es de:",Consumo)

print("Ingrese su numero de Tarjeta de credito del Banco Provincia")

num_tarjeta=int(input())

print(" Su pago con tarjeta de credito posee un 10% de descuento")

Descuento=Consumo*0.1

Total=Consumo-Descuento

print("Su compra con tarjeta de credito es:",Total)

exit()





