# atividade 25=  Leia um valor informado pelo usuário. Exiba o tipo da variável lida. Verifique se é possível
# converter o valor para número real (float). Se for possível, exiba o resultado da divisão desse
# número por 2. Caso contrário, exiba: “Não numérico”

valor = input("Digite um valor: ")

# Exibir tipo da variável
print("Tipo da variável:", type(valor))

try:
    numero = float(valor)
    resultado = numero / 2
    print("Resultado da divisão por 2:", resultado)
except ValueError:
    print("Não numérico")