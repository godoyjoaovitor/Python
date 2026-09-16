string = str(input("Insira sua frase: "))
contador = 0
for contador in range (len(string)):
    if string[contador] != " ":
        contador += 1
print(f"Há {contador} letras")