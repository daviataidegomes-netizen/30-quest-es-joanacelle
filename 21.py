#  atividade 21= Leia um número inteiro informado pelo usuário.Verifique se o número é positivo. Caso seja,
#analise se ele é múltiplo de 2 e de 3 ao mesmo tempo. Se atender a ambas as condições, exiba:
#“Múltiplo de 2 e 3”. Caso contrário, exiba: “Não atende”. Se o número não for positivo, exiba:
#“Número inválido”.
n1 = int(input('digite um valor para n1: '))
if n1 >= 0:
    if n1 % 2==0 and 3==0:
        print(f'{n1} é multiplo de 2 e de 3')
    else:
        print(f'{n1} não atende')
else:
    print('numero invalido')









