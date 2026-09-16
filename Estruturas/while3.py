quantidade = int(input("Insira quantos numero quer somar: "))
if quantidade <= 0:
    print("Insira um valor valido")
soma = 0
contador = 0
while contador != quantidade:
    numero = float(input(f"Insira o {contador + 1} numero: "))
    soma += numero
    contador += 1
print(soma)