def string(texto):
    vogais = 0
    arry_vogais = ('a', 'e', 'i', 'o', 'u')
    for i in texto:
        if i in arry_vogais:
            vogais += 1
    return vogais

print(string("Pedro"))