try:
    n1 = int(input('digite o valor para n1: '))
    n2 = int(input('digite o valor para n2: '))
    n3 = int(input('digite o valor para n3: '))

    valor = [n1 % 3, n2 % 3, n3 % 3]

    valor.sort(reverse=True)
    print(f'restos em ordem decrescente, {valor}')

except ValueError:
    print('entrada invalida')
