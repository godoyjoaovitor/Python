saldo = float(input("Insira seu saldo atual: "))
divida = float(input("Insira sua divida atual: "))
if divida > saldo:
    print("Voce tem um saldo negativo!")
else:
    print("Voce tem um saldo positivo!")