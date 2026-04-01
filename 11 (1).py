# atividade 11=
n1 = int(input('digite um valor para n1: '))
if n1 % 2==0:
    if n1 > 0:
        print(f'{n1} é par e positivo')
    elif n1 == 0:
        print(f'{n1} é nulo')
    else:
        print(f'{n1} é par e negativo')
else:
    print(f'{n1} é impar')