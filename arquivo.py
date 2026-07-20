import os

# Define a pasta do script
pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(pasta_atual, "palavras_jogo_forca.txt")

# Lê o conteúdo do arquivo

with open(caminho_arquivo, 'r', encoding="utf-8") as vasco:#se eu usar o o 'w' pra escrever em um arquivo ja criado,
    conteudo = vasco.read().splitlines()

for c in range(1,len(conteudo)-1):
    print(conteudo[c])