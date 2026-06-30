def calcular_imposto(valor):
  if valor <= 1000:
    imposto = valor * 0.1
  elif valor <= 2500:
    imposto = valor * 0.14
  else:
    imposto = valor * 0.2

  return imposto

valor1 = 500
valor2 = 10000
print(calcular_imposto(valor1))
print(calcular_imposto(valor2))