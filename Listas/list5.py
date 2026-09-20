dias = []
for i in range(1, 32):
    dias.append(i)
dia_nascido = int(input('Insira o dia que voce nasceu: '))
if dia_nascido in dias:
    dias.remove(dia_nascido)
    print(dias)
else:
    print("escreva um dia valido!")