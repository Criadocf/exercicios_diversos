import os
import random
# Define a pasta do script
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(pasta_atual, "palavras_jogo_forca.txt")


#vou fazer todo o esquema de iterar sobre o .txt aqui fora da funcao principal(jogo_da_forca)
with open(caminho_arquivo, 'r', encoding='utf-8') as txt:
  conteudo = txt.read().splitlines()

palavra_sorteada = random.choice(conteudo)
print(palavra_sorteada)