# atividade 24= Leia um número inteiro. Verifique se ele está no intervalo de 1 a 100 (inclusive). Se estiver:
# Verifique se o número é par ou ímpar; Exiba: “Par no intervalo” ou “Ímpar no intervalo”. Caso não
# esteja no intervalo, exiba: “Fora do intervalo”

n1 = int(input('digite um valor para n1: '))

if 0 <= n1 <= 100:
    if n1 % 2==0:
        print('par no intervalo')
    else:
        print('impar no intervalo')
else:
    print('fora do intervalo')