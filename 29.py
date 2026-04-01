# atividade 29=  Leia um número inteiro. Verifique se ele é múltiplo de 5; Se for: Se o número for maior que 50 →
# exiba: “Múltiplo alto”; Caso contrário → exiba: “Múltiplo baixo”; Caso não seja múltiplo de 5, exiba: “Não é
# múltiplo”

n1 = int(input('digite o valor para n1: '))
if n1 % 5==0:
    if n1 > 50:
        print('multiplo alto')
    else:
        print('multiplo baixo')
else:
    print('não é multiplo')