import adivinhacao_chute #arquivo
import jogo_forca


def jogar():
    
    escolher_jogo = int(input('ESCOLHA UM JOGO'))
    if escolher_jogo == 1:
        adivinhacao_chute.jogar_adivinhacao() #funcao(jogaradivinhacao())
    elif escolher_jogo == 2:
        jogo_forca.jogo_da_forca()
    else:
        print('Digite uma opcao valida')
     

if __name__ == '__main__':
    jogar()