"""
20) Escrever um algoritmo que lê um valor em reais e calcula qual o menor
 número possível de notas de 100, 50, 10, 5 e 1 em que o valor lido pode 
 ser decomposto. Escrever o valor lido e a relação de notas necessárias.

"""

valor = int(input("Digite o valor em reais: "))

notas100 = valor // 100
resto = valor % 100

notas50 = resto // 50
resto = resto % 50

notas10 = resto // 10
resto = resto % 10

notas5 = resto // 5
resto = resto % 5

notas1 = resto

print("Valor lido: R$", valor)
print("Notas de 100: ", notas100)
print("Notas de 50: ", notas50)
print("Notas de 10: ", notas10)
print("Notas de 5: ", notas5)
print("Notas de 1: ", notas1)
