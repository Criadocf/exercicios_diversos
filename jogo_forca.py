import random
import os

# Define a pasta do script
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(pasta_atual, "palavras_jogo_forca.txt")


#vou fazer todo o esquema de iterar sobre o .txt aqui fora da funcao principal(jogo_da_forca)
with open(caminho_arquivo, 'r', encoding='utf-8') as txt:
  conteudo = txt.read().splitlines() #essesplitlines() ja joga cada linha do arquivo .txt dentro de uma lista. EXECELENTE. entao 'conteudo' e uma lista

for c in range(conteudo.index('PALAVRAS DO JOGO DA FORCA')+1, len(conteudo)):
    palavra_sorteada = random.choice(conteudo)


def jogo_da_forca():
  palavra = palavra_sorteada
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
        print(f'O jogador era {palavra}')
        break

    print(''.join(letras_certas), tentativas) #junto as strings que foram 'jogadas soltas' dentro da lista, dessa forma imprimo como uma palavra completa.
    if palavra == ''.join(letras_certas):
      print('PARABÉNS, VOCÊ ACERTOU')
      acertou = True
if __name__ == '__main__':
    jogo_da_forca()