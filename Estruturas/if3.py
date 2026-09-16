idade = int(input("Insira sua idade: "))
if idade <= 3:
    print("Bebe")
elif idade > 3 and idade <= 13:
    print("Crianca")
elif idade > 13 and idade < 18:
    print("Adolecente")
elif idade >= 18 and idade < 65:
    print("Adulto")
else:
    print("Idoso")