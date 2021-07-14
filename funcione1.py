jugadora=[27, 14, 20, 4, 30, 22, 3, 29, 8, 12, 5]
jugadorb=[20, 25, 1, 6, 15, 26, 23, 17, 27, 0, 9, 11]

def compra_propiedad (jugadorb,jugadora):
  compra = 0
  for numero in jugadora:
    if numero not in jugadorb:
      compra += 1
  
  print(compra)

compra_propiedad(jugadorb,jugadora)
