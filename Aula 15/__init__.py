'''
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro
'''

'''entrada = input('Digite um número inteiro: ')

if entrada.isnumeric():

      number = int(entrada)

      if number % 2 == 0:
          print(f'O número {number} é par')

      else:
          print(f'O número {number} é ímpar')

else:
    print('Não é um número inteiro')'''


'''
Faça um programa que pergunte a hora ao usuário e, baseando - se no horário descrito, exiba a saudação apropriada.
EX: Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23
'''

time = input('Que horas são?: ')

if not time.isnumeric():
    print('Apenas números')

else:
    time = int(time)
    if time < 11:
        print('Bom dia!')

    elif time < 17:
        print('Boa tarde!')

    elif time < 23:
        print('Boa noite!')


'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"

'''

name = input('Digite seu nome')

if len(name) <= 4:
    print('Seu nome é curto')

elif len(name) <= 6:
    print('Seu nome é normal')

else:
    print('Seu nome é muito grande') 