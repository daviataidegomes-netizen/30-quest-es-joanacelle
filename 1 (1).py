# tarefa 1= Leia um número inteiro e informe se ele é positivo ou negativo
n1 = int(input('digite um numero inteiro: '))
if n1 < 0:
    print(f'{n1} é negativo')
elif n1 == 0:
    print(f'{n1} é nulo')
else:
    print(f'{n1} é positivo')
