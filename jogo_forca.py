
#ESQUELETO DO JOGO DA FORCA, TODAS AS LINHAS DE CÓDIGO SAIRÃO DESSA ESTRUTURA.
#palavra = 'caju'


#Letras_certas = ['_'] * (len(palavra))

#acertou = False

#while acertou == False:
  #chute = str(input('DIGITE UMA LETRA: '))
  #for c in palavra:
    #if chute == c:
      #letras_certas[palavra.index(c)] = chute
  #print(letras_certas)
  ######


palavra = 'RIVALDO'

letras_certas = ['_ '] * (len(palavra))

acertou = False

tentativas = 5

while acertou == False:
  letras_certas_copia = letras_certas.copy()
  chute = str(input('DIGITE UMA LETRA: ').upper())
  for indice, letra in enumerate(palavra):
    if chute == letra:
      letras_certas[indice] = chute

  if letras_certas == letras_certas_copia:
      tentativas -= 1
      if tentativas == 0:
        print('Suas tentativas acabaram, GAME OVER FILHOTE')
        break

  print(''.join(letras_certas), tentativas) #junto as strings que foram 'jogadas soltas' dentro da lista, dessa forma imprimo como uma palavra completa.
  if palavra == ''.join(letras_certas):
    print('PARABÉNS, VOCÊ ACERTOU')
    acertou = True