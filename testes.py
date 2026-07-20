import os


pasta_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(pasta_atual, "palavras_jogo_forca.txt")


with open(caminho_arquivo, 'r', encoding='utf-8') as teste:
  conteudo = teste.read().splitlines()
  
for c in range(conteudo.index('PALAVRAS DO JOGO DA FORCA')+1, len(conteudo)):
  print(conteudo[c])