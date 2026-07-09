def jogar_adivinhacao():
    from random import randint
    
    
    acertou = False
    tentativas = 0
    
    while acertou == False:
      numero = randint(1,10)
      tentativas += 1
      if tentativas > 3:
        print("tentativas esgotadas")
        break
      try:
        chute = int(input("Chute um numero de 1 a 10 ==>>>> "))
    
        if chute != numero:
            if chute <1 or chute >10:
              print("Digite um numero de 1 a 10")
              continue #volta pro loop inicial
              if chute > numero:
                print(f"chute alto. Tente novamente. O numero era {numero}")
              else:
                print(f"chute baixo. Tente novamente. O numero era {numero}")
        else:
          print('parabens, voce acertou')
          acertou = True
      except ValueError: #tratamento de erros
        print('Digite um numero valido')
    
        
if __name__ == '__main__':
    jogar_adivinhacao()