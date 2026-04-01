# atividade 12=
n1 = float(input('digite um valor para n1: '))
n2 = float(input('digite um valor para n2: '))

if n1 < n2:
    print(f'{n1} é maior que {n2}')
elif n2 < n1:
    print(f'{n2} é maior que {n1}')
else:
    print(f'{n2} e {n1} são iguais')