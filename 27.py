# atividade 27= Leia dois números informados pelo usuário. Se ambos forem positivos, calcule e exiba a soma entre
# eles Caso contrário, calcule e exiba o produto entre eles

n1 = float(input('digite o valor para n1: '))
n2 = float(input('digite o valor para n2: '))

if n1 and n2 > 0:
    soma = n1 + n2
    print(soma)
else:
    produto = n1 * n2
    print(produto)