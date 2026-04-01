#atividade 18=
idade = int(input('digite a sua idade: '))
if idade < 18:
    print(f'Você tem {idade} anos, você é: Menor de idade')
elif 18 <= idade <= 59:
    print(f'Você tem {idade} anos, você é: Adulto')
else:
    print(f'Você tem {idade} anos, você é: Velho')