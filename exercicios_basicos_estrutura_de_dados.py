#dada a lista

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]

#a) maior elemento

maior = max(lista)


print(maior)

#b) imprima o menor elemento

menor = min(lista)
print(menor)

#c) imprima os numeros pares
print('NÚMEROS PARES')
for c in lista:
  if c % 2 == 0:
    print(c)


#d)Imprima o número de ocorrências do primeiro elemento da lista.

print("OCORRÊNCIAS DO PRIMEIRO NUMERO DA LISTA.")
numero_igual = 0
for num in lista:
  if num == lista[0]:
    numero_igual += 1
print(numero_igual)

#e) Imprima a média dos elementos.
print(sum(lista)/(len(lista)))

#f) imprima a soma dos números negativos
print('soma dos números negativos')
soma_negativos = 0
for c in lista:
  if c < 0:
    soma_negativos += c
print(soma_negativos)