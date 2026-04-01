# atividade 16=
# Passo 1: Leitura do valor (Input sempre vem como string)
entrada = input("Digite algo: ")

# Mostra o tipo original da entrada
print(f"Tipo original da entrada: {type(entrada)}")

try:
    # Passo 2: Tentativa de conversão para número (float atende inteiros e decimais)
    valor_numerico = float(entrada)
    
    # Passo 3: Se a conversão funcionou, mostramos o quadrado
    quadrado = valor_numerico ** 2
    print(f"O valor é numérico. O quadrado de {valor_numerico} é: {quadrado}")
    
except ValueError:
    # Passo 4: Se der erro na conversão, informamos que não é numérico
    print("O valor inserido não é um número válido para cálculos.")