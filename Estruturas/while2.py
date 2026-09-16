soma = 0
i = 0
while i < 5 :
    numero = float(input(f"Insira o {i+1} numero: "))
    if numero > 0:
        soma += numero
        i += 1
    else:
        print("Insira um valor valido!")

print(soma)