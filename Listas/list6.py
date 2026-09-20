objetos = {
    'Mouse' : 'Serve para usar no computador',
    'Teclado' : 'Serve para escrever no computador',
    'Monitor' : 'Serve para ver o video do computador'
}
procurado = str(input("Insira o item que voce quer saber a funcao: "))
if procurado in objetos:
    print(objetos[procurado])
else:
    print("objeto nao encontrado!")
