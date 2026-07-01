# 1) Crie um arquivo com uma função chamada teste_args_kwargs() que recebe 3 argumentos e imprime cada um deles.

def teste_args_kwargs(a, b, c):
  print(f'argumento1: {a}\nargumento2: {b}\nargumento3: {c}')


teste_args_kwargs('ideia1', 'ideia2', 'ideia3')


# 2) agora vamos chamar a funcao utilizanmdo o *args.

argumentos = ('um', 2, 'tres')

teste_args_kwargs(*argumentos) #aqui no caso a variável 'argumentos' que é uma tupla está empacotada com os valores.


# 3) Teste a mesma funcão usando o **kwargs. Para isso, crie um dicionário com três argumentos:
def arg_dic(**kwargs): # 'kwargs é um dicionário agora por causa dos 2 asteriscos **
  for chave, valor in kwargs.items():
    print(f'{chave}:{valor}')


argumentos_dic = {'arg3':3, 'arg2': 'dois', 'arg1': 'um', 'arg0': 0}

arg_dic(**argumentos_dic)
