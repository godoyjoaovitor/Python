string = str(input("Insira sua frase: "))
contador = 0
i = 0
while i < len(string):
    if string[i] == " ":
        contador += 1
    i += 1
print(contador)