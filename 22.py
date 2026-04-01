# atividade 22=  Leia um valor informado pelo usuário. Tente convertê-lo para número inteiro. Caso não seja
# possível realizar a conversão, exiba: “Entrada inválida”. Caso a conversão seja bem-sucedida: Se
# o número for maior que 10, exiba: “Alto”. Caso contrário, exiba: “Baixo”
n1 = input('digite um valor para n1: ')
try:
    numero = int(n1)
    
    if numero > 10:
        print('alto')
    else:
        print('baixo')

except ValueError:
    print('entrada invalida')
