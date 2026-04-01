# atividade 30= Leia um valor informado pelo usuário. Tente convertê-lo para número inteiro. Caso não seja possível,
# exiba: “Entrada inválida”; Caso seja possível: Verifique se o número é par: Se for par e maior que 100 →
# exiba: “Par alto”; Se for par e menor ou igual a 100 → exiba: “Par baixo”; Caso não seja par, exiba:
# “Ímpar

entrada = input('digite o valor desejado: ')
print (type(entrada))

try: 
    valor = int(entrada)
    if valor % 2==0:
        if valor > 100:
            print('par maior')
        elif valor <= 100:
            print('par baixo')
    else: 
        print('impar')
except ValueError:
    print('entrada invalida')













