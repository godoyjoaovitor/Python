i = 0
soma = 0
while i < 5:
    numero = float(input(f"Insira o {i+1} numero: "))
    soma += numero
    i += 1
media = soma / 5

print(f"A media é {media}")

