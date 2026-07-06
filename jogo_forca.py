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


palavra = 'FORMIGA'

letras_certas = ['_'] * (len(palavra))

acertou = False

credito = int(5)

while acertou == False:
  chute = str(input('DIGITE UMA LETRA: ').upper())
  for c in palavra:
    if chute == c:
      letras_certas[palavra.index(c)] = chute
    else:
      credito -= 1
  print(''.join(letras_certas), palavra, credito)
  if palavra == ''.join(letras_certas):
    acertou = True