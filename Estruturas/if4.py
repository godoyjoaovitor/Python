n1 = float(input("Insira o primeiro numero: "))
n2 = float(input("Insira o segundo numero: "))
operacao = str(input("Qual operador voce quer usar?\nSoma: +\nSubtracao: -\nDivisao: /\nMultiplicacao: * "))
if operacao == str("+"):
    print(n1 + n2)
elif operacao == str("-"):
    print(n1 - n2)
elif operacao == str("/"):
    print(n1/n2)
elif operacao == str("*"):
    print(n1*n2)
else:
    print("Insira algo valido!")