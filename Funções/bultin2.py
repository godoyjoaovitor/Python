from math import sqrt, pow
a = int(input("Insira o valor de a "))
b = int(input("Insira o valor de b "))
c = int(input("Insira o valor de c "))
delta = sqrt((pow(b,2)) - (4 * a * c))
x1 = (-b + delta) / 2 * a
x2 = (-b - delta) / 2 * a
print(x1, x2)