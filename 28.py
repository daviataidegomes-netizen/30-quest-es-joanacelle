# atividade 28= Leia um valor informado pelo usuário. Verifique o tipo da variável; Caso seja possível interpretá-lo
# como um valor numérico: Se for um número inteiro, exiba o dobro; Caso seja um número real, exiba a
# metade; Caso não seja possível interpretar como número, exiba: “Tipo inválido”

valor = input('digite o valor desejado: ')
print (type(valor))

try:
    if "." in valor:
        valor1 = int(valor)
        dobro = valor1 * 2
        print(dobro)
    else:
        valor1 = float(valor)
        metade = valor1 / 2
        print(metade)
except ValueError:
    print('valor invalido')




