# atividade 26= Leia um número inteiro. Classifique o número de acordo com as seguintes regras: Se for maior que 0:
# Se for menor que 10 → exiba: “Pequeno”; Se estiver entre 10 e 100 → exiba: “Médio”; Se for maior que
# 100 → exiba: “Grande”; Caso contrário, exiba: “Negativo ou zero

n1 = int(input('digite uma valor inteiro: '))

if 0 < n1 <= 10:
    print('pequeno')
    if 10 <= n1 <= 100:
        print('médio')
    else:
        print('grande')
else:
    print('negativo ou zero')




