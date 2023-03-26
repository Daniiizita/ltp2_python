"""
19) Escrever um algoritmo que lê um conjunto de 4 valores i, a, b, c, onde i é um 
valor inteiro e positivo e a, b, c, são quaisquer valores reais e os escreva. A seguir: 
a) Se i=1 escrever os três valores a, b, c em ordem crescente.
b) Se i=2 escrever os três valores a, b, c em ordem decrescente.
c) Se i=3 escrever os três valores a, b, c de forma que o maior entre a, b, c fique dentre os dois.

"""

i = int(input("Digite o valor de i: "))
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if i == 1:
    if a <= b and a <= c:
        if b <= c:
            print(a, b, c)
        else:
            print(a, c, b)
    elif b <= a and b <= c:
        if a <= c:
            print(b, a, c)
        else:
            print(b, c, a)
    elif c <= a and c <= b:
        if a <= b:
            print(c, a, b)
        else:
            print(c, b, a)
elif i == 2:
    if a >= b and a >= c:
        if b >= c:
            print(a, b, c)
        else:
            print(a, c, b)
    elif b >= a and b >= c:
        if a >= c:
            print(b, a, c)
        else:
            print(b, c, a)
    elif c >= a and c >= b:
        if a >= b:
            print(c, a, b)
        else:
            print(c, b, a)
elif i == 3:
    if a >= b and a >= c:
        if b >= c:
            print(b, a, c)
        else:
            print(c, a, b)
    elif b >= a and b >= c:
        if a >= c:
            print(a, b, c)
        else:
            print(c, b, a)
    elif c >= a and c >= b:
        if a >= b:
            print(a, c, b)
        else:
            print(b, c, a)
else:
    print("Valor inválido para i.")
